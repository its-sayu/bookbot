def get_num_words(string):
    liste1= string.split(sep=None)
    return liste1

def get_num_char(string):
    lower_string=string.lower()
    liste2=list(lower_string)
    num_char_dict={}

    for item in liste2:
        if not item in num_char_dict:
            
            num_char_dict[item]=1
        else:
            num_char_dict[item]+=1
    return num_char_dict

