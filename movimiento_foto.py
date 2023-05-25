from datetime import datetime
import RPi.GPIO as GPIO
import time
import subprocess
import base64
from PIL import Image
 
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

      # Guardar la Hora y Fecha
      now = datetime.now()
      formatted_date = now.strftime('%d-%m-%Y %H:%M:%S')
      with open('/home/pi/sensores/sens_txt/movimiento.txt', 'a') as f:
          f.write(f'{formatted_date} - Movimiento detectado\n')   
      
      # Encender el LED
      GPIO.output(LED_PIN, GPIO.HIGH)

      # Tomar la foto
      command = "fswebcam -q -r 1280x720 /home/pi/sensores/movimiento/movimiento.jpg"
      subprocess.run(command, shell=True)

      # Cargar la imagen en formato JPG
      image_path = "/home/pi/sensores/movimiento/movimiento.jpg"
      image = Image.open(image_path)

      # Convertir la imagen a bytes
      image_bytes = image.tobytes()

      # Codificar los bytes en Base64
      base64_image = base64.b64encode(image_bytes).decode('utf-8')
      
      # Imprimir el resultado
      with open('/home/pi/sensores/movimiento/foto_base64.txt', 'w') as f:
          f.write(base64_image)

      # Borrar la foto
      command = "rm -f /home/pi/sensores/movimiento/movimiento.jpg"
      subprocess.run(command, shell=True)
      
      time.sleep(3)
    else:
      GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.5)
      
