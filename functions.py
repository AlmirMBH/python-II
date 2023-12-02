def form_sentence(string1, string2, string3='default string'):
    return string1 + " " + string2 + " " + string3


string1 = 'string_1'
string2 = 'string_2'
string3 = 'string_3'

# named parameters
volume = form_sentence(string1=string1, string3=string3, string2=string2)
print(volume)

volume_2 = form_sentence(string1=string1, string2=string2)
print(volume_2)