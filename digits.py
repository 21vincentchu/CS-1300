# Vincent Chu
# Fall 2025
# CS1300
# Assignment #7

def printDigits(n: int) -> None:
    """
    prints each digit of the integer n in reverse order using recursion

    Args:
        n (int): digit whos digits are to be printed in reverse order
    
    Returns: 
        none
    """
    # Handle negative numbers
    if n < 0:                                                                                                                
        print('-', end='')      # Print the minus sign                                                                       
        printDigits(-n)          # Then handle the positive version                                                          
        return                                                                                                               
                                                                                                                             
    # base case - handles single digits                                                
    if n < 10:                                                                                                               
        print(n, end='')         # Just print the digit and we're done                                                       
        return                                                                                                               
                                                                                                                             
    # Recursive case - For multi-digit numbers                                                                       
    # Print the last digit first                                                                
    last_digit = n % 10                                                                                                      
    print(last_digit, end='')                                                                                                
                                                                                                                             
    # Remove the last digit and do it again                                                                      
    remaining_digits = n // 10                                                                                               
    printDigits(remaining_digits)        
