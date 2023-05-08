from datetime import datetime
import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
PIR_PIN = 14
GPIO.setup(PIR_PIN, GPIO.IN)
LED_PIN = 15
GPIO.setup(LED_PIN, GPIO.OUT)

#print('Inciando sensor de movimiento')
#GPIO.output(LED_PIN, GPIO.HIGH)
#time.sleep(1)
#GPIO.output(LED_PIN, GPIO.LOW)
#time.sleep(0.5)
#print ('Listo')


while True:
    if GPIO.input(PIR_PIN):
      now = datetime.now()
      formatted_date = now.strftime('%d-%m-%Y %H:%M:%S')
      with open('/home/pi/sensores/sens_txt/movimiento.txt', 'a') as f:
          f.write(f'{formatted_date} - Movimiento detectado\n')
      GPIO.output(LED_PIN, GPIO.HIGH)
      time.sleep(3)
    else:
      GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.5)
