#  It is used to store complex data

import shelve

# ###################Write file
# shelfFile = shelve.open('mydata')
# shelfFile['cats'] = ['Zopphie', 'Clara', 'Fat-tail']
# shelfFile.close()

# ##################Reading file
shelfFile = shelve.open('mydata')
print(shelfFile.keys())                     # KeysView(<shelve.DbfilenameShelf object at 0x00000000021A44E0>)
print(list(shelfFile.keys()))              # ['cats']
print(list(shelfFile.values()))            # [['Zopphie', 'Clara', 'Fat-tail']]