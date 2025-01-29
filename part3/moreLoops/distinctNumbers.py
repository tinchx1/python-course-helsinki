def distinct_numbers(numbers):
  distinct = list(set(numbers))
  distinct.sort()
  return distinct

my_list = [3, 2, 2, 1, 3, 3, 1]
print(distinct_numbers(my_list)) 