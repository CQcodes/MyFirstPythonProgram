# prints fibonacci series       
def Print(number_of_terms):
   counter = 1

   first = 0
   second = 1
   temp = 0
 
   while counter <= number_of_terms:
      print(first)
      temp = first + second
      first = second
      second = temp
      counter = counter + 1

   return first
