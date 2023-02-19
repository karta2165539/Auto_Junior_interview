anniversary="Hello welcome to Cathay 60th year anniversary"

counter = dict()
for letter in anniversary.replace(" ","").upper():
    if letter not in counter :
        counter[letter]= 1
    else:
        counter[letter]= counter[letter]+1

for key in sorted(counter):
    print(str(key) + ":" + str(counter[key]))