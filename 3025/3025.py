"""chanceseason"""
month = input()
day = int(input())
undivide = ["1", "2", "4", "5", "7", "8", "10", "11"]
divide = ["3", "6", "9", "12"]
winter = ["1", "2", "3"]
spring = ["4", "5", "6"]
summer = ["7", "8", "9"]
fall = ["10", "11", "12"]
if month in divide and day >= 21:
    if month == "3":
        print("spring")
    elif month == "6":
        print("summer")
    elif month == "9":
        print("fall")
    elif month == "12":
        print("winter")
elif month in undivide and day <= 31:
    if month in winter:
        print("winter")
    elif month in spring:
        print("spring")
    elif month in summer:
        print("summer")
    elif month in fall:
        print("fall")
elif month in divide and day < 21:
    if month in winter:
        print("winter")
    elif month in spring:
        print("spring")
    elif month in summer:
        print("summer")
    elif month in fall:
        print("fall")
