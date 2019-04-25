
import grpc
from protos.aps import application_pb2
from protos.aps import application_pb2_grpc
from protos.aps import organization_pb2
from protos.aps import organization_pb2_grpc
from protos.aps import device_pb2
from protos.aps import device_pb2_grpc
from protos.aps import deviceProfile_pb2
from protos.aps import deviceProfile_pb2_grpc
from controller import protocontroller
from protos import iiot_pb2
from protos.sibur import device_pb2 as sib

import asyncio
import websockets

'''
device_request = device_pb2.CreateDeviceRequest()
    device_request.device.dev_eui = '363833355C38770F'
    device_request.device.name = 'TD-11 Sibur IoT Labs'
    device_request.device.description = 'TD 11 IIoT Labs from Sibur'
    device_request.device.skip_f_cnt_check = False

    dev_keys_request = device_pb2.CreateDeviceKeysRequest()
    dev_keys_request.device_keys.dev_eui = '363833355C38770F'
    dev_keys_request.device_keys.nwk_key = '1C38770F000000001C38770F3A480D4B'

    activate_request = device_pb2.ActivateDeviceRequest()
    activate_request.device_activation.dev_eui = '363833355C38770F'
    activate_request.device_activation.dev_addr = '0044002A'
    activate_request.device_activation.app_s_key = '2C003000363833353038470F66707A44'
    activate_request.device_activation.nwk_s_enc_key = '3038470F363833352C0030005C38770F'

    create_keys_request = device_pb2.CreateDeviceKeysRequest()
    create_keys_request.device_keys.dev_eui = '363833355C38770F'
    create_keys_request.device_keys.nwk_key = '1C38770F000000001C38770F3A480D4B'

    creds = grpc.ssl_channel_credentials(root_certificates=open('/Users/kwak_yv/fullchain.pem','rb').read())
    jwt = grpc.access_token_call_credentials('eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJsb3JhLWFwcC1zZXJ2ZXIiLCJhdWQiOiJsb3JhLWFwcC1zZXJ2ZXIiLCJzdWIiOiJ1c2VyIiwidXNlcm5hbWUiOiJhZG1pbiJ9.skwsaItibzeDIbltZZIrmIlp8JGhRzz61AHin7HPONM')
    composite_creds = grpc.composite_channel_credentials(creds, jwt)
    
    eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJsb3JhLWFwcC1zZXJ2ZXIiLCJhdWQiOiJsb3JhLWFwcC1zZXJ2ZXIiLCJzdWIiOiJ1c2VyIiwidXNlcm5hbWUiOiJrdmFreXV2In0.yz3rVuhLkvMHCJQIAeu7DmKlG7nPYytbIHL4JFaEdrI
'''

"""
def run():
    list_application_request = application_pb2.ListApplicationRequest(limit=10)
    org_list_request = organization_pb2.ListOrganizationRequest()
    org_list_request.limit = 10
    list_device_profile = deviceProfile_pb2.ListDeviceProfileRequest(limit=10)
    creds = grpc.ssl_channel_credentials(root_certificates=open('/Users/kwak_yv/fullchain.pem', 'rb').read())
    jwt = grpc.access_token_call_credentials('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJsb3JhLWFwcC1zZXJ2ZXIiLCJhdWQiOiJsb3JhLWFwcC1zZXJ2ZXIiLCJzdWIiOiJ1c2VyIiwidXNlcm5hbWUiOiJrdmFreXV2In0.yz3rVuhLkvMHCJQIAeu7DmKlG7nPYytbIHL4JFaEdrI')
    composite_creds = grpc.composite_channel_credentials(creds, jwt)
    with grpc.secure_channel('lpwa.ru:8080', composite_creds) as channel:
        res = organization_pb2_grpc.OrganizationServiceStub(channel).List(org_list_request)
        print(res)


if __name__ == '__main__':
    run()


"""
"""
    create_device_request.create_device.name = 'TD___11'
    create_device_request.create_device.dev_eui = '363833355C38770F'
    create_device_request.create_device.type = 'TD---11'
    create_device_request.create_device.measurement = "Celsius"
    create_device_request.create_device.port = 0
    create_device_request.create_device.appkey = '1C38770F000000001C38770F3A480D4B'
    create_device_request.create_device.profile = '868_ABP'
    create_device_request.create_device.application = 'SiburLab'
    create_device_request.create_device.plant = 'ZapSib'
"""

async def run():
    create_device_request = iiot_pb2.Request()
    create_device_request.type = iiot_pb2.MessageTypeRequest.Name(5)
    create_device_request.create_device.name = 'TD_11'
    create_device_request.create_device.dev_eui = '363833357B386B10'
    create_device_request.create_device.type = 'TD11'
    create_device_request.create_device.measurement = "Celsius"
    create_device_request.create_device.port = 0
    create_device_request.create_device.appkey = '7B386310000000007B3863101D481155'
    create_device_request.create_device.profile = 'Sibur profile'
    create_device_request.create_device.application = 'Sibur'
    create_device_request.create_device.plant = 'ZapSib'
    async with websockets.connect('ws://127.0.0.1:8766/') as ws:
        await ws.send(create_device_request.SerializeToString())
        response = await ws.recv()
        print(response)

asyncio.get_event_loop().run_until_complete(run())