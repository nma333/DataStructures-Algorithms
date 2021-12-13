my_list=[]

length=int(input("Length:"))
for i in range(0,length):
    ele=int(input("elements:"))
    my_list.append(ele)

print("Array before sorting:")
print(my_list)
for i in range(0,length-1):
    for j in range(0,length-1):
        if my_list[j]>my_list[j+1]:
            temp=my_list[j]
            my_list[j]=my_list[j+1]
            my_list[j+1]=temp
           # my_list[j],my_list[j+1]=my_list[j+1],my_list[j]
            swaped=True

print("Array after sorting:")
print(my_list)


OUTPUT:
          Length:4
          elements:9
          elements:1
          elements:6
          elements:2
          Array before sorting:
          [9, 1, 6, 2]
          Array after sorting:
          [1, 2, 6, 9]
