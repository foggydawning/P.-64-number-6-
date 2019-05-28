def sort (list, li=[], i=0):
    k=len(list)//2
    while i!= k:
        li.append(list.pop(0))
        i+=1

    list.sort(reverse=True)
    li.sort(reverse=False)
    while len(li)!=0:
        list.insert(0, li.pop())
    return list

list=[]

print("Ваш отсортированный список:", sort(list), sep="\n")
