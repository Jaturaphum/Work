'''
หน้าที่ 19
นายจตุรภูมิ เสือประโคน 644020373
'''
from numpy import array

array = [int(input("Enter number: ")) for i in range (10)]
print(f"Max {max(array)}\n")
print(f"Min: {min(array)}\n")
print(f"Average: {sum(array)/len(array)}")
array1 = [[(int(input("Enter array: "))) for i in range(4)] for i in range(3)]
total = 0
for i in array1: total+sum(i)
print(f"total number: {total}")