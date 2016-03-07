import anydbm
db = anydbm.open('captions.db','c')
db['chees.png'] = 'Photo of my friends.'
print db['chees.png']

