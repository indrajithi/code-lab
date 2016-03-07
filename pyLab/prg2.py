from sys import argv

script , filename = argv

txt = open(filename)

print "here is your file %s: " % filename
print txt.read()

#print "type another filename:"
#file_nw =  raw_input("> ")

#txt_nw = open(file_nw)

#print txt_nw.read()
print "--------------"
print txt.read()
