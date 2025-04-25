def find_second_smallest(my_list):
    result = (sorted(my_list))
    answer = result[1]
    return answer

def find_second_smallest_v2(my_list):
    smallest = float('inf')
    second_smallest = float('inf')
    for num in my_list:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    return second_smallest


print(find_second_smallest_v2([5, 8, 3, 2, 6]))
