import Fibonacci
import Check

# Driver Code
print("Program to print Fibonacci series upto 'n'th term.")
input = input("Enter value for 'n' :  ")

if(Check.IsNumber(input)):
   print("Printing fibonacci series upto '" + input + "' terms.")
   Fibonacci.Print(int(input))
else:
   print("Entered value is not a valid integer. Please Retry.")
