"""----------------------------------------------------------------"""
"""Bubble sort ----------------------------------------------------"""
vector = [2, -3, 1, 0, 7, 4, -5, 9, 12, 6]
count = 0
def bubble_sort(count):
    find = True
    aux = 1
    while find:
        find = False
        for i in range(vector.__len__() - aux):
            if (vector[i] > vector[i+1]):
                print(vector)
                tro = vector[i]
                vector[i] = vector[i+1]
                vector[i+1] = tro
                find = True
            count+=1
        aux += 1
    return count
count = bubble_sort(count)
print(vector)
print("Numero de movimentos: ",count)
"""Bubble sort ----------------------------------------------------"""
print("\n")

"""Insert sort ----------------------------------------------------"""
vectorinsert = [2,1,3,0]
c = 0
i = 1
while i < vectorinsert.__len__():
    k = i
    while vectorinsert[k] < vectorinsert[k - 1]:
        print(vectorinsert)
        tro = vectorinsert[k]
        vectorinsert[k] = vectorinsert[k-1]
        vectorinsert[k-1] = tro
        c += 1
        if k > 1:
            k -= 1
    c += 1
    i += 1
print(vectorinsert)
print("Numero de movimentos: ",c)
"""Insert sort ----------------------------------------------------"""


