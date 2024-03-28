shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
print(shopping_list)
item_to_find = input("Enter the item to find: ")
found_at = None

# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find.casefold():
#         found_at = index
#         break
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print(f"Item found at position {found_at}")
else:
    print(f"{item_to_find} not Found!")
