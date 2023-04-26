import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
PIR_PIN = 14
GPIO.setup(PIR_PIN, GPIO.IN)
LED_PIN = 15
GPIO.setup(LED_PIN, GPIO.OUT)

print('Inciando sensor de movimiento')
GPIO.output(LED_PIN, GPIO.HIGH)
time.sleep(1)
GPIO.output(LED_PIN, GPIO.LOW)
time.sleep(0.5)
print ('Listo')

while True:
  if GPIO.input(PIR_PIN):
    print('Movimiento detectado')
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(3)
  else:
    print('No hay movimiento detectado')
    GPIO.output(LED_PIN, GPIO.LOW)
  time.sleep(0.5)
