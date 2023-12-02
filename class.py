# import string
from string import get_url


class Greeting:
    # import from the 'string' file
    def my_method(self, name):
        return (
                'Hello, ' +
                str(name) + ' this is the URL from string file: ' + get_url()
                )


greeting = Greeting()
print(greeting.my_method('Almir'))
