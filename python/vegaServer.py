import asyncio
import websockets
import json as jsn
# import time as tm
import configparser
import traceback

########################################################
# Read configuration parameters for web  socket server #
########################################################
config = configparser.ConfigParser()
config.read('config.properties')
v_params = config['config.vega']
h_params = config['websocket.server']


async def get_devices(ws):
    await ws.send('{"cmd":"get_device_appdata_req"}')
    async for mess in ws:
        json_mess = jsn.loads(mess)
        if json_mess['cmd'] == 'get_device_appdata_resp':
            devices_list = json_mess['devices_list']
            sensor = {'cmd': 'get_devices', 'data': {
                'sensors': [{"devEui": item['devEui'], "description": item['devName']} for item in devices_list]}}
            js_str = jsn.dumps(sensor)
            return js_str


async def get_device_data(devEuiArr, ws):
    cli_str = '{"cmd":"get_data_req", "devEui":"%s", "select": {"limit": 1}}'
    # seconds = 43200  # 12 hours
    # from_date = tm.time() - seconds  # current time point minus 12 hours
    devEui_list = devEuiArr
    cmd_dict = {item: cli_str % (item) for item in devEui_list}
    res_list = []
    for devEui, cmd in cmd_dict.items():
        await ws.send(cmd)
    async for mess in ws:
        json_mess = jsn.loads(mess)
        if json_mess['cmd'] == 'get_data_resp':
            data = bytes.fromhex(json_mess['data_list'][0]['data'])
            ts = json_mess['data_list'][0]['ts']
            temp = (data[3] - data[4]) / 10
            res_list.append({"devEui": json_mess['devEui'], "temperature": temp, "timestamp": ts})
            if len(res_list) == len(devEui_list):
                break
    return jsn.dumps({"cmd": "get_device_data", "data": res_list})


async def get_device_history(dev_eui, ts, ws):
    cli_str = '{"cmd":"get_data_req", "devEui":"%s", "select": {"date_from": %d}}'
    devEui_list = dev_eui
    date_from = ts
    calc = lambda b: (b[3] - b[4]) / 10
    result = []
    for dev_eui in devEui_list:
        cmd = cli_str % (dev_eui, date_from)
        await ws.send(cmd)
    async for mess in ws:
        json_mess = jsn.loads(mess)
        if json_mess['cmd'] == 'get_data_resp':
            obj = {"devEui": json_mess['devEui'], "history": [{'utc_timestamp': item['ts'],
                                                               'temperature': calc(bytes.fromhex(item['data']))}
                                                              for item in json_mess['data_list']]}
            result.append(obj)
            if len(result) == len(devEui_list):
                break  # return jsn.dumps({"cmd": "get_device_history", "data": result})

    return jsn.dumps({"cmd": "get_device_history", "data": result})


async def producer(message, params):
    async with websockets.connect(params['ws_path']) as ws:
        auth_cmd = '{"cmd":"auth_req", "login":"%s", "password":"%s"}' % (params['login'], params['pass'])
        await ws.send(auth_cmd)
        try:
            json_object = jsn.loads(message)
            func_name = json_object['cmd']
            if func_name == 'get_devices':
                return await get_devices(ws)
            elif func_name == 'get_device_data':
                return await get_device_data(json_object['devEui'], ws)
            elif func_name == 'get_device_history':
                return await get_device_history(json_object['devEui'], json_object['utc_timestamp'], ws)
            else:
                return "Bad function name"
        except Exception as ex:
            traceback.print_exc()
            return 'Bad message format'


async def echo(ws, path):
    async for message in ws:
        prod_mess = await producer(message, v_params)
        await ws.send(prod_mess)


start_server = websockets.serve(echo, h_params['host'], h_params['port'])
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
