def sort(items):
    n = len(items)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if items[j] < items[min_index]:
                min_index = j
        if i != min_index:
            items[i], items[min_index] = items[min_index], items[i]
    return items

items = [4, 5, 2, 3, 1]
print(sort(items))