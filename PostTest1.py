import os
os.system("cls")

def ms(list) :
    if len(list) <= 1 :
        return list
    else :
        mid = len(list) //2
        left = list[:mid]
        right = list[mid:]

        ms(left)
        ms(right)

        u = v = w = 0
        while u < len(left) and v < len(right):
            if left[u] < right [v]:
                list[w] = left[u]
                u = u + 1
            else :
                list[w] = right[v]
                v = v + 1
            w = w+1

        while u < len(left):
            list[w] = left[u]
            u = u+1
            w = w+1

        while v < len(right):
            list[w] = right[v]
            v = v+1
            w = w+1
    return list


def separate(listt):
    hasil = []
    for var in listt:
        if isinstance(var,list):
            for i in var:
                if isinstance(i, list):
                    for x in i :
                        hasil.append(int(x))
                elif isinstance(i, int) :
                    hasil.append(i)
        else :
            hasil.append(int(var))
    return hasil

var = [12, 1, [22, 3, [8, 14]], 2, 6, [11], 90]
print("Proses pengurutan variabel menggunakan Merge Sort")
print("sebelum diurutkan       = ",var)

hasil = separate(var)
print("proses pengurutan       = ",hasil)

sort = ms(hasil)
print("hasil setelah diurutkan = ",sort)