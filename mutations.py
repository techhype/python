st="abracadabra"

print('mutating  string letter:',st[5])

st=list(st)

#first method(list method)
#making string into list
print("list:",st)
#changing the letter st[4]=k
st[4]='k'
#***join the list to form a string***
st="".join(st)
print(st)

#second method(slicing method)
st=st[:5]+'o'+st[6:]
print(st)
