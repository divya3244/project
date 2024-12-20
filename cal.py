'''
def display_menu():
    print("\n----Calculator Menu---- ")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    return input("choose an operation (1:5): ")result = multiply(num1, num2)
        
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
     if b  == 0:
         return "Error: Division by zero is underfined."
     return a / b

while True:
     choice = display_menu()

     if choice in ["1","2","3","4"]:
         try:
             num1 = float(input("Enter the first number:"))
             num2 = float(input("Enter the second number:"))

             if choice == "1":
                 result = add(num1, num2)
                 print(f"Result: {num1}  +  {num2}  =  {result}")
             elif choice == "2":
                 result = subtract(num1, num2)
                 print(f"Result: {num1}  -  {num2}  =  {result}")
             elif choice == "3":
                 result = multiply(num1, num2)
                 print(f"Result: {num1}  *  {num2}  =  {result}")
             elif choice  == "4":
                result = divide(num1, num2)
                print(f"Result: {num1}  /  {num2}  =  {result}")
         except ValueError:
             print("Invalid input! Please enter numbers only.")
     elif choice  == "5":
         print("Exiting the Calculator,Goodbye:")
         break
     else:
         print("Invalid choice! Please select valid operation.")



'''
out put:
----Calculator Menu---- 
1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Exit
choose an operation (1:5): 1
Enter the first number:46
Enter the second number:4
Result: 46.0  +  4.0  =  50.0

----Calculator Menu---- 
1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Exit
choose an operation (1:5): 2
Enter the first number:4
Enter the second number:5
Result: 4.0  -  5.0  =  -1.0

----Calculator Menu---- 
1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Exit
choose an operation (1:5): 3
Enter the first number:5
Enter the second number:7
Result: 5.0  *  7.0  =  35.0

----Calculator Menu---- 
1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Exit
choose an operation (1:5): 4
Enter the first number:9
Enter the second number:7
Result: 9.0  /  7.0  =  1.2857142857142858

----Calculator Menu---- 
1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Exit
choose an operation (1:5): 5
Exiting the Calculator,Goodbye:

