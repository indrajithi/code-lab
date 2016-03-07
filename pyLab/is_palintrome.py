def is_palintrom(s):
    for i in range(len(s)):
        if s[i] != s[-i - 1]:
            return False
    return True

print is_palintrom(raw_input("enter a string: "))
for i in range(5):
    print 'love you'
