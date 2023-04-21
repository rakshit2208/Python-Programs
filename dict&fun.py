d1 = {"Rohit":"Burger","Vedant":"Roti","Mohan":"Food","shubham":{"B":"maggie","c":"roti"}}
print(d1["shubham"])
d1["Raja"]="Junk food"
print(d1)

print(d1.keys())           #keys fun
print(d1.items())          #items fun
d2 = d1
del d2["Rohit"]
print(d1)
