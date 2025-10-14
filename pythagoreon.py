# Vincent Chu
# Fall 2025
# CS1300
# Assignment A6

def arithmeticMean(*numbers):
    """
        Calculates the average / arithmetic mean
    
    Args:
        numbers (tuple): any length and any type 

    Returns:
        _type_: float
    """
    n = 0
    sum = 0
    
    #iterate through tuple
    for num in numbers:
        n +=1
        sum += num
        
    return (sum / n)

def geometricMean(*numbers):
    """
        Calculates the geometric mean
    Args:
        numbers (tuple): any length and any type
    Returns:
        _type_: float
    """
    n = 0
    product = 1

    #iterate through tuple
    for num in numbers:
        n +=1
        product *= num

    return abs(product) ** (1/n)
    

def harmonicMean(*numbers):
    """
    Summary:
        Calculates the harmonic mean
    Args:
        numbers (tuple): any length and any type
    Returns:
        _type_: float
    """
    n = 0
    sum = 0

    #iterate through tuple
    for num in numbers:
        n +=1
        sum += (1/num)

    return (n / sum)
    