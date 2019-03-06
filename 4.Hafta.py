matris_1 = [[1,2,3],[4,5,6]]
matris_2 = [[7,8,9],[10,11,12]]
matris_3 = [[1,2],[3,4]]
matris_4 = [[1,2,3],[4,5,6],[7,8,9]]
matris_5 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
a = int(input("Bir deger giriniz: "))

for row in matris_1:
    for column in row:
        print(column,end = " ")
    print()

def matris_toplama(m1,m2):
    result = []
    for row in range(len(m1)):
        result.append([])
        for column in range (len(m1[row])):
            #print(m1[row][column], end = " ")
            result[row].append(m1[row][column]+m2[row][column])
        #print()
    return result

def matris_cikarma(m1,m2):
    result = []
    for row in range(len(m1)):
        result.append([])
        for column in range (len(m1[row])):
            #print(m1[row][column], end = " ")
            result[row].append(m1[row][column]-m2[row][column])
        #print()
    return result

def matris_Skaler_carpim(a,m1):
    result = []
    for row in range(len(m1)):
        result.append([])
        for column in range (len(m1[row])):
            #print(m1[row][column], end = " ")
            result[row].append(m1[row][column]*a)
        #print()
    return result

def f1 (m1,i):
    return m1[i]

def f2 (m1,j):
    my_j_th_col = []
    for row in m1:
        for indis in range (len(row)):
            if (indis == j):
                my_j_th_col.append(row[indis])
    return my_j_th_col

def Vektorel_carpim(v,w):
    size = len(v)
    result = []
    for i in range(size):
        result.append(0)
    for i in range (size):
        result[i] = v[i]*w[i]
    t = 0
    for i in range (size):
        t = t + result[i]
    return t

def matris_carpimi(m1,m2):
    result = []
    for row in range (len(m1)):
        result.append([])
        for column in range (len(m2[row])):
            t = f1(m1,row)
            y = f2(m2,column)
            x = Vektorel_carpim(t,y)
            result[row].append(x)
    return result

def det_from_2_by_2(m1):
    s1 = m1[0][0]*m1[1][1]
    s2 = m1[0][1]*m1[1][0]
    s3 = s1-s2
    return s3

def delete_row_col_from_matris(m1,i,j):
    result = []
    size1 = (len(m1))
    size2 = (len(m1[0]))
    
    for a in range (size1):
        if (i == a):
            continue
        row1=[]
        for b in range (size2):
            if (j == b):
                continue
            row1.append(m1[a][b])
        result.append(row1)
    return result

def det_from_3_by_3(m1):
    a1 = m1[0][0]
    a2 = delete_row_col_from_matris(m1,0,0)
    a3 = det_from_2_by_2(a2)
    a4 = a1*a3

    b1 = m1[0][1]
    b2 = delete_row_col_from_matris(m1,0,1)
    b3 = det_from_2_by_2(b2)
    b4 = b1*b3

    c1 = m1[0][2]
    c2 = delete_row_col_from_matris(m1,0,2)
    c3 = det_from_2_by_2(c2)
    c4 = c1*c3

    return a4-b4+c4

def det_from_4_by_4(m1):
    a1 = m1[0][0]
    a2 = delete_row_col_from_matris(m1,0,0)
    a3 = det_from_3_by_3(a2)
    a4 = a1*a3

    b1 = m1[0][1]
    b2 = delete_row_col_from_matris(m1,0,1)
    b3 = det_from_3_by_3(b2)
    b4 = b1*b3

    c1 = m1[0][2]
    c2 = delete_row_col_from_matris(m1,0,2)
    c3 = det_from_3_by_3(c2)
    c4 = c1*c3

    d1 = m1[0][3]
    d2 = delete_row_col_from_matris(m1,0,3)
    d3 = det_from_3_by_3(c2)
    d4 = d1*d3

    return a4-b4+c4-d4

print(matris_toplama(matris_1,matris_2))
print(matris_cikarma(matris_1,matris_2))
print(matris_Skaler_carpim(a,matris_1))
print(matris_carpimi(matris_3,matris_4))
print(det_from_2_by_2(matris_3))
print(delete_row_col_from_matris(matris_4,0,0))
print(det_from_3_by_3(matris_4))
print(det_from_4_by_4(matris_5))