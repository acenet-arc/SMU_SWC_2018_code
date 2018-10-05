import sys
import numpy

def main():
   script = sys.argv[0]
   action = sys.argv[1]
   assert action in ['--max', '--mean','--min'], \
      'Action ' + action + ' is not recognized'

   filenames = sys.argv[2:]
   if len(filenames) == 0:
      process(sys.stdin, action)
   else:
      for filename in filenames:
         filehandle = open(filename, 'r')
         process(filename, action)
         filehandle.close()

def process(filehandle, action):
   data = numpy.loadtxt(filehandle, delimiter=',')

   if action == '--max':
      values = numpy.max(data, axis=1)
   elif action == '--mean':
      values = numpy.mean(data, axis=1)
   elif action == '--min':
      values = numpy.min(data, axis=1)

   for m in values:
      print(m)

if __name__ == '__main__':
   main()
