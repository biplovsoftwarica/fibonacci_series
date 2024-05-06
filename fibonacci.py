#write a program to print the fibonacci series upto given integer

#creating a function to find fib0nacci sequence
# def fibonacci(num):
#     a = 0
#     b = 1
#     if num == 1: #just print 0 if user enter for 1st term of fibonacci series
#         print(a)
#     elif num == 2:
#         print(a)
#         print(b)
#     elif num < 0: # reminding user that they entered negative number and converting it into positive number
#         print(f"Can't enter negative number\nIt might be positive {-(num)}")
#         yes = input(f"Is it {-num}? (y/n) :")
#         if yes == "y":
#             nump = -num
#             fibonacci(nump)
#         else:
#             print("sorry try again!") #exiting the program if user doesnot accept to change negative number into positive
#             exit()

#         #finally printing the fibonacci series
#     else:
#         print(a)
#         print(b)
#         for i in range(1,num-1):
#             c = a+b
#             a = b
#             b = c
#             print(c)
    
    
    
    
def get_fibonacci_series(num):
    fibonacci_series = [0,1]
    for i in range(num-2):
        next_item = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_item)
    return fibonacci_series    
    
    
#main function to call fibonacci funtion
# def main():
#     number = int(input("Enter the number: "))
#     fab = fibonacci(number)
#     nofap = get_fibonacci_series(number)
#     print(nofap)
    
# main()