import paho.mqtt.client as mqtt
import config

def on_connect(client, userdata, rc, result):
    print('conectou no mqtt' + str(rc))
    client.subscribe(config.mqtt['topic'])

def on_message(client, userdata, msg):	
    val = str(msg.payload)
    print(val)
	

client = mqtt.Client("", clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")

#callback
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(config.mqtt['username'], config.mqtt['password'])
client.connect(config.mqtt['host'], config.mqtt['port'], config.mqtt['timeout'])

client.loop_forever()