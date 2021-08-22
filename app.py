'''
	Raspberry Pi GPIO Status and Control
'''
import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#define sensors GPIOs
button = 20
senPIR = 16
#define actuators GPIOs
motorIn1 = 18
motorIn2 = 23
motorIn3 = 25
motorIn4 = 24
#initialize GPIO status variables
motorIn1Sts = 0
motorIn2Sts = 0
motorIn3Sts = 0
motorIn4Sts = 0
# Define button and PIR sensor pins as an input

# Define led pins as output
GPIO.setup(motorIn1, GPIO.OUT)   
GPIO.setup(motorIn2, GPIO.OUT) 
GPIO.setup(motorIn3, GPIO.OUT)
GPIO.setup(motorIn4, GPIO.OUT) 
# turn leds OFF 
GPIO.output(motorIn1, GPIO.LOW)
GPIO.output(motorIn2, GPIO.LOW)
GPIO.output(motorIn3, GPIO.LOW)
GPIO.output(motorIn4, GPIO.LOW)
	
@app.route("/")
def index():
	# Read GPIO Status
	motorIn1Sts = GPIO.input(motorIn1)
	motorIn2Sts = GPIO.input(motorIn2)
	motorIn3Sts = GPIO.input(motorIn3)
	motorIn4Sts = GPIO.input(motorIn4)
	templateData = {
      		'motorIn1'  : motorIn1Sts,
      		'motorIn2'  : motorIn2Sts,
      		'motorIn3'  : motorIn3Sts,
      		'motorIn4'  : motorIn4Sts,
      	}
	return render_template('index.html', **templateData)
	
@app.route("/<action>")
def action(action):
   
	if action == "straight":
		GPIO.output(motorIn1, GPIO.HIGH)
		GPIO.output(motorIn2, GPIO.LOW)
		GPIO.output(motorIn3, GPIO.HIGH)
		GPIO.output(motorIn4, GPIO.LOW)
	if action == "reverse":
		GPIO.output(motorIn1, GPIO.LOW)
		GPIO.output(motorIn2, GPIO.HIGH)
		GPIO.output(motorIn3, GPIO.LOW)
		GPIO.output(motorIn4, GPIO.HIGH)
	if action == "left":
		GPIO.output(motorIn1, GPIO.HIGH)
		GPIO.output(motorIn2, GPIO.LOW)
		GPIO.output(motorIn3, GPIO.LOW)
		GPIO.output(motorIn4, GPIO.LOW)
	if action == "right":
		GPIO.output(motorIn1, GPIO.LOW)
		GPIO.output(motorIn2, GPIO.LOW)
		GPIO.output(motorIn3, GPIO.HIGH)
		GPIO.output(motorIn4, GPIO.LOW)
	if action == "stop":
		GPIO.output(motorIn1, GPIO.LOW)
		GPIO.output(motorIn2, GPIO.LOW)
		GPIO.output(motorIn3, GPIO.LOW)
		GPIO.output(motorIn4, GPIO.LOW)
		     
	motorIn1Sts = GPIO.input(motorIn1)
	motorIn2Sts = GPIO.input(motorIn2)
	motorIn3Sts = GPIO.input(motorIn3)
	motorIn4Sts = GPIO.input(motorIn4)
   
	templateData = {
	 	'motorIn1'  : motorIn1Sts,
      		'motorIn2'  : motorIn2Sts,
      		'motorIn3'  : motorIn3Sts,
      		'motorIn4'  : motorIn4Sts,
	}
	return render_template('index.html', **templateData)
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080, debug=True)
