# Vincent Chu
# Fall 2025
# CS1300
# Assignment A5

def composite(number : int) -> bool:
    if number <= 1:
        return False
    
    for num in range(2, number-1):
        if number % num == 0:
             return True

    return False


def positiveNum(number : int) -> bool:
    '''
    Parameeter: number type int
    Summary: Checks if number is positive
    Returns: None if pos, error if neg
    '''
    if number <= 0:
        return f"***Error. You entered {number} but a positive integer is required. "
    else: 
        return None

def main():
    #Get user input
    n = int(input("Enter a positive Integer: "))
    error = positiveNum(n)
    
    if error:
        print(error)
        exit()

    primes = []
    for num in range(2, n+1):
        boolComp = composite(num)
        
        if boolComp == False:
            primes.append(num)
    
    print(f"all the prime numbers between 2 and {n} are {primes}")

if __name__ == "__main__":
    main()