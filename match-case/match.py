# User String input
user_input = input("Enter the name of the month: ")

# Match statement with days of month
match user_input:
    case "january":
        print("31 days")
    case "february":
        print("28 days")
    case "march":
        print("31 days")
    case "april":
        print("30 days")
    case "may":
        print("31 days")
    case "june":
        print("30 days")
    case "july":
        print("31 days")
    case "august":
        print("31 days")
    case "september":
        print("30 days")
    case "october":
        print("31 days")
    case "november":
        print("30 days")
    case "december":
        print("31 days")
    case _:
        print("Invalid input")