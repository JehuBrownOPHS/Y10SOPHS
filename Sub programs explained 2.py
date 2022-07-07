#this subprogram is an example of a "function"
#A function contains a return state/Value

a = int(input("Enter a number >>> "))

b = int(input("Enter another number >>> "))

def adding(a, b): #parameters are used a and b 
    answer = 0
    answer = a + b
   
    return answer

adding(a, b)#call with parameters

x = adding(a, b)

print(x)

