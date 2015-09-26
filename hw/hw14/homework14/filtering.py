dictlist = [{'first': 'James', 'last': 'Joule'},
            {'first': 'James', 'last': 'Watt'},
            {'first': 'Christian', 'last': 'Doppler'}]


def copyf(dictlist, key, valuelist):
    return [dictio for dictio in dictlist if dictio[key] in valuelist]


def mine(dictlist, key, valuelist):
    dictio = dictlist[:]
    for row in dictio:
        if row[key] not in valuelist:
            dictio.pop()
    return dictio

foo = mine(dictlist, 'first', ['James'])
