import asyncio
import websockets
import json as jsn
import time as tm


# get_devices, get_data, get_device_appdata
# 393337386C37570C

async def main():
    async with websockets.connect('ws://192.168.10.12:8766/') as ws:
        await ws.send('{"cmd":"get_device_data", "devEui":[]}')
        response = await ws.recv()
        print(response)

        await ws.send('{"cmd": "get_device_history", "devEui":["343438357137550E"], "utc_timestamp":1542716804000}')
        response = await ws.recv()
        print(response)

        await ws.send('{"cmd": "get_devices"}')
        response = await ws.recv()
        print(response)
    #async with websockets.connect('ws://192.168.10.10:8766/') as ws:
    #async with websockets.connect('ws://10.0.100.253:8765/') as ws:
'''
        auth_cmd = '{"cmd":"auth_req", "login":"%s", "password":"%s"}' % ('root', '123')
        await ws.send(auth_cmd)
        res = ws.recv()
        print(res)

        await ws.send('{"cmd":"get_device_appdata_req"}')
        async for mess in ws:
            msg = jsn.loads(mess)
            if msg["cmd"] == "get_device_appdata_resp":
                break
        print(msg)
        #363833354C38620F
        #cli_str = '{"cmd":"get_data_req", "devEui":"363833354C38620F", "select": {"limit": 1}}'
        #await ws.send(cli_str)
        #async for mess in ws:
        #    print(mess)
        # add timestamp
        #await  ws.send('{"cmd":"get_device_appdata_req"}')

'''







async def get_devices():
    async with websockets.connect('ws://192.168.10.13:8002/ws') as ws:
        await ws.send('{"cmd":"auth_req", "login":"god", "password":"god"}')
        response = await ws.recv()

        await ws.send('{"cmd":"get_device_appdata_req"}')
        dev_list_data = await ws.recv()
        devices_list_json = jsn.loads(dev_list_data)
        devices_list = devices_list_json['devices_list']
        print(devices_list)
        sensor = {'sensor': [{"devEui": item['devEui'], "description": item['devName']} for item in devices_list]}
        js_str = jsn.dumps(sensor)
        return js_str


async def get_device_data(js_str):
    cli_str = '{"cmd":"get_data_req", "devEui":"%s", "select": {"date_from": %d, "limit": 10}}'
    auth_cmd = '{"cmd":"auth_req", "login":"god", "password":"god"}'
    seconds = 43200  # 12 hours
    from_date = tm.time() - seconds  # current time point minus 12 hours
    devEui_list = jsn.loads(js_str)
    cmd_dict = {item: cli_str % (item, from_date) for item in devEui_list}
    res_list = []
    async with websockets.connect('ws://192.168.10.13:8002/ws') as ws:
        await ws.send(auth_cmd)
        response = await ws.recv()
        for devEui, cmd in cmd_dict.items():
            await ws.send(cmd)
            dev_data = await ws.recv()
            dev_data_json = jsn.loads(dev_data)
            data = bytes.fromhex(dev_data_json['data_list'][0]['data'])
            temp = (data[3] + data[4]) / 10
            res_list.append({devEui: temp})
    return jsn.dumps(res_list)

calc = lambda b: (b[3] + b[4]) / 10

# date_from = 1540494000
async def get_device_history(js_str):
    cli_str = '{"cmd":"get_data_req", "devEui":"%s", "select": {"date_from": %d}}'
    auth_cmd = '{"cmd":"auth_req", "login":"god", "password":"god"}'
    js_params = jsn.loads(js_str)
    devEui_list = js_params['devEui']
    date_from = js_params['utc_timestamp']

    result = []
    async with websockets.connect('ws://192.168.10.13:8002/ws') as ws:
        await ws.send(auth_cmd)
        await ws.recv()
        for devEui in devEui_list:
            cmd = cli_str % (devEui, date_from)
            await ws.send(cmd)
            dev_data = await ws.recv()
            dev_data_json = jsn.loads(dev_data)
            hist_data = dev_data_json['data_list']
            obj = {"devEui": devEui, "history": [{'utc_timestamp': item['ts'],
                                                  'temperature': calc(bytes.fromhex(item['data']))}
                                                 for item in hist_data]}

            result.append(obj)
            print(result)
    return jsn.dumps(result)


asyncio.get_event_loop().run_until_complete(main())
# asyncio.get_event_loop().run_until_complete(get_device_data('["393337386C37570C"]'))
#asyncio.get_event_loop().run_until_complete(
 #   get_device_history('{"cmd": "get_device_history", "devEui":["393337386C37570C"], "utc_timestamp":1540494000}'))
