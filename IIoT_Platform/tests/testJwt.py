import jwt



def run():
    key='verysecret'
    jwt_token = jwt.encode(payload={"iss": "lora-app-server",
                                    "aud": "lora-app-server",
                                    "sub": "user",
                                    "username": "kvakyuv"}, key=key, algorithm='HS256', )



if __name__ == '__main__':
    run()
"""
select t.deveui, t.value
from
(
select first_value(d.id) over (partition by sensor_id order by ppndt desc) val, d.*, dev.deveuistr deveui
from iiot.sensor s 
Join iiot.device dev on s.device_id = dev.id and dev.deveuistr in (:lst)
join iiot.data d on d.sensor_id = s.id
) t where  t.val = t.id;


select dev.deveuistr deveui, d.ppndt ts, COALESCE(d.value,0.0)
        from iiot.sensor s 
        Join iiot.device dev on s.device_id = dev.id and dev.deveuistr in ('363833357B386B10')
        join iiot.data d on d.sensor_id = s.id
        where d.effdt < to_timestamp(1547516339) AT TIME ZONE 'UTC'

"""