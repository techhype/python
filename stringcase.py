y="Hello,World"
a=""
for w in y:
    if w.isupper()==True:
        a+=w.lower()
    if w.islower()==True:
        a+=w.upper()
print(a)
