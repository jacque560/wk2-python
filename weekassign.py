my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(2, 15)

my_list.extend([50])
my_list.extend([60])
my_list.extend([70])

my_list.pop () # remove the last item
my_list.sort() #ascending order

index_of_30 = my_list.index(30)
print("the index of 30 is:" , index_of_30)
