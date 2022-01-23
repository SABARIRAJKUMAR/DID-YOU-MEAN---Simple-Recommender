import json
from difflib import get_close_matches
jsonfile = json.load(open("data1.json"))

word = input("enter tha word")

def check(d):
    if d in jsonfile:
        return jsonfile[d]
    elif len(get_close_matches(d, jsonfile.keys())) >0:
        choice = input("did you mean %s , enter y for YES,N for NO " % get_close_matches(d, jsonfile.keys())[0])
        if choice == "Y":
            return jsonfile[get_close_matches(d, jsonfile.keys())[0]]
        elif choice == "N":
            return "the word doesn't exist,please enter the correct word"
        else:
            return "you entered the wrong choice"
    else:
        return "the word doesn't exists"

result =(check(word))
if type(result) == list:
    for i in result:
        print(i)
    else:
        print(result)