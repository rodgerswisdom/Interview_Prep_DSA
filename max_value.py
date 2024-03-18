def find_max(List):
    max_value = List[0]

    for item in List[1:]:
        if item > max_value:
            max_value = item
    print(max_value)
    # return max_value

    find_max([3,4,9,2,1])