import grpc
import configparser


########################################################
# Read configuration parameters for web  socket server #
########################################################
config = configparser.ConfigParser()
config.read('../configs/integration.properties')
cert_path = config['certificate.settings']
host_settings = config['host.settings']


def connection():
    with open(cert_path['root_cert'], 'rb') as f:
        creds = grpc.ssl_channel_credentials(f.read())
        jwt = grpc.access_token_call_credentials('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJsb3JhLWFwcC1zZXJ2ZXIiLCJhdWQiOiJsb3JhLWFwcC1zZXJ2ZXIiLCJzdWIiOiJ1c2VyIiwidXNlcm5hbWUiOiJhZG1pbiJ9.sBe3chmhhgMaDBq-W-g6OicAA-aMFdW46D2udG1oVVI')
        comp = grpc.composite_channel_credentials(creds, jwt)
        conn = grpc.secure_channel('{}:{}'.format(host_settings['host'],host_settings['port']), comp)
    return conn
