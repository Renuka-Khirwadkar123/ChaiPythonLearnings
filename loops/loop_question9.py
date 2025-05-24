items=['Apple','Banana','Banana','Orange','Mango','Apple']
unique_item=set()

for item in items:
    if item in unique_item:
        print(f"Duplicate found: {item}")
        break
    else:
        unique_item.add(item)


