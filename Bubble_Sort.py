def sort(items):
    for i in range(len(items)):
        for j in range(i):
            if items[i] > items[j]:
                items[i], items[j] = items[j], items[i]
    return items

items = [1, 5, 3, 2, 4]
print(sort(items))