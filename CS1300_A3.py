# Vincent Chu
# FALL 2025
# CS1300
# Assignment: A3
def checkNumPositive(number: int):
    if number <= 0:
        return "Please enter a positive integer"
    else: 
        return None

def print_Matrix_and_factors(m : int, n : int):
    factors = []
    
    for num in range(1, m+1):
        print(f"{n} * {num} = {n*num}")
        
    for num in range(1, n+1):
        if n % num == 0:
            factors.append(num)
            
    print(f"factors of {n} are {factors}")

    
def main():
    #read in two integers, must be positive, if not, loop continues.
    while True:
        m = int(input("Enter a positive integer: "))
        error = checkNumPositive(m)
        if error:
            print(error)
            continue
        
        n = int(input("Enter a positive integer: "))
        error = checkNumPositive(n)
        if error:
            print(error)
            continue
        
        break
    
    print_Matrix_and_factors(m, n)

if __name__ == "__main__":
    main()