# Vincent Chu
# Fall 2025
# CS1300
# Assignment: A2

#Gets the ticket price correlating to their age
def getTicketPrice(age : int) -> int:
    match age:
        case child_age if age < 12:
            return 8
        case teen_age if 12 <= age < 18:
            return 10
        case adult if 18 <= age < 60 :
            return 15
        case senior if age >= 60:
            return 12
        
#Verify persons age
def verifyAge(age : int) -> None:
    if int(age) <= 0:
        print("Error: Age can not be less than 1")
        exit()

#Verify loyalty status
def verifyLoyalty(answer : str) -> bool:
    if answer.lower() == "yes":
        return True
    else: 
        return False

def main():
    #Grab user's age
    age : int = input("What is your age?: ")

    #Verify the age
    verifyAge(int(age))

    #Grab user's loyalty status
    loyaltyStr : str = input("Are you part of our loyalty program? (Yes/No): ")

    #verify loyalty
    loyaltyBool = verifyLoyalty(loyaltyStr)

    #get price tice
    ticketPrice : int = getTicketPrice(int(age))    

    #print
    if loyaltyBool:
        print(f"Your ticket price is ${ticketPrice - 2}")
    else: 
        print(f"Your ticket price is ${ticketPrice}")

if __name__ == "__main__":
    main()
