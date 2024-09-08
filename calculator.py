def add(x,y):
    z = x + y
    return z

def sub(x,y):
    z = x - y
    return z

def mul(x,y):
    z = x * y
    return z

def div(x,y):
    z = x / y
    return z

def pow(x,y):
    z = x **y
    return z

print(" 1. Addition")
print(" 2. Subtraction")
print(" 3. Multiplication")
print(" 4. Division")
print(" 5. Power")
print(" 6. Exit")
print(" 7. RESET")

result = 'i'

while True:
 
    b = int(input("\nEnter a desired operation: "))

    if b == 6:
        break
    
    if result == 'i':
        input1 = int(input("Enter the no.: "))
        input2 = int(input("Enter the no.: "))
        if b == 1:
            result = add(input1, input2)
            print(result)
        elif b == 2:
            result = sub(input1, input2)
            print(result)
        elif b == 3:
            result = mul(input1, input2)
            print(result)
        elif b == 4:
            if input2 == 0:
                print("Error")
                continue
            else:
                result = div(input1, input2)
                print(result)
        elif b == 5:
            result = pow(input1,input2)
            print(result)
        elif b == 7:
            result = 'i'
            continue
            
        else:
            print("Error")
            continue
    else:

        if b == 6:
            break
        
        input3 = int(input("Enter the no.: "))
        if b == 1:
            result = add(input3,result)
            print(result)
            
        elif b == 2:
            if result>input3:
                result = sub(result,input3)
                print(result)
            else:
                result = sub(input3,result)
                print(result)
                
        elif b == 3:
            result = mul(result, input3)
            print(result)
            
        elif b == 4:
            if input3 == 0:
                print("Error")
                continue
                
            else:
                result = div(input3,result)
                print(result)
                
        elif b == 5:
            result = pow(result, input3)
            print(result)

        elif b == 7:
            result = 'i'
            continue
            
        else:
            print("Error")
            continue
        
                
    
    
          
