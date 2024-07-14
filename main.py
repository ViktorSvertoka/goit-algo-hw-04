import timeit
import random


# Реалізація сортування злиттям
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


# Реалізація сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Порівняння алгоритмів
def compare_sorts():
    setup_code = "from __main__ import merge_sort, insertion_sort; import random"
    num_elements = [10, 100, 1000, 10000]

    for n in num_elements:
        test_data = [random.randint(0, 10000) for _ in range(n)]
        test_code_merge = f"merge_sort({test_data})"
        test_code_insertion = f"insertion_sort({test_data})"
        test_code_sorted = f"sorted({test_data})"
        test_code_sort = f"{test_data}.sort()"

        print(f"Number of elements: {n}")
        print(
            "Merge Sort: ",
            timeit.timeit(stmt=test_code_merge, setup=setup_code, number=10),
        )
        print(
            "Insertion Sort: ",
            timeit.timeit(stmt=test_code_insertion, setup=setup_code, number=10),
        )
        print(
            "Timsort (sorted): ",
            timeit.timeit(stmt=test_code_sorted, setup=setup_code, number=10),
        )
        print(
            "Timsort (sort): ",
            timeit.timeit(stmt=test_code_sort, setup=setup_code, number=10),
        )
        print()


# Запуск порівняння
compare_sorts()

# Результат виконання коду

"""
Number of elements: 10
Merge Sort:  4.8290996346622705e-05
Insertion Sort:  1.7916958313435316e-05
Timsort (sorted):  3.4999684430658817e-06
Timsort (sort):  2.4999608285725117e-06

Number of elements: 100
Merge Sort:  0.000669291999656707
Insertion Sort:  0.0008775420137681067
Timsort (sorted):  3.6375015042722225e-05
Timsort (sort):  2.787495031952858e-05

Number of elements: 1000
Merge Sort:  0.009126457967795432
Insertion Sort:  0.11143320897826925
Timsort (sorted):  0.0005297079915180802
Timsort (sort):  0.00043175002792850137

Number of elements: 10000
Merge Sort:  0.11520141700748354
Insertion Sort:  11.680987500003539
Timsort (sorted):  0.008780165982898325
Timsort (sort):  0.00895641598617658
"""

# Висновки

"""
Timsort (sorted і sort):

Timsort показав найкращі результати на всіх наборах даних. Це підтверджує його ефективність завдяки гібридній природі,
яка поєднує сортування злиттям та сортування вставками.
Використання вбудованих функцій sorted і sort є найбільш доцільним для більшості завдань сортування в Python.

Merge Sort:

Merge Sort є ефективним для середніх і великих наборів даних, але поступається Timsort.
Цей алгоритм має стабільну продуктивність, але його час виконання збільшується зі збільшенням розміру даних.

Insertion Sort:

Insertion Sort працює добре на малих наборах даних, але його ефективність різко падає з збільшенням розміру даних.
Через квадратичну складність, цей алгоритм не підходить для великих наборів даних.
"""
