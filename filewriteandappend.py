#f = open("f3.txt","a")
#f.write("Hello world\n")
#f.close()
f = open("f3.txt","r+")
print(f.read())
f.write("Thankyou")
f.close()