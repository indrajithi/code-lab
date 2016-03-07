from sys import argv
from os.path import exists
script, fr, to = argv

print "copying file from %s to %s" % (fr, to)

op_fr  = open(fr)
indata = op_fr.read()

print "input file is %s bytes long:" % len(indata0
