list = [50, "Bharathi", 3.14, True, "Dibbidi"]
print("Initial list:", list)

list.append("Varma")
list.append(42)
print("After appending two items in the list : ", list)

removed = list.pop()  
print("Removed item:", removed)
print("After removed one item in the list : ", list)

list.reverse()
print("Reversed list : ", list)

sort_list = []
for item in list:
    if isinstance(item, str):
        sort_list.append(item)

sort_list.sort()
print("Sorted list of strings: ", sort_list)

print("\n Final original list is :", list)
