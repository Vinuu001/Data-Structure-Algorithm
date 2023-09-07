# Creating an array
arr = [1, 2, 3, 4, 5]

# Accessing elements
print("Element at index 2:", arr[2])  # Output: Element at index 2: 3

# Modifying elements
arr[3] = 8
print("Modified array:", arr)  # Output: Modified array: [1, 2, 3, 8, 5]

# Length of the array
print("Length of array:", len(arr))  # Output: Length of array: 5

# Appending elements
arr.append(6)
print("Appended array:", arr)  # Output: Appended array: [1, 2, 3, 8, 5, 6]

# Removing elements
removed_element = arr.pop(2)  # Remove element at index 2
print("Removed element:", removed_element)  # Output: Removed element: 3
print("Updated array:", arr)  # Output: Updated array: [1, 2, 8, 5, 6]

# Slicing
sub_array = arr[1:4]
print("Sub-array:", sub_array)  # Output: Sub-array: [2, 8, 5]
