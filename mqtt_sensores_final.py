import paho.mqtt.client as mqtt
import json
from datetime import datetime

# Definir variables
MQTT_HOST = "127.0.0.1"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 60
# pandorafms/raspberry/*sensor*


# Extraemos la hora actual
timestamp = datetime.now()

nombres = ['BMP280', 'CCS811', 'DHT-22', 'BMP280', 'DHT-22', 'CCS811']
# Nombre del .txt donde se guarda el dato
sensores = ['altitud', 'eco2', 'humedad', 'presion', 'temperatura', 'tvoc']
descripciones = ['Relative altitude in metres', 'CO2 Equivalent in Parts Per Million', 'Relative humidity in the environment', 'Atmospheric pressure in Hectopascals', 'Temperature in degrees Celsius', 'Total Volatile Organic Compounds in Parts Per Billon']

for nombre, sensor, descripcion in zip(nombres, sensores, descripciones):

    filename = '/home/pi/sensores/sens_txt/{}.txt'.format(sensor)

    with open(filename, 'r') as file:
        dato = file.read()

    MQTT_MSG = {"timestamp": str(timestamp), "data": dato, "description": descripcion}
    MQTT_MSG_JSON = json.dumps (MQTT_MSG)
    MQTT_TOPIC = "pandorafms/raspberry/{}/{}".format(nombre,sensor)

    # Definir la función de evento on_publish
    def on_publish(client, userdata, mid):
        print("Published message...")

    # Iniciar el cliente MQTT
    mqttc = mqtt.Client()
    mqttc.on_publish = on_publish

    # Conectar con el Broker MQTT
    mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

    # Publicar el mensaje en el Broker
    mqttc.publish(MQTT_TOPIC, MQTT_MSG_JSON, retain=True)
    
# Desconectar del Broker MQTT
mqttc.disconnect()
