def is_consq(line):
    """Return true if there is
    three consequtitive pair of letters."""

    stack = []
    for i in range( len(line) - 1 ):
        if line[i] == line[i+1]:
            stack.append(i)

    if len(stack) >= 3:
        for i in range(len(stack) - 1):
             if (i + 3) <= len(stack):
                if stack[i] + 2 == stack[i + 1]:
                    if stack[i + 1 ] + 2 == stack[i + 2]:
                         return True
    return False

file = open('words.txt')
for line in file:
     if is_consq(line.strip()):
          print line.strip()
          
          
#line = 'whippoorwills'
#if is_consq(line):
#     print line
