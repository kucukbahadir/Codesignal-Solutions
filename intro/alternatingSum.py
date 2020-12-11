def alternatingSums(a):
    list1 = [a[i] for i in range(0,len(a), 2)]
    list2 = [a[i] for i in range(1,len(a), 2)]
    return [sum(list1),sum(list2)]