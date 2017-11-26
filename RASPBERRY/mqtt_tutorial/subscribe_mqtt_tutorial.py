import paho.mqtt.client as mqtt

def funcao_para_salvar_no_banco(conteudo):
   print "Salvando no banco: %s" % conteudo

def on_connect(mosq, obj, rc):
    # Start subscribe, with QoS level 0
    mqttc.subscribe("topic1", 0)
    mqttc.subscribe("topic2", 0)

def on_message(mosq, obj, msg):
    # Quando alguma mensagem chega no broker, o objeto 'msg' contem tanto
    # o topico onde aquela mensagem foi enviada, quanto o topico
    if (msg.topic == "topic1"):
        print "Mensagem que chegou no topico '%s': %s" % (msg.topic,msg.payload)
        funcao_para_salvar_no_banco(msg.payload)

# Criando o objeto
mqttc = mqtt.Client()

# Dizendo quais serao as fucoes que trataram os eventos
# de conexao, e acao ao chegar mensagem
mqttc.on_message = on_message
mqttc.on_connect = on_connect

# Conecta, passando o IP do broker, a porta, e nao
# lembro o que eh o terceiro parametro, desculpa :)
mqttc.connect("192.168.0.145", 1883,60)


# Entra em loop eterno
mqttc.loop_forever()
