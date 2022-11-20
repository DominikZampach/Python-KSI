def lists(a, b, c, d):
    x=0
    li1 = []
    while x <= a:
        li1.append(x)
        x += 1
    li2 = []
    x = 0
    while x <= len(li1)-1:
        li2.append(li1[x] + 10)
        x += 1
    li2[len(li2) - 1] = "KSI"
    if b in li2:
        li2.remove(b)
    else:
        print("Not here")
    li3 = []
    x = 0
    while x < c:
        li3.append(li1[x])
        x += 1
    li2.extend(li3)
    li1[1] = d
    li1.sort()
    li3.reverse()
    return (li1, li2, li3)
    pass

print(lists(5, 12, 3, 20))
    # ([0, 2, 3, 4, 5, 20], [10, 11, 13, 14, 'KSI', 0, 1, 2], [2, 1, 0])
print(lists(10, 3, 2, 11))
    # Not here
    # ([0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 'KSI', 0, 1], [1, 0])
