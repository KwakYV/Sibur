
import grpc
from protos.aps import application_pb2
from protos.aps import application_pb2_grpc
from protos.aps import organization_pb2
from protos.aps import organization_pb2_grpc
from protos.aps import device_pb2
from protos.aps import device_pb2_grpc
from protos.aps import deviceProfile_pb2
from protos.aps import deviceProfile_pb2_grpc






def run():
    list_application_request = application_pb2.ListApplicationRequest(limit=10, search="SiburLab")
    org_list_request = organization_pb2.ListOrganizationRequest()
    org_list_request.limit = 10
    list_device_profile = deviceProfile_pb2.ListDeviceProfileRequest(limit=10)

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
    with grpc.secure_channel('lpwa.ru:8080', composite_creds) as channel:
        res = organization_pb2_grpc.OrganizationServiceStub(channel).List(org_list_request)
        org_id = res.result[0].id
        app_list = application_pb2_grpc.ApplicationServiceStub(channel).List(list_application_request)
        app_id = app_list.result[0].id
        list_device_profile.organization_id = org_id
        list_device_profile.application_id = app_id
        profile_list = deviceProfile_pb2_grpc.DeviceProfileServiceStub(channel).List(list_device_profile)
        profile_id = profile_list.result[0].id
        device_request.device.device_profile_id = profile_id
        device_request.device.application_id = app_id
        #device_pb2_grpc.DeviceServiceStub(channel).Create(device_request)
        #device_pb2_grpc.DeviceServiceStub(channel).CreateKeys(create_keys_request)
        device_pb2_grpc.DeviceServiceStub(channel).Activate(activate_request)


if __name__ == '__main__':
    run()
