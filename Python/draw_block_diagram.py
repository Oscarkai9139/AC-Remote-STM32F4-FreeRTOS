from matplotlib import pyplot as plt
import sys
import os
import re

if __name__ == "__main__":

  # Check valid input arguements
  if(len(sys.argv) < 1):
    print("<error> invalid arguements")
    exit()
  else:
    f = open(sys.argv[1])

  # Read line & split
  line = f.readline()
  vals = re.findall(r'[-+]?[0-9]+', line)
  vals = list(map(int, vals))
  f.close()
  #***print(vals)

  # Data frame decode
  set_bit = 0
  data = []

  # parameters for time graph
  time = 0
  y = []
  t = []
  for val in vals:
    # Decode input signal
    if(val > 0):
      if(val > 3000):
        set_bit = 'T'
      elif(val > 2000):
        set_bit = 'S'
      elif(val > 1000):
        set_bit = 1
      else:
        set_bit = 0
    else:
      data.append(set_bit)

    if(val > 0):
      target_t = time + val
    else:
      target_t = time - val

    while(time != target_t):
      t.append(time)
      time+=1
      if(val > 0):
        y.append(1)
      else:
        y.append(0)

  print("[1] Start Decoding...")
  print("<log> length of data: ", len(data)-4, "bit")

  for bit in data:
    if (bit == 'T'):
      print("")
    print(bit, end="")
  print("")


  #plt.plot(t,y)
  #plt.show()

