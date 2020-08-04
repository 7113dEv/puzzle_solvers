'''
A number's persistence is the number of steps required to reduce it to a single digit by multiplying all its digits to obtain a second number, 
then multiplying all the digits of that number to obtain a third number, and so on until a one-digit number is obtained. 
For example, 77 has a persistence of four because it requires four steps to reduce it to one digit: 77-49-36-18-8. 
The smallest number of persistence one is 10, the smallest of persistence two is 25, the smallest of persistence three is 39, and the smaller of persistence four is 77. 
What is the smallest number of persistence five?
'''


def multiplyDigits(number):  # multiplyDigits(121)
    # Splits each digit in a given number individually into an array
    digits = [int(d) for d in str(number)]  # digits = [1, 2, 1]
    currentProduct = digits[0]  # currentProduct = 1
    # Multiply the digits together
    for i in range(1, len(digits)):
        currentProduct = currentProduct * digits[i]

    return currentProduct


def findPersistence(number):
    productList = []
    # Multiply each digit in the number EX: 77 ---> 7*7
    product = multiplyDigits(number)
    print("Current Number: " + str(product))
    productList.append(product)

    while len(str(product)) != 1:
        product = multiplyDigits(product)
        print("Current Number: " + str(product))
        productList.append(product)

    persistence = len(productList)
    print("Done")
    print("Persistence length: " + str(persistence)+"\n")
    return persistence


def solve(startNum, endNum):
    for x in range(startNum, endNum+1):
        print("Peristence for number: " + str(x))
        fivePersistenceNumbers = []
        if findPersistence(x) == 5:
            fivePersistenceNumbers.append(x)
    print("Numbers with a persistence of five: " + str(fivePersistenceNumbers))


def has_givenPersistence(x, num):
    return findPersistence(num) == x


def findSmallestFivePersistenceNum(x):
    num = 1
    while has_givenPersistence(x, num) == False:
        print("\nPeristence for number: " + str(num))
        num += 1
        has_givenPersistence(x, num)

    print(str(num) + " is the lowest number with " + str(x) + " persistence")


#solve(1000, 9999)
findSmallestFivePersistenceNum(6)
