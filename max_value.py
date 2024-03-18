def find_max(List):
    max_value = List[0]

    for item in List[1:]:
        if item > max_value:
            max_value = item
    return max_value
    
    

print(find_max([3,4,9,2,1]))