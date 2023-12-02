# Strings

def manipulate_string():
    string = 'This is a string that we will process with various built-in functions'
    # [start:stop:step]
    # [4:22:3]
    # start at character at index 4, stop at character at index 22,
    # print every third character, including the first at index 4
    print(string[:17])
    print(string[19:])
    print(string[::3])

    # reverse the string
    print(string[::-1])

    # slice string
    url = 'http://www.google.com/images'
    url_slice = slice(11, -11)
    print(url[url_slice])

    animal_1 = 'cow'
    animal_2 = 'tiger'
    item = 'moon'

    # String formatting
    text_1 = "The {:5} jumped over the {}"  # :5 - 5 empty spaces
    text_2 = "The {0:5} jumped over the {2}"
    text_3 = "The {animal1:5} jumped over the {animal2}"
    number_1 = 3.14159
    number_2 = 1000

    print(text_1.format(animal_1, item))  # order
    print(text_2.format(animal_1, item, animal_2))  # index
    print(text_3.format(animal1=animal_1, item=item, animal2=animal_2))  # key-value
    print("The number PI is {:.2f}".format(number_1))
    print("The binary number is {:b}".format(number_2))
    print("The octa number is {:o}".format(number_2))
    print("The hexa number is {:x}".format(number_2))  # or capital X
    print("The scientific notation number is {:e}".format(number_2))  # or capital E


def get_url():
    return 'http://www.google.com/images'


# This block will only be executed if the file is run directly, not when imported as a module
if __name__ == "__main__":
    manipulate_string()
