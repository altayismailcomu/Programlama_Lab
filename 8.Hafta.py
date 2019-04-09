import random
#table_size = 19
#hash_table = []
#for i in range(table_size):
#   hash_table.append(0)

#print(hash_table)

def createMyHashTable(N):
    myTable = []
    for i in range (N):
        myTable.append(0)
    return myTable

my_table = createMyHashTable(19)

def my_hash(size,key):
    return key % size

def insert(myTable,key):
    isCollision = False
    index = my_hash(len(myTable),key)
    if (myTable[index] == 1):
        isCollision = True
    else:
        myTable[index] = 1

    return isCollision

def myTest(size = 13, Insert = 10):
    m_h_1 = createMyHashTable(size)
    c = 0
    for s in range (Insert):
        number = random.randint(0,1000)
        if(insert(m_h_1,number) == True):
            c = c + 1
    print(m_h_1)
    return c

insert(my_table,100)
print(my_table)
print(myTest(103,59))