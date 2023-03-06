first_num = int(input("Enter you first number : "))
second_num = int(input("Enter you second number : "))
if first_num == second_num :
    print("your numbers are even")
else:
    num = (first_num, second_num)
    print(sorted(num))