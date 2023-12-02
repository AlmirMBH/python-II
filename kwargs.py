# kwargs is a parameter that packs all (key word) arguments of a method into a dictionary,
# so that the method can receive a varying number of arguments
def form_sentence(**kwargs):  # *args can be anything e.g. *strings
    for i in kwargs:
        # return args[0] + " " + args[1] + " " + args[2]
        # return kwargs['string_1'] + " " + kwargs['string_2'] + " " + kwargs['string_3']
        return kwargs.items()


string1 = 'string_1'
string2 = 'string_2'
string3 = 'string_3'

# named parameters
volume = form_sentence(string_1=string1, string_2=string2, string_3=string3)
print(volume)
