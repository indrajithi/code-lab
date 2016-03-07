from sys import argv
print len(argv)
prompt = '> '
if (len(argv) == 4):
    script, first, second, third = argv
    print "the script name is:", script
    print "first arg is :", first
    print "second arg is:", second
    print "third arg is :", third
else: print "input three arguments"
