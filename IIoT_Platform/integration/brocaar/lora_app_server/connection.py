import grpc
import configparser
import jwt

########################################################
# Read configuration parameters for web  socket server #
########################################################
config = configparser.ConfigParser()
config.read('../configs/integration.properties')
cert_path = config['certificate.settings']
host_settings = config['host.settings']
jwt_settings = config['jwt.settings']

def connection():
    with open(cert_path['root_cert'], 'rb') as f: #eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJsb3JhLWFwcC1zZXJ2ZXIiLCJhdWQiOiJsb3JhLWFwcC1zZXJ2ZXIiLCJzdWIiOiJ1c2VyIiwidXNlcm5hbWUiOiJrdmFreXV2In0.yz3rVuhLkvMHCJQIAeu7DmKlG7nPYytbIHL4JFaEdrI
        creds = grpc.ssl_channel_credentials(f.read())#eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJsb3JhLWFwcC1zZXJ2ZXIiLCJhdWQiOiJsb3JhLWFwcC1zZXJ2ZXIiLCJzdWIiOiJ1c2VyIiwidXNlcm5hbWUiOiJhZG1pbiJ9.sBe3chmhhgMaDBq-W-g6OicAA-aMFdW46D2udG1oVVI
        jwt = grpc.access_token_call_credentials('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJsb3JhLWFwcC1zZXJ2ZXIiLCJhdWQiOiJsb3JhLWFwcC1zZXJ2ZXIiLCJzdWIiOiJ1c2VyIiwidXNlcm5hbWUiOiJhZG1pbiJ9.sBe3chmhhgMaDBq-W-g6OicAA-aMFdW46D2udG1oVVI')
        comp = grpc.composite_channel_credentials(creds, jwt)
    with open(cert_path['root_cert'], 'rb') as f:
        creds = grpc.ssl_channel_credentials(f.read())
        jwt_token = jwt.encode(payload={"iss": "lora-app-server",
                                        "aud": "lora-app-server",
                                        "sub": "user",
                                        "username": "{}".format(jwt_settings['user'])}, key=jwt_settings['key'], algorithm='HS256')
        jwt_str = grpc.access_token_call_credentials(str(jwt_token,'utf-8'))
        comp = grpc.composite_channel_credentials(creds, jwt_str)
        conn = grpc.secure_channel('{}:{}'.format(host_settings['host'],host_settings['port']), comp)
    return conn