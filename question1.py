import re

def check_password_strength(password):
    # it will be checking if password length is greater than 8
    if len(password) < 8:
        return False
    
    # it will be checking for Upper and lower cases
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        return False
    
    # It will be checking for digits
    if not any(char.isdigit() for char in password):
        return False
    
    # It will be checking for Special character 
    special_characters = r"[!@#$%]"
    if not re.search(special_characters, password):
        return False
    
    # If all the criteria is met
    return True

def main():
    # Getting user input for password
    user_password = input("Enter your password: ")

    # Checking the  password strength
    is_strong_password = check_password_strength(user_password)

    # Providing the feedback to the user
    if is_strong_password:
        print("Password is strong! Good job!")
    else:
        print("Password does not meet the criteria. Please ensure it has at least 8 characters, both uppercase and lowercase letters, at least one digit, and at least one special character.")

if __name__ == "__main__":
    main()
