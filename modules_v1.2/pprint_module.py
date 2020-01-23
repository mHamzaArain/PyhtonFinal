import pprint
# pprint.pprint()       ->  This print in a clean fomat 


# that format/display dictioanary values cleanly
dic = {'1':'hasdkf', '2':"uhdsfh", '3':'safuk'}

# This save in a clean way
formatSave = pprint.pformat(dic)
print(dic)

# This pint in a clean way
pprint.pprint(dic)  