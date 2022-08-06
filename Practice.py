numbers = ('2 1 4 3 6 5 9 8 7')
array = list(map(int, numbers.split()))

for i in range(len(array)):
    idx_min = i
    for j in range(i, len(array)):
        if array[j] < array[idx_min]:
            idx_min = j
    if i != idx_min:
        array[i], array[idx_min] = array[idx_min], array[i]

while True:
    try:
        user_number = int(input("Введите целое число от 1 до 9: "))
        if user_number in range(1, 9):
            break
        else:
            print('Число не соответствует!')
    except ValueError:
        print('Ошибка ввода!')


def binary_search(array, user_number, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == user_number:
        return middle
    elif user_number < array[middle]:
        return binary_search(array, user_number, left, middle - 1)
    else:
        return binary_search(array, user_number, middle + 1, right)

print(binary_search(array, user_number, 1, 9))
