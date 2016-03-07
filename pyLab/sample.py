line = 'whippoorwills'
stack = []
for i in range(len(line) - 1):
#   if(i < len(line)):          
     if (line[i] == line[i + 1]):
          stack.append(i)
               
     print line[i],i

print line
print stack

for i in range(len(stack) - 1):
   if (i + 3) <= len(stack):
         if stack[i] + 2 == stack[i + 1]:
               if stack[i] + 2 == stack[i + 1]:
                     if stack[i] + 2 == stack[i + 1]:                        
                          print "Holly shit!"
