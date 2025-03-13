def insert_at_index(lst, index, item):
    lst.insert(index, item)

def append_items(lst, items):
    lst.extend(items)

def append_list(lst1, lst2):
    lst1.extend(lst2)

my_list = [1, 2, 3]
insert_at_index(my_list, 1, 100)
print(my_list)

append_items(my_list, [200, 300])
print(my_list)

another_list = [400, 500]
append_list(my_list, another_list)
print(my_list)
