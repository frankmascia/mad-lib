#Mad Lib game - 

#Trying using a dictonary
prompt1Dictonary = {
    "adjective1": ["", "adjective"],
    "noun1": ["","noun"],
    "verb1": ["", "verb past tense"],
    "adverb1": ["","adverb"],
    "adjective2": ["","adjective"],
    "noun2": ["","noun"],
    "noun3":["","noun"], 
    "adjective3":["","adjective"],
    "verb2":["","verb"],
    "adverb2":["","adverb"],
    "verb3":["","verb past tense"],
    "adjective4":["", "adjective"]
}

#For each key in prompt1Dictonary, input = promtp1dictonary[i][0]
# x = input("Enter a(n) {prompt1Dictonary[i][1]}")

for key in prompt1Dictonary:
    prompt1Dictonary[key][0] = input(f"Enter a(n) {prompt1Dictonary[key][1]} :")

prompt1 = f"""Today I went to the zoo. I saw a(n) {prompt1Dictonary['adjective1'][0]} {prompt1Dictonary['noun1'][0]} jumping up and down in its tree.
He {prompt1Dictonary['verb1'][0]} {prompt1Dictonary['adverb1'][0]} through the large tunnel that led to its {prompt1Dictonary['adjective2'][0]} {prompt1Dictonary['noun2'][0]}. 
I got some peanuts and passed them through the cage to a gigantic gray {prompt1Dictonary['noun3'][0]} towering above my head. 
Feeding that animal made me hungry. I went to get a {prompt1Dictonary['adjective3'][0]} scoop of ice cream. 
It filled my stomach. Afterwards I had to {prompt1Dictonary['verb2'][0]} {prompt1Dictonary['adverb2'][0]} to catch our bus.
When I got home I {prompt1Dictonary['verb3'][0]} my mom for a {prompt1Dictonary['adjective4'][0]} day at the zoo."""

print(prompt1)
          
  