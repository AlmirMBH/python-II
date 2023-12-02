# args is a parameter that packs all (positional) arguments of a method into a tuple,
# so that the method can receive an indefinite number of arguments
def form_sentence(*args):  # *args can be anything e.g. *strings
    for i in args:
        # if changes need to be applied, cast the tuple (not changeable) into other data type
        args = list(args)
        args[2] = 'string_4'
        return args[0] + " " + args[1] + " " + args[2]


string1 = 'string_1'
string2 = 'string_2'
string3 = 'string_3'

# named parameters
volume = form_sentence(string1, string2, string3)
print(volume)