from sys import argv
script,filename = argv

print "we are going to erase the file:"
print "do you want to continue?"

x = raw_input("> ")

if( x  == 'yea' or 'yes' or 'y' or '\n'):
    print "here we erase the file: type 'v' to view the file:"
    x = raw_input("> ")

    if x == 'v':
        print "you are viewing the %s file:", filename
        txt = open(filename,'r')
        print txt.read()

    print "do you wanna erase this file content:"
    x = raw_input("> ")

    if (x == "yes" or "y"):
        print "erasing..."
        txt = open(filename,'w')
        txt.truncate()
        line1 = raw_input("enter a line:")
        txt.write(line1)
        txt = open(filename,'r')
        print ".............file content............"
        print txt.read()
        print ".............file content............"
        txt.close()
else: print "oops"
