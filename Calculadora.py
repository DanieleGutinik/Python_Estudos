#Program make a simple calculator

#This function add two numbers
def add(x,y):
    return x + y

#This function subtracts two numbers
def subtracts(x,y):
    return x - y   

#This funtion multiplies two numbres
def multiplies(x,y):
    return x * y

#This function divides two numbres
def divide (x,y):
    return x / y  

print("Selection Operation")     
print("1.add") 
print("2.subtracts")   
print("3.multiplies")
print("4.divide")

while True:
   #take input from the user 
   choice = input ("Enter choice(1/2/3/4): ")

   #check if choice is one of the options 
   if choice in ('1','2','3','4'):
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))

      if choice == '1':
         print(num1, "+", num2, "=", add(num1,num2))

      elif choice == '2':
           print(num1, "-", num2, "=", subracts(num1,num2))

      elif choice == '3':
           print(num1, '*', num2, "=", multiplies(num1,num2))

      elif choice == '4':
           print(num1, '/', num2, "=", divide(num1,num2))   
      break
else:
  print("invalid Input")
  
      