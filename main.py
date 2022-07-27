# def factorial(number):
#     i = 1
#     while number > 0:
#         i = i*number
#         number = number - 1
#     return i

# def palindrome(value):
#     i = 0
#     length = len(value)
#     inpu = list(value)
#     output = []
#     while length > 0:
#         i = i - 1
#         length = length - 1
#         output.append(value[i])
#     return output == inpu

# def fibonacci(converted_number):
#     x = [0,1,]     
#     output = []
#     if converted_number == 1:
#         return [0]
#     elif converted_number == 2:
#         return [0,1]    
#     else:
#         while converted_number > 2:
#             output = x[-1] + x[-2]
#             x.append(output)
#             converted_number = converted_number - 1
#         return x
     
def main():
    try:
        selectionmode, input_type = getuserinput("main")
        if selectionmode == 1:
            number,input_type = getuserinput("positive_integer")
            calculated_value = factorial(number)
            print(f"Factorial of {number} is {calculated_value}")
        elif selectionmode == 2:
            number,input_type = getuserinput("positive_integer")
            calculated_value = fibonacci(number)
            print(f"fibonacci series of {number} is {calculated_value}")
        elif selectionmode == 3:
            str_value,input_type = getuserinput("string")
            is_palindrome = palindrome(str_value)
            if is_palindrome:
                print(f"{str_value} is a palindrome")
            else:
                print(f"{str_value} is not a palindrome")  
    finally:
        print("--*--"*12)

# def getuserinput(input_type:str):
#     if input_type == "main":
#         reqd = input("choose mode 1 = factorial,2 = fibonacci , 3 = palindrome check ")
#         con_reqd = int(reqd)
#         if con_reqd not in [1,2,3]:
#             raise ValueError("Please enter either 1 or 2 or 3")
#     elif input_type == "positive_integer":
#         reqd = input("Please enter positive integer ")
#         con_reqd = int(reqd)
#         if con_reqd < 0:
#             raise ValueError("Please enter positive integer")           
#     elif input_type == "string":
#         con_reqd = input("Please enter a string ") 
#     else:
#         raise RuntimeError("Please enter valid input type one of -[main, positive_integer, string]")  
#     return con_reqd, input_type


if __name__ == "__main__":
    main()

        
            