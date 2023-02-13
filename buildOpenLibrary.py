from json import *

nb_turn = 5

def openArchives():
    with open('proGameArchives.json', 'r') as file: 
        data = load(file)
    return data

def getData(nb_turn): 
    data = openArchives()
    if isinstance(data, list):
        length = len(data)
    values = []
    for i in range(nb_turn):
        tmp = []
        for j in range(length): 
            tmp.append(data[j]['moves'][i])
        values.append(tmp)
    return values

def dictionaryToArray(dictionary, index):
    return [tuple[index] for tuple in dictionary] 

def countMoves(array):
    count_moves = {}
    for i in array:
        if i in count_moves:
            count_moves[i] += 1
        else:
            count_moves[i] = 1
    return count_moves

def sortMoves(countedMoves):
    sortedMoves = sorted(countedMoves.items(), key = lambda x: x[1], reverse=True)
    return dictionaryToArray(sortedMoves, 0)

def createOpenLibrary(nb_turn): 
    result = []
    values = getData(nb_turn)
    for i in range(nb_turn):
        result.append(sortMoves(countMoves(values[i])))
    return result

def stockOpenLibrary(nb_turn):
    data = createOpenLibrary(nb_turn)
    with open('openLibrary.json', 'w') as file:
        dump(data, file)
    

#print(createOpenLibrary(5))
stockOpenLibrary(5)

