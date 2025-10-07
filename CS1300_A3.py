# Vincent Chu
# Fall 2025
# CS1300
# Assignment: A3

def main():
    #prompt user for POSITIVE integers
    while True:
        
        m = int(input("Enter the first number:"))
        
        n = int(input("Enter the second number:"))
        
        if m <=0 or n <=0:
            print("Ensure both numbers are positive!")
            continue
        else:
            break
    
    
    #print multiplication table for N from 1 to M and add valid factors to our list
    validFactor = []
    for num in range(1, n+1):
        print(f"{n} * {num} = {n * num}")
        
        #check if its a valid factor of n
        if n % num == 0:
            validFactor.append(num)
    
    print(f"Factors of {n} are: {validFactor}")
    
if __name__ == "__main__":
    main()