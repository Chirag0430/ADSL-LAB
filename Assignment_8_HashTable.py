
list=[]
j=1
y=int(input("Enter the array size: "))

for i in range(y):
    list.append(0)
print("Initial array is: ",list)

for k in range(y):
    x=int(input("Enter the value: "))
    h=x%y

    if list[h]==0:
        list[h]=x
        print(list)

    else:
        while(list[h]!=0):
            h=(h+j)%y
        list[h]=x
print(list)
