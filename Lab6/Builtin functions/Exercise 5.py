def all_elements_true(tuple_values):
    return all(tuple_values)

my_tuple1 = (True, True, True)
my_tuple2 = (True, False, True)

result1 = all_elements_true(my_tuple1)
result2 = all_elements_true(my_tuple2)

print(f"All elements in {my_tuple1} are true: {result1}")
print(f"All elements in {my_tuple2} are true: {result2}")
