print("\nWelcome to Inventory List Analyzer!")

items = { }

categories = [ ]

while True:
    name = input("Enter item name: ")
    category = input("Enter category: ")
    quantity = int(input("Enter quantity: "))

    items[name] = quantity

    if category not in categories:
        categories.append(category)

    more = input("\nDo you want to add more items? (y/n): ")
    if more.lower() != 'y':
        break

# Summary
print("\n========== INVENTORY SUMMARY ==========")

print("\nTotal Different Items:", len(items))
print("\nTotal Quantity in Stock:", sum(items.values()))

average = sum(items.values()) / len(items)
print("\nAverage Quantity per Item:", average)

# Most and Least items
most = max(items, key=items.get)
least = min(items, key=items.get)

print("\nMost Stocked Item:", most, " - ", items[most], "units")

print("\nLeast Stocked Item:", least, " - ", items[least], "units")

# Unique categories
print("\nUnique Categories:")
for cat in sorted(categories):
    print(cat , ",")

# Items sorted by quantity
print("\nItems Sorted by Quantity:")
sorted_items = sorted(items.items(), key=lambda x: x[1], reverse=True)
for item, qty in sorted_items:
    print(item, "-", qty, "units" , ",")

print("\n========== END OF REPORT ==========")