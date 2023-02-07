import math
# Am building a simple calculator with operations like add, subtract, multipy, divide 
print("Choose operation to be performed:  ")
print("1. ADD")
print("2. SUBTRACT")
print("3. DIVIDE")
print("4. MULTIPLY")
print("5. SQUARE")
print("6. SQUAREROOT")

operation = input ()
 

if  operation =="1":
    #code for add
  num1 = input ("number 1; ")
  num2 = input ("number 2;")
  print("The sum is " + str(int(num1) +  int(num2)))
elif operation =="2":
    #code for subtract
    num1 = input ("number 1; ")
    num2 = input ("number 2; ")
    print("The sunbtraction is " + str(int(num1) -  int(num2)))
elif operation =="3":
    #code for divide
    num1 = input ("number 1; ")
    num2 = input ("number 2; ")
    print("The division is " + str(int(num1) / int(num2)))
elif operation =="4":
    #code for multiply
   num1 = input ("number 1; ")
   num2 = input ("number 2; ")
   print("The multiplication  is " + str(int(num1) *  int(num2)))
elif operation =="5":
    #code for RAISE TO squre a number 
   num1 = int(input ("number 1; "))
   print("The square  is %f " % + pow (num1, 2) )
elif operation =="6":
    #code for square root
   num1 = int(input ("number 1; "))
   print("The square root  is %f " % + math.sqrt  (num1) )

else:
    print("Invalid entry")

