"""Luke Sexton"""


def main():

    valid_password = password_checker()
    while valid_password is False:
        print("Invalid.")
        valid_password = password_checker()

    for star in range(valid_password):
        print('*', end=' ')


def password_checker():

    length_min = 5

    user_password = input("Please enter a password with 6 or more characters: ")
    if len(user_password) <= length_min:
        return False
    else:
        count_character = 0

        for char in user_password:
            if char.isalpha():
                count_character += 1

        return count_character


main()
