import re

print("Please input a passcode which contains atleast a capital letter, a number, a special character [!@#_$%^&*+-/\><], and greater than 15 characters")


def PassValidate():
    passcode = input("Please put a strong password: ")
    valid = True
    for valid in passcode:
        if (len(passcode) < 15):
            print("Invalid passcode")
            break
        elif not re.search('[A-Z]', passcode):
            print("Invalid passcode")
            break 
        elif not re.search('[0-9]', passcode):
            print("Invalid passcode")
            break
        elif not re.search('[!@#_$%^&*+-/]', passcode):
            print("Invalid pascode")
            break
        else:
            print("Passcode inputted is valid")
            break

PassValidate()