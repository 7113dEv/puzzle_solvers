'''
There is a school with 1,000 students and 1,000 lockers. On the first day of term the headteacher asks the first student to go along and open every single locker, 
he asks the second to go to every second locker and close it, the third to go to every third locker and close it if it is open or open it if it is closed, 
the fourth to go to the fourth locker and so on. The process is completed with the thousandth student. How many lockers are open at the end?
'''

# Creates 1000 lockers
locker = []
for x in range(0, 1000):
    locker.append(0)

# Creates 1000 students
student = []
for x in range(1, 1001):
    student.append(x)

# Send a student to interact with every nth locker


def sendStudent(n, locker):
    # Iterate over every Nth locker
    for i in range(n-1, len(locker), n):
        if (i + n) > len(locker):
            if locker[i] == 0:
                locker[i] = 1
            else:
                locker[i] = 0
            return locker
        else:
            if locker[i] == 0:
                locker[i] = 1
            else:
                locker[i] = 0
    return locker


# Solve Student Lockers problem
for i in student:
    sendStudent(i, locker)
print(locker)
# Count amount of open lockers
openLockers = 0
for x in locker:
    if x == 1:
        openLockers += 1

# print amount of open lockers
print(str(openLockers) + " lockers will be open")
