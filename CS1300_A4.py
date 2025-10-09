# Vincent Chu
# Fall 2025
# CS1300
# Assignment: A4

def checkNumPositive(number: int):
    '''
    Parameeter: number type int
    Summary: Checks if number is positive
    Returns: None if pos, error if neg
    '''
    if number <= 0:
        return f"***Error. You entered {number} but a positive integer is required. "
    else: 
        return None
    
def partial_sum_harmonic_series(number: int) -> float:
    '''
    Parameter: number type int
    summary: returns the partial sum of the harmonic series
    Returns: float 
    '''
    sum = 0
    for num in range(1,number + 1):
        sum += 1/num
        num +=1
    
    return round(sum,5)
    
def main():
    while True:
        #Get user input
        n = int(input("Enter a positive Integer: "))
        error = checkNumPositive(n)
        if error:
            print(error)
            continue
        
        #Print partial harmonic series
        print(f"the {n} -th partial sum of the harmonic series is {partial_sum_harmonic_series(n)}\n")
        
        #prompt to continue
        response = input("Do you wish to continue (Y/N)? ")
        if response.upper() == "Y":
            continue
        else:
            print("\nThank you for running my harmonic series program!")
            break
    
if __name__ == "__main__":
    main()