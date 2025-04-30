a=eval(input("Enter limit"))
lst=[]
for a in range(1,a+1):
    a=eval(input("enter element"))
    lst.append(a)
print(lst)
l=len(lst)
for i in range(l):
    for j in range(0,1-i-1):
        if lst[j]>lst[j+1]:
            temp=lst[j]
            lst[j]=lst[j+1]
            lst[j+1]=temp
print("after sorting the list is")
print(lst)