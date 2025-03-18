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

def sort_on(dict):
    return dict["number"]

def sort_dict(dict):
    #make a list of dictionaries. each with the structure {symbol: ..., number: ...}
    dict_list=[]
    for item in dict:
        temp_dict={}
        temp_dict["symbol"]=item
        temp_dict["number"]=dict[item]
        dict_list.append(temp_dict)
        
    #sprt this dictionary list according to numbers high to low
    dict_list.sort(reverse=True, key=sort_on)
    #print(dict_list)

    for i in dict_list:
        x=i["symbol"]
        y=i["number"]
        if x.isalpha()==True:
            print(x+": "+str(y))
    #new_dict={}
    #for i in dict_list:
    #    x= i["symbol"]
    #    new_dict[x]=i["number"]
    #print(new_dict)
    return 


