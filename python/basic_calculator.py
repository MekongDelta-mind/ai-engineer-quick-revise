"""
creating a basic calucator which takes in 2 inputs from the users and print the selected operation
"""

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")


result = float(num1) + float(num2)

print(f"the reuslt of the operationg is {result}")

"""
Enter a number: 24
Enter another number: 34
the result of the operationg is 2434
If you don't convert into number then it adds only as a string.


Enter a number: 4.5
Enter another number: 45
Traceback (most recent call last):
  File "/home/prabin_nayak/Workspace/side_projects/ai-engineer-quick-revise/python/basic_calculator.py", line 8, in <module>
    result = int(num1)+int(num2)
ValueError: invalid literal for int() with base 10: '4.5'
"""
