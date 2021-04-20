import sys,termios, tty
import time
import pigpio


motor = 14
servo = 23

pi = pigpio.pi()

pi.set_servo_pulsewidth(motor, 1500)
time.sleep(1)

pi.set_servo_pulsewidth(motor, 1500)

class _Getch:
	def __call__(self):
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch


motor_speed = 1500
servo_speed = 1500
sz=0
def get():
	ms = 1500
	ss = 1500
	while True:
		
		inkey = _Getch()
		while(1):
			k=inkey()
			pi.set_servo_pulsewidth(servo, 1500)
			if k!= '':break
#		print(' cou pressed', ord(k))
		val = ord(k)
		if (val == 27):
			print("Esc clicked")
			pi.set_servo_pulsewidth(motor, 1500)
			sys.exit()
		elif (val == 119):
		#	ms = ms + 50
			pi.set_servo_pulsewidth(motor, 1550)
			print(ms)
			print("w clicked")
		#	time.sleep(0.5)
		elif (val == 115):
		#	ms = ms - 50
			pi.set_servo_pulsewidth(motor, 1500)
			time.sleep(0.6)
			pi.set_servo_pulsewidth(motor, 1380)
			print(ms)
			print("s clicked")
		elif (val == 100):

			if (ss <= 2000):
				print("max")
#				ss = ss + 50
			else:
				print("Servo auf Maximum (Plus)")
			pi.set_servo_pulsewidth(servo, 1750)
			print(ss)
			print("d clicked")
		#	time.sleep(0.01)
		elif (val == 97):
			if (ss >= 1200):
				print("max")
#				ss = ss - 50
			else:
				print("Servo auf Maximum (Minus)")

			pi.set_servo_pulsewidth(servo, 1350)
			print(ss)
			print("a clicked")
	#	time.sleep(0.01)
	ms = 1500
	ss = 1500
	pi.set_servo_pulsewidth(servo, ss)
	pi.set_servo_pulsewidth(motor, ms)
#	inkey = _Getch()
#	while(1):
#		k=inkey()
#		if k!= '':break
#	print(' cou pressed', ord(k))
#	val = ord(k)
#	if (val == 27):
#		print("Esc clicked")
#		pi.set_servo_pulsewidth(motor, 1500)
#		sys.exit()
#	elif (val == 119):
#		ms = ms + 50
#		pi.set_servo_pulsewidth(motor, ms)
#		print(ms)
#		print("w clicked")
#		return ms
#		time.sleep(0.5)
#	elif (val == 115):
#		ms = ms - 50
#		pi.set_servo_pulsewidth(motor, ms)
#		print(ms)
#		print("s clicked")
#		return ms
#	elif (val == 100):
#		ss = ss + 50
#		pi.set_servo_pulsewidth(servo, ss)
#		print(ss)
#		print("d clicked")
#		return ss

if(__name__=='__main__'):
	get()
#	while True:
#		motor_speed, servo_speed = get(motor_speed, servo_speed)


