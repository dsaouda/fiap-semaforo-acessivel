import paho.mqtt.client as mqtt
import sys
import config

valor = int(sys.argv[1])
print("movimento" if valor == 1 else "sem movimento")

client = mqtt.Client(client_id="", clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")
client.username_pw_set(config.mqtt['username'], config.mqtt['password'])
client.connect(config.mqtt['host'], config.mqtt['port'], config.mqtt['timeout'])

client.publish(config.mqtt['topic'], valor)