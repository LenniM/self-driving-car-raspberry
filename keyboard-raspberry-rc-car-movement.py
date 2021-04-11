

import time
import os
import platform
import pigpio

motor = 14
servo = 18



class _Getch:

   def __init__(self):
         try:
            self.impl = _GetchWindows()
         except ImportError:
            try:
               self.impl = _GetchUnix()
            except:
               print("error while init (getch)")

   def __call__(self): 
      return self.impl()


class _GetchWindows:
   def __init__(self):
      import msvcrt

   def __call__(self):
      import msvcrt
      return msvcrt.getch()

class _GetchUnix:
    def __init__(self):
        import tty, sys, termios 

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.t



if __name__ == '__main__':
   inkey = _Getch()
   

   if platform.system() == "Linux":
      while True:
         k = inkey()
         print(ord(k))
         print("\n")
         print("k")
         val = ord(k)


         if (val == 119):
            print("w clicked")
         elif (val == 100):
            print("d clicked")
         elif (val == 97):
            print("a clicked")
         elif (val == 27):
            print("esc clicked")
            break
         else:
            print("not a correct value")
      
         time.sleep(0.03)


   elif platform.system() == "Windows":
      while True:
         k = inkey()
         print(ord(k))
         val = ord(k)
         if (val == 119):
            print("w clicked")
         elif (val == 100):
            print("d clicked")
         elif (val == 97):
            print("a clicked")
         elif (val == 27):
            print("esc clicked")
            break
      
         time.sleep(0.03)
     
      
    

