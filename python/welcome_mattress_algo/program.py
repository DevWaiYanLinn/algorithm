# Try giving an input of "7 21", it would give an output like this below.
# ---------.|.---------        
# ------.|..|..|.------        
# ---.|..|..|..|..|.---        
# -------WELCOME-------        
# ---.|..|..|..|..|.---        
# ------.|..|..|.------        
# ---------.|.---------    

def vinc():
  while True:
    l = input("Enter size of N and M (note: M must be 3 times of N) and N must be 5 or greater than 5: ")
    n, m = l.split(" ")
    n, m = int(n), int(m)
    if m == 3 * n and n >= 5 and m % 3 == 0:
      d = n//2
      c = 1
      o = 1
      for i in range(d,0,-1):
          print("-"*(i*3),".|."*(c),"-"*(i*3),sep='')
          c += 2
      for i in range(5, n+1, 2):
          o += 3
      print("-"*(o),"WELCOME","-"*(o),sep='')
      c = n - 2
      for i in range(1,d+1):
          print("-"*(i*3),".|."*(c),"-"*(i*3),sep='')
          c -= 2
      break
    else:
       print("\033[91m"+"Invalid input value error! Please try again."+"\033[0m")
       continue
vinc()