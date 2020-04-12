def total_sum(list):
    total_sum=0
    for item in list:
        total_sum+=item 
    return total_sum

def max_min(list):
    min_value=list[0]
    max_value=list[0]
    for item in list:
        if item > min_value:
            min_value=item
        if item < max_value:
            max_value=item
    return min_value, max_value

num_list = [10,34,23,56,19,16,18,19,34]
min_value, max_value = max_min(num_list)
 
print(f"Sum = {total_sum(num_list)}")
print("Averrage = {:5.4}".format(total_sum(num_list)/len(num_list)))
print(f"Min value = {min_value}")
print(f"Max value = {max_value}")