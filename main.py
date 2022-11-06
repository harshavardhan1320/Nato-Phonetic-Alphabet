# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# square_numbers = [num * num for num in numbers]
# print(square_numbers)
# even_numbers = [num for num in numbers if num % 2 == 0]
# print(even_numbers)
#
# with open("file1.txt", mode="w")as f1:
#     f1.writelines(["3", "\n6", "\n13", "\n7", "\n89", "\n12", "\n33", "\n34", "\n1", "\n344", "\n42"])
#
# with open("file2.txt", mode="w")as f2:
#     f2.writelines(["3", "\n6", "\n5", "\n33", "\n12", "\n7", "\n4", "\n74", "\n2", "\n42", "\n13"])


file1_list = []
f1 = open("file1.txt")
for lines in f1:
    file1_list.append(lines.replace("\n", ""))
print(file1_list)

file2_list = []
f2 = open("file2.txt")
for lines in f2:
    file2_list.append(lines.replace("\n", ""))
print(file2_list)

common_num = []
for numbers in file2_list:
    new_num = [num for num in file1_list if numbers == num]
    for num in new_num:
        common_num.append(num)
print(common_num)


# another method

f1 = open("file1.txt")
f1_data = f1.readlines()

f2 = open("file2.txt")
f2_data = f2.readlines()

common_items = [int(num) for num in f1_data if num in f2_data]
print(common_items)
