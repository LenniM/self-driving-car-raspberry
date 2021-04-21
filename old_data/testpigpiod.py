import time
import pigpio
import sys,tty, termios

SERVO = 14

pi = pigpio.pi()

pi.set_servo_pulsewidth(SERVO,1500)
time.sleep(1)
pi.set_servo_pulsewidth(SERVO, 1600)
time.sleep(0.1)
pi.set_servo_pulsewidth(SERVO,0)





class _Getch:
	def __call__(self):
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(3)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch




def get():
	inkey = _Getch()
	while(1):
		k=inkey()
		if k!='':break
	if(k=='\x1b[A'):
		pi.set_servo_pulsewidth(SERVO,1600)
		print("fw")
	elif(k=='\x1b['):
		pi.set_servo_pulsewidth(SERVO,1500)
	if(k=='3'):
		print("stop")
		pi.stop()
		sys.exit()




def main():
	for i in range(25):
		get()

if(__name__=='__main__'):
	main()
