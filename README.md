# fiap-semaforo-acessivel
Projeto tem como objetivo simular um semáforo acessível.

# como funciona?

### raspberry pi e pir sensor

![raspberrypi-pir](https://raw.githubusercontent.com/dsaouda/fiap-semaforo-acessivel/master/docs/raspberrypi_pir.png)

Um sensor de presença pir envia um sinal 0 ou 1 para um dispositivo raspberry pi 3 através de um programa escrito em python. O programa em python envia o sinal para [hive mq](http://www.hivemq.com/) utilizando MQQT.

### NodeRed Flow

O fluxo em nodered que está hospedado no bluemix expõe um websoket com o valor do MQQT.

![flow](https://raw.githubusercontent.com/dsaouda/fiap-semaforo-acessivel/master/docs/1-fluxo.png)

### mobile acessível

A aplicação html5 executando no mobile recebe toda mudança do MQQT através do websocket do NodeRed e dependendo do sinal recebido emite um valor sonoro informando que o sinal está aberto ou fechado. Quando o sinal está aberto a tela do disposivo fica verde, quando está fechado fica vermelho.

### sinal aberto
![sinal aberto](https://raw.githubusercontent.com/dsaouda/fiap-semaforo-acessivel/master/docs/mobile-aberto.png)

### sinal fechado
![sinal fechado](https://raw.githubusercontent.com/dsaouda/fiap-semaforo-acessivel/master/docs/mobile-fechado.png)
