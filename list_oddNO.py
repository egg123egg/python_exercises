def is_odd_num(l1):
    onum=[]
    for n in l1:
        if n%2!=0:
            onum.append(n)
    return onum
print(is_odd_num([1,2,3,4,5,6,7,8,9]))
