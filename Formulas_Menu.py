def Basic_Arithmetic():
    print("\n\t\t\t----Basic Arithmetic Formulas----\n")
    print("A. Addition :-        [a + b]")
    print("B. Substraction :-    [a - b]")
    print("C. Multiplication :-  [a * b]")
    print("D. Division :-        [a / b]")
    print("E. Modulus :-         [a % b]")
    print("F. Power :-           [a ** b]")

def Number_Based():
    print("\n\t\t\t----Number-Based Formulas----\n")
    print("A. Even Number:-     [n % 2 == 0]")
    print("B. Odd Number:-      [n % 2 != 0]")
    print("C. Sum of N numbers:- [n(n+1)/2]")


def Financial_Calculations():
    print("\n\t\t\t----Financial Calculations Formulas----\n")
    print("A. Find Average:-         (a+b+c)/n")
    print("B. Find Percentage:-      (Value/Total)*100")
    print("C. Find Simple Interest:- (P * R * T) / 100")
    print("D. Find Discount Amount:-    (price * discount_percent) / 100")

def Profit_Loss():
    print("\n\t\t\t---- Profit & Loss Formulas ----\n")
    print("A. Profit:-          SP - CP")
    print("B. Loss:-            CP - SP")
    print("C. Profit %:-        (Profit / CP) * 100")
    print("D. Loss %:-          (Loss / CP) * 100")


def Area():
    print("\n\t\t\t---- Area Based Formulas ----\n")
    print("A. Rectangle:-       (length * width)")
    print("B. Square:-          (side * side)")
    print("C. Triangle:-        (base * height) / 2")
    print("D. Circle:-          (3.14 * r * r)")

def Volume():
    print("\n\t\t\t---- Volume Based Formulas ----\n")
    print("A. Cube:-            (side ** 3)")
    print("B. Cuboid:-          (length * width * height)")
    print("C. Cylinder:-        (3.14 * r * r * height)")
    print("D. Sphere:-          (4/3) * 3.14 * r ** 3")

def Time_Speed():
    print("\n\t\t\t---- Time & Speed Formulas ----\n")
    print("A. Speed:-           distance / time")
    print("B. Distance:-        speed * time")
    print("C. Time:-            distance / speed")

def Temperature():
    print("\n\t\t\t---- Temperature Formulas ----\n")
    print("A. Celsius to Fahrenheit:- (C * 9/5) + 32")
    print("B. Fahrenheit to Celsius:- (F - 32) * 5/9")

def Weight():
    print("\n\t\t\t---- Weight Formulas ----\n")
    print("A. Kg to Gram:-      kg * 1000")
    print("B. Gram to Kg:-      g / 1000")
    print("C. Kg to Pound:-     kg * 2.20462")
    print("D. Pound to Kg:-     lb / 2.20462")

def Geometry():
    print("\n\t\t\t---- Geometry (Perimeter) ----\n")
    print("A. Perimeter Rectangle:- 2*(l + w)")
    print("B. Perimeter Square:-    4 * side")
    print("C. Circumference:-       2 * 3.14 * r")


def Main_Menu():
    while True:
        print("\n\t\t\t===== FORMULA MENU =====\n")
        print("1. Basic Arithmetic")
        print("2. Number Based")
        print("3. Financial Calculations")
        print("4. Profit_Loss")
        print("5. Area")
        print("6. Volume")
        print("7. Time and Speed")
        print("8. Temperature")
        print("9. Weight")
        print("10. Geometry")
        print("11. Exit")

        User_Choice = (input("\nEnter Your Choice: "))

        if User_Choice == '1':
            Basic_Arithmetic()
        
        elif User_Choice == '2':
            Number_Based()
        
        elif User_Choice == '3':
            Financial_Calculations()
        
        elif User_Choice == '4':
            Profit_Loss()
        
        elif User_Choice == '5':
            Area()
        
        elif User_Choice == '6':
            Volume()
        
        elif User_Choice == '7':
            Time_Speed()
        
        elif User_Choice == '8':
            Temperature()
        
        elif User_Choice == '9':
            Weight()
        
        elif User_Choice == '10':
            Geometry()
        
        elif User_Choice == '11':
            print("Exiting Program......")
            print("Thank You For Using")
            break
        
        else:
            print(f"{User_Choice}This Is A Invaild Choice! Try Again")


Main_Menu()