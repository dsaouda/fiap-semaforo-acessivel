import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(17, GPIO.IN)
GPIO.setwarnings(False)

topic = "/fiap/28scj/iot/semaforo/acessivel"
#host = "broker.hivemq.com"
#port = 1883

host = "m13.cloudmqtt.com"
port = 18088
user = "dpnqsysv"
password = "irztw2QzXI1t"


def on_connect(client, userdata, rc):
   print("conectou "+str(rc))
   client.subscribe(topic)

client.username_pw_set(user, password)
client = mqtt.Client("", clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")

client.on_connect = on_connect

client.connect(host, 1883, 60)

flag = 0
while(True):

   valor = GPIO.input(17)
   if (flag <> valor):
      flag = valor
      client.publish(topic, valor)

      print("enviou sinal para mqqt")
      #depois que enviou um sinal aguarda 5 segundos para pegar o próximo sinal. Medida implementada para não ficar fazendo o semáforo abrir e fechar a todo momento
      time.sleep(5)      
   
   # acender ou apagar led no protoboard      
   if (valor == 1):
      GPIO.output(4, 0)
      GPIO.output(27, 1)
   else:
      GPIO.output(4, 1)
      GPIO.output(27, 0)

   print("movimento" if valor == 1 else "")
   time.sleep(0.5)
