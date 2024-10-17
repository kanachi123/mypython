
number = int(input("Input number: "))
sum_digits = 0
tmp = number

while number != 0:
    tmp = number % 10
    number //= 10
    sum_digits += tmp

print("\nSum of digits:", sum_digits)

number = 0
tmp_number = sum_digits
while tmp_number != 0:
    digit = tmp_number % 10
    number = number * 10 + digit
    tmp_number //= 10

print("Reversed sum:", number)

# List operations
list1 = ["hello", "students"]
list2 = ["everyone", "dear"]

print("List 1:", list1)
print("List 2:", list2)

list1 += list2
del list2

print("\nCombined List 1:", list1)
