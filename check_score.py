from fuzzywuzzy import fuzz
import sys
import pandas as pd

def check_similarity_score(string1,string2):
    string1=string1.lower()
    string2=string2.lower()

    similarity_score=fuzz.ratio(string1,string2)

    print(f"similarity score for {string1} and {string2} is \n"
          f"{similarity_score}")
    
string1="Abbey Digital"
string2="Abbey Digital Limited"

check_similarity_score(string1,string2)