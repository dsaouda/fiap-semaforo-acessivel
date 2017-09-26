import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time
import config

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(17, GPIO.IN)
GPIO.setwarnings(False)

client = mqtt.Client("", clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")
client.username_pw_set(config.mqtt['username'], config.mqtt['password'])
client.connect(config.mqtt['host'], config.mqtt['port'], config.mqtt['timeout'])

flag = 0
while(True):

   valor = int(GPIO.input(17))
   if (flag != valor):
      flag = valor
      client.publish(config.mqtt['topic'], valor)

      print("enviou sinal para mqtt")
      #depois que enviou um sinal aguarda 5 segundos para pegar o próximo sinal. Medida implementada para não ficar fazendo o semáforo abrir e fechar a todo momento
      time.sleep(5)      
   
   # acender ou apagar led no protoboard      
   if (valor == 1):
      GPIO.output(4, 0)
      GPIO.output(27, 1)
   else:
      GPIO.output(4, 1)
      GPIO.output(27, 0)

   print("movimento" if valor == 1 else "sem movimento")
   time.sleep(0.5)
