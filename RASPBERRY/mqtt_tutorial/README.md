# MQTT Tutorial 
Exemplo de uso do protocolo MQTT no raspberry. O exemplo de publish irá publicar algo em um tópico, e o exemplo de subscribe irá assinar um determinado tópico, e ficará rodando em loop eterno.

## Como rodar

Como o comando abaixo ficará em loop eterno, é recomendável que ele rode em background.
```
python subscribe_mqtt_tutorial.py &
```

Exemplo que irá publicar uma mensagem no tópico que o comando anterior, assinou
```
python publish_mqtt_tutorial.py
```

## Dependência

O script depende de uma library Python chamada paho-mqtt. Para instala-la, siga o procedimento nessa página:

https://pypi.python.org/pypi/paho-mqtt/1.1

Um servidor de MQTT deve estar rodando no Raspberry. Por exemplo, o mosquitto
