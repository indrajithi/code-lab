def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint

print ask_ok('Do you really want to quit?',10)
print ".............\n"
print  ask_ok('OK to overwrite the file?', 2)
print "..............\n"
print ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')


