words = [ 'indrajith', 'indraprastham','perambra' , 'calicut', 'kerala', 'india' , '673525']

for i in [0-6]:
    w = words[i]
#    print w, len(w)
    if len(w) > 10:
        print w
        words[0] = w

print words
