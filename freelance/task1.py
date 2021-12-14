def cocktailSort(lst):
    n = len(lst)
    start = 0
    end = n - 1
    flag = True
    while flag == True:
        flag = False
        # as the bubble sort
        for i in range(start, end):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                flag = True
        # if nothing happened, then array is sorted.
        if flag == False:
            break
        flag = False
        end -= 1
        for i in range(end - 1, start - 1, -1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                flag = True
        start += 1


def read_numbers(file, sep=","):
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read()
    return list(map(int, data.split(sep)))


def save_list_to_txt(lst, file, sep=","):
    with open(file, 'w', encoding="utf-8") as f:
        f.write(sep.join(list(map(str, lst))))


if __name__ == '__main__':
    file = input("The read-numbers file name: ")
    res_file = input("Enter the name of the result file: ")
    separator = ","
    numbers = read_numbers(file, separator)
    numbers = list(set(numbers))
    # no need to return an array - its linked data is sorted already
    cocktailSort(numbers)
    save_list_to_txt(numbers, res_file, separator)
