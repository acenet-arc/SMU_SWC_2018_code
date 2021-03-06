import numpy
import matplotlib.pyplot
import glob
import sys

def detect_problems(data):
  max_inflammation_0=numpy.max(data,axis=0)[0]
  max_inflammation_20=numpy.max(data,axis=0)[20]
  if max_inflammation_0==0 and max_inflammation_20==20:
    print('suspicious max')
  elif numpy.sum(numpy.min(data,axis=0))==0:
    print('Minima add up to zero!')
  else:
    print("Seems OK!")

def plot_data(data,filename):
  fig=matplotlib.pyplot.figure(figsize=(10.0,3.0))

  axes1=fig.add_subplot(1,3,1)
  axes2=fig.add_subplot(1,3,2)
  axes3=fig.add_subplot(1,3,3)

  axes1.set_ylabel('average')
  axes1.plot(numpy.mean(data,axis=0))

  axes2.set_ylabel('max')
  axes2.plot(numpy.max(data,axis=0))

  axes3.set_ylabel('min')
  axes3.plot(numpy.min(data,axis=0))

  fig.tight_layout()
  
  outFilename=filename[:-4]+".png"
  matplotlib.pyplot.savefig(outFilename)
  #matplotlib.pyplot.show()

# Main program

files=sys.argv[1:]

for file in files:
  print(file)
  data=numpy.loadtxt(fname=file, delimiter=',')

  detect_problems(data)

  plot_data(data,file)

