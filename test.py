array = [42323234,23,4,143,23,25,25,252]


def sort_arr(arr):
    smalles_el_ind = 0
    for i in range(len(arr)):
        smallest_el = arr[i]
        smalles_el_ind = i
        for j,el in enumerate(arr[i:]):
            if el < smallest_el:
                smallest_el = el
                smalles_el_ind = j+i

        tmp = arr[i]
        arr[i] = smallest_el
        arr[smalles_el_ind] = tmp

    return arr




print(sort_arr(array))