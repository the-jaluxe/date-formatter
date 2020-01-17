# Question:    Python Project to determine the number of ambiguous days
#              between L and M peoples?
# Author:      Jarrett Cornelison
# Date:        December 26, 2018
# Purpose:     To solve the problem asked in the above question

from datetime import date
from datetime import time
from datetime import datetime

days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

endianessB = ["Bhutan", "China", "Koreas", "Canada", "Taiwan", "Hungary", "Iran", "Japan", "Lithuania", "Mongolia"]
endianessL = ["Asia", "Australia", "New Zealand", "Latin America", "North Africa", "India", "Indonesia", "Bangladesh", "Russia"]
endianessM = ["United States", "Philippines", "Marshall Islands"]
#endianessLM = ["Malaysia", "Nigeria", "Saudi Arabia", "Somalia"]
#endianessLB = ["Afghanistan", "Albania", "Austria", "Germany", "Kenya", "Macau", "Maldives", "Montenegro", "Namibia", "Nepal", "Singapore", "South Africa", "Sri Lanka", "Sweden", "Poland"]

def endianessBComparsion(arg1):
    
    # Compares B endianess countries with L and M endianess countries
    i = 0
    x = 0
    amountOfAmbiguousDays = 0
    userCountry = str(arg1)
    now = datetime.now()

    #Counts ambiguous days by comparing the days arrays to months arrays
    while i < len(months):
        j = 0
        for x in months:
            if days[i] == months[j]:
                j += 1
            else:
                amountOfAmbiguousDays += 1
                j += 1
        i += 1

    #Prints amount of amibiguous days with respective countries
    print("\n" + str(userCountry) + " has 0 ambiguous days with:\n")

    for x in endianessL:
        print(x)

    for x in endianessM:
        print(x)

    #Prints current date based on the enduanness of the country
    print("\nThe current date in " + str(userCountry) + " is: ")
    print(now.strftime("%Y-%m-%d\n "))

def endianessLComparsion(arg1):
    
    # Compares L endianess countries with B and M endianess countries
    i = 0
    x = 0
    userCountry = str(arg1)
    amountOfAmbiguousDays = 0
    now = datetime.now()

    #Counts ambiguous days by comparing the days arrays to months arrays
    while i < len(months):
        j = 0
        for x in months:
            if days[i] == months[j]:
                j += 1
            else:
                amountOfAmbiguousDays += 1
                j += 1
        i += 1

    #Prints amount of amibiguous days with respective countries
    print("\n" + str(userCountry) + " has " + str(amountOfAmbiguousDays) + " ambiguous days with:\n")

    for x in endianessM:
        print(x)

    print("\n" + str(userCountry) + " has 0 ambiguous days with:\n")

    for x in endianessB:
        print(x)

    #Prints current date based on the enduanness of the country
    print("\nThe current date in " + str(userCountry) + " is: ")
    print(now.strftime("%d-%m-%Y\n"))

def endianessMComparsion(arg1):

    # Compares M endianess countries with L and B endianess countries
    i = 0
    x = 0
    userCountry = str(arg1)
    amountOfAmbiguousDays = 0
    now = datetime.now()

    #Counts ambiguous days by comparing the days arrays to months arrays
    while i < len(months):
        j = 0
        for x in months:
            if days[i] == months[j]:
                j += 1
            else:
                amountOfAmbiguousDays += 1
                j += 1
        i += 1

    #Prints amount of amibiguous days with respective countries
    print("\n" + str(userCountry) + " has " + str(amountOfAmbiguousDays) + " ambiguous days with:\n")

    for x in endianessL:
        print(x)

    print("\n" + str(userCountry) + " has 0 ambiguous days with:\n")

    for x in endianessB:
        print(x)

    #Prints current date based on the enduanness of the country
    print("\nThe current date in " + str(userCountry) + " is: ")
    print(now.strftime("%m-%d-%Y\n"))

def main():

    # Variable list
    userInput = False

    # Get input from user with error catching
    while userInput == False:
        userCountry = input("What country do you live in? (Enter ? for supported countries) ")

        if userCountry == "":
            print("\nError: No country was entered\n")
            continue

        if userCountry.find(" ") > 0 and not userCountry.endswith(" "):
            userCountry = userCountry.split()
            userCountry = userCountry[0].capitalize() + " " + userCountry[1].capitalize()
        else:
            userCountry = userCountry.capitalize()

        if userCountry in endianessB:
            userInput = True
            break

        if userCountry in endianessL:
            userInput = True
            break

        if userCountry in endianessM:
            userInput = True
            break

        if userCountry == "?":
            print("\nList of supported countries: \nBhutan, China, Koreas, Canada, Taiwan, Hungary, \nIran, Japan, Lithuania, Mongolia, Asia, Australia,\nNew Zealand, Latin America, North Africa, India, Indonesia,\nBangladesh, Russia, United States, Philippines,\nFederated States of Micronesia, Marshall Islands\n")
        else:
            print("\nError: That country is invalid. Please check for spelling mistakes\n")
    
    # Call correct function based on user's selected country
    if userCountry in endianessB:
        endianessBComparsion(userCountry)

    if userCountry in endianessL:
        endianessLComparsion(userCountry)

    if userCountry in endianessM:
        endianessMComparsion(userCountry)


if __name__ == "__main__":
  main();