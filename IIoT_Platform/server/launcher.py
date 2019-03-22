import paho.mqtt.client as mqtt
import configparser
from IIoT_Platform.mqtt.parser_mqtt import *
from IIoT_Platform.dao.crud_db import *

config = configparser.ConfigParser()
config.read('set.properties')
sub1_params = config['config.server_1']
sub2_params = config['config.server_2']
topic_params = config['config.topic']

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(topic_params['topic_1'], qos=2)

def on_message(client, userdata, msg):
    d = msg.topic + " " + str(msg.payload)
    if 'innolabs' in msg.topic: # if 'innolabs' in msg.topic: #
        print(d)
        data = get_message(d)
        parsed_data = parser_message(data)
        comit_Data_Table(read_Device_table(deveui(parsed_data)), 1, data_hex(parsed_data), parsed_data['time'], parsed_data['time']
                         , parsed_data['fCnt'], parsed_data['frequency'], parsed_data['RSSI'], 4, 5, data_val(parsed_data))

client = mqtt.Client(sub1_params['client_id_1'], clean_session=False).max_queued_messages_set(queue_size=100)
client.on_connect = on_connect
client.on_message = on_message
client.connect(sub1_params['ip_1'], int(sub1_params['port_1']), 60)
client.loop_forever()