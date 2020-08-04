'''
There is a school with 1,000 students and 1,000 lockers. On the first day of term the headteacher asks the first student to go along and open every single locker, 
he asks the second to go to every second locker and close it, the third to go to every third locker and close it if it is open or open it if it is closed, 
the fourth to go to the fourth locker and so on. The process is completed with the thousandth student. How many lockers are open at the end?
'''

# Creates 1000 lockers
lockerNumber = []
for x in range(0, 1000):
    lockerNumber.append(0)

# Creates 1000 students
student = []
for x in range(1, 1001):
    student.append(x)

# Open or Close a given locker


def interactWithLocker(num):
    if lockerNumber[num] == 0:
        lockerNumber[num] == 1
    else:
        lockerNumber[num] == 0


print(lockerNumber)
interactWithLocker(0)
print(lockerNumber)
# def locker_present(x):
