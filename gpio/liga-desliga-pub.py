import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(17, GPIO.IN)
GPIO.setwarnings(False)

def on_connect(client, userdata, rc):
   print("Connected with result code "+str(rc))
   client.subscribe("/fiap/28scj/dhjv")

def on_message(client, userdata, msg):
	val = int(msg.payload)
	print(val)
	GPIO.output(4, val)

client = mqtt.Client("", clean_session=True, userdata=None, 
	                 protocol=mqtt.MQTTv311, transport="tcp")

client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60)

#GPIO.cleanup()
flag = 0
while(True):

   valor = GPIO.input(17)
   if (flag <> valor):
      flag = valor
      client.publish("/fiap/28scj/dhjv", valor)
      print("enviou mqtt")
         
   if (valor == 1):
      GPIO.output(4, 0)
      GPIO.output(27, 1)
   else:
      GPIO.output(4, 1)
      GPIO.output(27, 0)

   print(valor)
   time.sleep(1)
