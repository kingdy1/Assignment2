"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    return annual_cost/SEMESTERS_PER_YEAR


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return annual_cost/MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    return cost_per_semester(annual_cost)/CLASS_DAYS_PER_SEMESTER


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    return cost_per_semester(annual_cost)/credits


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    return (cost_per_credit(annual_cost, credits)*CS1430_CREDITS)/CS1430_MEETINGS_PER_SEMESTER

def cost_per_minute(annual_cost, credits, minutes):
    return (cost_per_class(annual_cost, credits)/50)*minutes

# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    # Then ask for the credits this semester.
    annual_cost = float(input("What is the total cost of your year of college? "))
    credits = int(input("How many credits do you have this semester? "))
    while True:
        print("\nTHE COST OF COLLEGE\n" \
        "1 Per Semester\n" \
        "2 Per Month\n" \
        "3 Per Class Day\n" \
        "4 Per Credit\n" \
        "5 Per CS 1430 Class\n" \
        "6 Every Minute Being Late\n" \
        "Q Quit\n")

        choice = input("Choose an option: ")

        if choice == "Q":
            print("Buh bye")
            break

        # Add a branch for each menu option here.
        elif choice == "1":
            result = cost_per_semester(annual_cost)
            print(f"The cost per semester is ${result:.2f}")
        elif choice == "2":
            result = cost_per_month(annual_cost)
            print(f"The cost per month is ${result:.2f}")
        elif choice == "3":
            result = cost_per_day(annual_cost)
            print(f"The cost per day is ${result:.2f}")
        elif choice == "4":
            result = cost_per_credit(annual_cost, credits)
            print(f"The cost per credit is ${result:.2f}")
        elif choice == "5":
            result = cost_per_class(annual_cost, credits)
            print(f"The cost per CS 1430 class is ${result:.2f}")
        elif choice == "6":
            minutes = int(input("How many minutes late were you? "))
            result = cost_per_minute(annual_cost, credits, minutes)
            print(f"You spent ${result:.2f} being late")
        else:
            print("Wrong")
            break

# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
