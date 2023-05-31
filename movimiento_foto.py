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

      # Se abre la imagen y se codifica en base64
      with open("/home/pi/sensores/movimiento/movimiento.jpg", "rb") as img_file:
        b64_string = base64.b64encode(img_file.read())
      
      # Eliminamos el caracter "b" extra
      base64_image = b64_string.decode('utf-8')
      
      # Concatenamos la cabecera de imagen jpg para base64
      imagen_final = "data:image/jpg;base64, " + base64_image
      
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
      
