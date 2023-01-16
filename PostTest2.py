#-----------------------Search-----------------------------#
import math
def jumpSearch(arr, x, n):
    prev = 0
    step = math.sqrt(n)
    while arr[int(min(step, n) - 1)] < x:
        step += math.sqrt(n)
        if prev >= n:
            return -1
    while arr[int(prev)] < x:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[int(prev)] == x:
        return prev
    return -1

#SORT
def partition(l, bwh, atas):
    pivot = l[bwh]
    pos_batas = bwh+1
    for a in range(bwh+1,atas):
        if l[a] < pivot:
            l[pos_batas],l[a]=l[a],l[pos_batas]
            pos_batas += 1
    l[pos_batas-1],l[bwh] = l[bwh],l[pos_batas-1]
    return pos_batas
    
def quicksort(l, bwh, atas):
    if atas <= bwh:
        return
    b = partition(l, bwh, atas)
    quicksort(l, bwh, b-1)
    quicksort(l, b, atas)
    return l

def merge_sort(lst):
    if len(lst) <= 1: 
        return lst 
    tgh = len(lst) // 2 
    kiri = merge_sort(lst[:tgh])
    kanan = merge_sort(lst[tgh:])
    return integrator(kiri, kanan)

def integrator(left, right): 
    result = []
    i, j = 0, 0 

    while i < len(left) and j < len(right): 
        if left[i] < right[j]: 
            result.append(left[i]) 
            i += 1 
        else: 
            result.append(right[j]) 
            j += 1

    result += left[i:]
    result += right[j:]
    return result

#-----------------------Separation--------------------------------#
def nested_str_separator(raw_data):
    main_data = []
    nested_list = {}
    for k in range(len(raw_data)):
        if type(raw_data[k]) == str:
            main_data.append(raw_data[k])
        else:
            nested_list[k] = merge_sort(raw_data[k])
    main_data = quicksort(main_data,0,len(main_data))
    for k in nested_list:
        main_data.insert(k,nested_list[k])
    return main_data
#------------------------------------------------------------#
data = ['daiva', 'zaki', ['wahyu', 'zaki'], 'shafa', ['zaki', 'aji', 'wahyu'], 'zaki']
main_data = nested_str_separator(data)

print("Data sebelum di sort :\n",data)
print("\nData Setelah di sort :\n",main_data)

loop = True
while (loop):

    search = str(input("\nNama yang ingin dicari : "))
    print()
    for baris in reversed(range(len(main_data))):
        if type(main_data[baris]) == list:
            idx = jumpSearch(main_data[baris],search,len(main_data[baris]))
            if idx != -1:
                print(search,"berada di index ke -",baris,"kolom",idx)
        else:
            if main_data[baris] == search:
                print(search,"berada di index ke -",baris)

    choose = str(input("Apakah anda ingin mencari nama lagi? (y/t): "))
    if (choose) == "y":
        "p"
    else: 
        loop = False