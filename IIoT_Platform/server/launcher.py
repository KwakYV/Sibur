import paho.mqtt.client as mqtt
import configparser
from mqtt.parser_mqtt import *
from dao.crud_db import *
import logging as lg
import logging.handlers as handlers

logger = lg.getLogger('launcher.py')
logger.setLevel(lg.INFO)
formatter = lg.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(funcName)s')

loghandler = handlers.RotatingFileHandler('info_launcher.log', maxBytes=20000000, backupCount=10)
loghandler.setFormatter(formatter)

errorhandler = handlers.RotatingFileHandler('error_launcher.log', maxBytes=20000000, backupCount=10)
errorhandler.setLevel(lg.ERROR)
errorhandler.setFormatter(formatter)

logger.addHandler(loghandler)
logger.addHandler(errorhandler)

config = configparser.ConfigParser()
config.read('../configs/mqtt_set.properties')
sub1_params = config['config.server_1']
sub2_params = config['config.server_2']
topic_params = config['config.topic']

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    try:
        logger.info("Trying to subscribe the topic: %s" %(topic_params['topic_1']))
        client.subscribe(topic_params['topic_1'], qos=2)
        logger.info("Success subscribed to the topic: %s" %(topic_params['topic_1']))
    except Exception as ex:
        logger.error(ex)

def on_message(client, userdata, msg):
    logger.info("Getting messages from host %s:%s" %(sub1_params['ip_1'], int(sub1_params['port_1'])))
    d = msg.topic + " " + str(msg.payload)
    logger.info("Got message from topic %s" %(msg.topic))
    if 'innolabs' in msg.topic: # if 'innolabs' in msg.topic: #
        data = get_message(d)
        parsed_data = parser_message(data)
        print(parsed_data['gatewayID'])
        logger.info("Commiting message to data_base =========> ")
        try:
            comit_Data_Table(read_Device_table(deveui(parsed_data)), read_Gateway_table(parsed_data['gatewayID']), data_hex(parsed_data), parsed_data['time'], parsed_data['time']
                                , parsed_data['fCnt'], parsed_data['frequency'], parsed_data['RSSI'], 4, 5, data_val(parsed_data))
        except Exception as ex:
            logger.error(ex)
        print(deveui(parsed_data))
        print(data_val(parsed_data))
try:
    client = mqtt.Client(sub1_params['client_id_1'], clean_session=False).max_queued_messages_set(queue_size=100)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(sub1_params['ip_1'], int(sub1_params['port_1']), 60)
    client.loop_forever()
except Exception as ex:
    logger.error(ex)