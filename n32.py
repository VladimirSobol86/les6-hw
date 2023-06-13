list_1 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
min_number = int(input("Min: "))
max_number = int(input("Max: "))
for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        print(i)