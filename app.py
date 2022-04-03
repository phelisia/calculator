# calculator app using addition
# multiplication
# subtraction
# division
print("select an opertaion to perform: ")
print("1.Add")
print("2.Subtract")
print("3.Multiplication")
print("4.Division")
print("5.Modulus")
operation = input()

if operation == "1":
    num1 =input("Enter first num")
    num2=input("Enter second num")
    print("sum is ", str(int(num1)+int(num2)))
elif operation == "2" :
    num1 =input("Enter first num")
    num2=input("Enter second num")
    print( "subtraction", str(int(num1)- int (num2)))
   
elif operation == "3" :
    num1 =input("Enter first num")
    num2=input("Enter second num")
    print( "multiplaction", str(int(num1)* int (num2)))
elif operation == "4" :
    num1 =input("Enter first num")
    num2=input("Enter second num")
    print("miltiplication is", str (int(num1)/(num2)))
    
elif operation == "5" :
    num1 =input("Enter first num")
    num2=input("Enter second num")
    print("the modulus is",  str (int(num1)% int (num2)))
    # code for square
else :
 print("invalid entry")
