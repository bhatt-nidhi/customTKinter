# num=int(input("enter any number : "))
# for i in range(num):
#     if(num%2==0):
#         print(f"the number {num} is even:")
#         break
#     else:
#         print("the number is odd")
#         break


while True:
    try:
        num = int(input("Enter any number: "))  # Try to convert input to an integer
        break  # Exit the loop if conversion is successful
    except ValueError:
        print("Please enter a valid number.")  # Display this message if a ValueError occurs

# Now proceed with the rest of the program logic
for i in range(num):
    if num % 2 == 0:
        print(f"The number {num} is even.")
        break
    else:
        print(f"The number {num} is odd.")
        break
