import jwt



def run():
    key='verysecret'
    jwt_token = jwt.encode(payload={"iss": "lora-app-server",
                                    "aud": "lora-app-server",
                                    "sub": "user",
                                    "username": "kvakyuv"}, key=key, algorithm='HS256', )



if __name__ == '__main__':
    run()
