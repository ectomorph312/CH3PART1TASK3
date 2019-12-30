list1 = input('Enter message: ').split(' ')
list2 = int(input('Сдвиг: '))
if list2 > 0:
    for x in range(list2):
        a = list1.pop(0)
        list1.append(a)
elif list2 < 0:
    list1.reverse()
    for j in range(abs(list2)):
        b = list1.pop(0)
        list1.append(b)
    list1.reverse()
    # for n in list1.reverse(range(list2)):
    #     b = list1.pop()
    #     list1.append(0)





result = str(list1)

print(result.replace("'",''))