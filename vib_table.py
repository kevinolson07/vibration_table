import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.output(17,GPIO.LOW)

pwmFrequency = 980
period = 1/pwmFrequency
duty1 = .5
duty2 = .75 
duty3 = 1

# PWM driver function
def pwm_driver(duty, dwell):
    for i in pwmFrequency: 
        timeHigh = duty*period
        GPIO.output(18,GPIO.HIGH)
        time.sleep(timeLLOW)
        timeLow = (1-duty)*period
        time.sleep(timeLow)

# Auto mode function
def autoMode():
    dwell = int(input("Enter dwell time in seconds: "))
    cycles = int(input("Enter number of cycles: "))

# Manual mode Function
def manualMode():
    duty = int(input("Enter \'1\' for \'50%\' duty, \'2\' for \'75%\' duty or \'3\' for \'100%\' duty: "))
    if duty == 1 or duty = 2 or duty = 3:
        if duty == 1:
            duty = duty1
        if duty == 2:
            duty = duty2
        if duty == 3:
            duty = duty3
        dwell = 0
    else:
        print("Value not valid")
        
    pwm_driver(duty, dwell)

# User input 
while True:
    try: 
        mode = int(input("Enter \'1\' for auto mode or \'2\' for mnanual mode: "))
        if mode == 1:
            autoMode()
        elif mode == 2:
            manaulMode()
        else:
            print("Number not valid. try again")
    except ValueError:
        print("Value not valid. try again")