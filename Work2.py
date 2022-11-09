'''
หน้าที่ 14
นายจตุรภูมิ เสือประโคน 6440200373
'''
list = []
for i in range(10):
    list.append(int(input("Enter number: ")))
    print(f"Max {max(list)}\n")
    print(f"Min: {min(list)}\n")
    print(f"{sum(list)/len(list)}")