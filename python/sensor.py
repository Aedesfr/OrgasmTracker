import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import paho.mqtt.client as mqtt

# Configuration du MQTT
BROKER = 'localhost'  # Si Node-RED et Mosquitto sont sur le même Pi
PORT = 1883
PULSE_TOPIC = 'sensors/pulse'
TEMP_TOPIC = 'sensors/temperature'
PRESSURE_TOPIC = 'sensors/pressure'  # New topic for anal pressure sensor

# Initialisation de l'I2C et de l'ADS1115 (pour les capteurs)
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)

# Pulse sensor on A0
pulse_chan = AnalogIn(ads, ADS.P0)

# Temperature sensor on A1
temp_chan = AnalogIn(ads, ADS.P3)

# Anal pressure sensor on A2
pressure_chan = AnalogIn(ads, ADS.P2)

# Configuration du client MQTT
client = mqtt.Client()
client.connect(BROKER, PORT, 60)

# Boucle de lecture
try:
    while True:
        # Lecture du Pulse Sensor via ADS1115 A0
        pulse_value = pulse_chan.value  # Valeur analogique brute du capteur
        voltage_pulse = pulse_chan.voltage  # Convertir en tension (facultatif)
        print(f"Pulse sensor value: {pulse_value}, Voltage: {voltage_pulse:.2f}V")

        # Lecture du capteur de température via ADS1115 A1
        temp_value = temp_chan.value
        voltage_temp = temp_chan.voltage
        print(f"Temperature sensor value: {temp_value}, Voltage: {voltage_temp:.2f}V")

        # Lecture du capteur de pression anale via ADS1115 A2
        pressure_value = pressure_chan.value
        voltage_pressure = pressure_chan.voltage
        print(f"Pressure sensor value: {pressure_value}, Voltage: {voltage_pressure:.2f}V")

        # Publier les données via MQTT
        client.publish(PULSE_TOPIC, pulse_value)
        client.publish(TEMP_TOPIC, temp_value)
        client.publish(PRESSURE_TOPIC, pressure_value)

        # Pause avant la prochaine lecture
        time.sleep(0.2)

except KeyboardInterrupt:
    print("Terminé.")

finally:
    client.disconnect()

