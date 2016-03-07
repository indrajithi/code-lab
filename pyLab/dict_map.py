def dict_map(file):
    my_dictionary = dict()
    for line in file:
        my_dictionary[line.strip()] = 'present'
    return my_dictionary

file = open('words.txt')
dictionaty = dict_map(file)
in_str = raw_input('Enter a word to check: ')
if in_str in dictionaty:
    print "Hurray! ",
    print "%s is present in the dictionary" % in_str
else:
    print "Nope! ",
    print "%s is not present in the dictionary" % in_str
