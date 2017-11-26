import paho.mqtt.client as mqtt

# Funcao para ser usada pra quem quiser publicar algo,
# em algum topico. Ambos devem ser passados como parametro
def publish(topic, message):
    mqttc=mqtt.Client()
    mqttc.connect("192.168.0.145",1883,60)
    mqttc.loop_start()

    (result,mid)=mqttc.publish(topic,message,2)

    mqttc.loop_stop()
    mqttc.disconnect()
