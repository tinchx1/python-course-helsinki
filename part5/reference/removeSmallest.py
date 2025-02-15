def remove_smallest(numbers: list):
  smallest = min(numbers)
  list_without_min = numbers.remove(smallest)
  numbers = list_without_min

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)
