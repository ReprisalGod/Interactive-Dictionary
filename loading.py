import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
d=json.load(open("data.json","r"))
m=0
def dic(w):
  global m
  if w in d:
     return d[w]
  
  else:
    if(len(get_close_matches(w,d.keys()))>m):
      k=input("Did you mean %s if yes input 1 else 0 : \n" % get_close_matches(w,d.keys())[m])
      if(int(k)==1):
         return d[get_close_matches(w,d.keys())[m]]
      else:
         m=m+1
         return dic(w)
    else:
      return "The word might be incorrect"


word=input("Enter a word \n")
output=dic(word.lower())
if(type(output)==list):
    for i in output:
     print(i)
else:
  print(output)  