import grpc

def connection():
    with open('/Users/erguj/git_rep_2/IIoT_Platform/grpc_lora_test/http-key.pem', 'rb') as f:
        creds = grpc.ssl_channel_credentials(f.read())
        jwt = grpc.access_token_call_credentials('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJsb3JhLWFwcC1zZXJ2ZXIiLCJhdWQiOiJsb3JhLWFwcC1zZXJ2ZXIiLCJzdWIiOiJ1c2VyIiwidXNlcm5hbWUiOiJhZG1pbiJ9.sBe3chmhhgMaDBq-W-g6OicAA-aMFdW46D2udG1oVVI')
        comp = grpc.composite_channel_credentials(creds, jwt)
        conn = grpc.secure_channel('lpwa.ru:8080', comp)
    return conn