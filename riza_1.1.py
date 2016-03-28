import RPi.GPIO as GPIO
import time
import random

ir_r = 22 
ir_l = 7 
mr_r1 = 15
mr_r2 = 16
mr_l1 = 18
mr_l2 = 22

GPIO.setmode( GPIO.BOARD )
GPIO.setup( ir_r, GPIO.IN, pull_up_down=GPIO.PUD_UP )
GPIO.setup( ir_l, GPIO.IN, pull_up_down=GPIO.PUD_UP )
GPIO.setup( mr_r1, GPIO.OUT )
GPIO.setup( mr_r2, GPIO.OUT )
GPIO.setup( mr_l1, GPIO.OUT )
GPIO.setup( mr_l2, GPIO.OUT )

def motor_r_forward():
	GPIO.output( mr_r1, 0 )
	GPIO.output( mr_r2, 1 )

def motor_r_reverse():
	GPIO.output( mr_r1, 1 )
	GPIO.output( mr_r2, 0 )

def motor_l_forward():
	GPIO.output( mr_l1, 1 )
	GPIO.output( mr_l2, 0 )

def motor_l_reverse():
	GPIO.output( mr_l1, 0 )
	GPIO.output( mr_l2, 1 )

def move_forward():
	motor_r_forward()
	motor_l_forward()
	
def move_back():
	motor_r_reverse()
	motor_l_reverse()
	
def turn_right():
	motor_r_reverse()
	motor_l_forward()
	
def turn_left ():
	motor_r_forward()
	motor_l_reverse()
	
try:
	
	while True:
		
		ir_rin = GPIO.input( ir_r )
		ir_lin = GPIO.input( ir_l )

		if ir_rin == 1 and ir_lin == 1 :
			move_forward()
			time.sleep( 0.1 )

		elif ( ir_rin == 0 ) and ( ir_lin == 1 ):
			move_back()
			time.sleep( 2 )
			turn_left()
			time.sleep( 2 )

		elif ( ir_rin == 1 ) and ( ir_lin == 0 ):
			move_back()
			time.sleep( 2 )
			turn_right()
			time.sleep( 2 )

		else:
			judgement = { 1 : turn_right, 2 : turn_left }
			random_func = random.choice( [ 1, 2 ] )
			judgement[ random_func ]()
			time.sleep( 2 )

			if random_func == 1 and GPIO.input( ir_r ) == 0 and GPIO.input( ir_l ) == 0 :
				turn_left()
				time.sleep( 4 )
					
				if GPIO.input( ir_r ) == 0 and GPIO.input( ir_l ) == 0 :
					turn_left()
					time.sleep( 2 )

			elif random_func == 2 and GPIO.input( ir_r ) == 0 and GPIO.input( ir_l ) == 0 :
				turn_right()
				time.sleep( 4 )
					
				if GPIO.input( ir_r ) == 0 and GPIO.input( ir_l ) == 0 :
					turn_right()
					time.sleep( 2 )

except KeyboardInterrupt:
	GPIO.cleanup()
	
