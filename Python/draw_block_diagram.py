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

  # parameters for time graph
  time = 0
  y = []
  t = []
  for val in vals:
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

  plt.plot(t,y)
  plt.show()

