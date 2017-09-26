# fiap-semaforo-acessivel
Projeto tem como objetivo simular um semáforo acessível.

# como funciona?

### raspberry pi e pir sensor

![raspberrypi-pir](https://raw.githubusercontent.com/dsaouda/fiap-semaforo-acessivel/master/docs/raspberrypi_pir.png)

Um sensor de presença pir envia um sinal 0 ou 1 para um dispositivo raspberry pi 3 através de um programa escrito em python. O programa em python envia o sinal para [hive mq](http://www.hivemq.com/) utilizando MQTT.

### NodeRed Flow

O fluxo em nodered que está hospedado no bluemix expõe um websoket com o valor do MQTT.

![flow](https://raw.githubusercontent.com/dsaouda/fiap-semaforo-acessivel/master/docs/1-fluxo.png)

### mobile acessível

A aplicação html5 executando no mobile recebe toda mudança do MQTT através do websocket do NodeRed e dependendo do sinal recebido emite um valor sonoro informando que o sinal está aberto ou fechado. Quando o sinal está aberto a tela do disposivo fica verde, quando está fechado fica vermelho.

### sinal aberto
![sinal aberto](https://raw.githubusercontent.com/dsaouda/fiap-semaforo-acessivel/master/docs/mobile-aberto.png)

### sinal fechado
![sinal fechado](https://raw.githubusercontent.com/dsaouda/fiap-semaforo-acessivel/master/docs/mobile-fechado.png)

# Ver funcionando

Para ver funcionando acesse https://dsaouda.github.io/fiap-semaforo-acessivel/ e envie um post com sinal 0 ou 1 para https://fiap-iot.mybluemix.net/semaforo-acessivel 

## Simulando sinal via CURL

enviando 0 `curl -s -X POST -H "Content-Type: text/plain" --data 0 https://fiap-iot.mybluemix.net/semaforo-acessivel` 

enviando 1 `curl -s -X POST -H "Content-Type: text/plain" --data 1 https://fiap-iot.mybluemix.net/semaforo-acessivel`

obs: Se preferir pode usar o postman

## Compatibilidade web browser mobile

Alguns navegadores mobile, como o chrome, não permitem o autoplay por padrão. O motivo é para poupar banda do dispositivo. Para liberar o recurso é necessário acessar chrome://flags e selecionar a opção **No user gesture is required** na opção **Autoplay policy**.
