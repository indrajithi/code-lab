#def has_no(word,lst):
#     for letter in word:
#          if letter in list(lst):
#               return True
#     else: return True

def has_list(word, lst):
    if lst in word[0]:
        return True


file = open('words.txt')
lst1 = 'a'
for line in file:
     for ls in lst1:
         lst = ls
         if has_list(line.strip(),lst):
            print line.strip()



