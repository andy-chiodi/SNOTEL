#! /usr/bin/python

# script to strip data from SNOTEL historic records obstained from http://wcc.sc.egov.usda.gov/nwcc/rgrpt?report=snowmonth_hist&state=WA
# output files should be ready to load into matlab

import sys, getopt

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# the def main and self-test here makes it so this can be run from command line or imported 
def main():
# read and open the input file  
  input1 = sys.argv[1]
  print(input1)
  myfile = open(input1,'r')
# march through lines and if first 4 characters evaluate as a float, then...
  fn=input1.strip( '.txt' );
  b =  '.dat'
  fn = fn + b
  outfile = open(fn,'w')
  for line in myfile:
      if is_number(line[0:4]):
           sep = line.split(",") 
# use that empty returns false to replace with bad value=-99.9
           sep2 = [-99.9 if not v else v for v in sep]
           myl = sep2
           print(sep2[0],sep2[2],sep2[3],sep2[5],sep2[6],sep2[8],sep2[9],sep2[11],sep2[12],sep2[14],sep2[15],sep2[17],sep2[18].rstrip())
# delete list item 1 through 16 by 3
           del myl[1:19:3] 
           outfile.write(' '.join(map(str,myl))) 
  outfile.close()
  myfile.close()
if __name__ == "__main__":
   main()


# get file name
