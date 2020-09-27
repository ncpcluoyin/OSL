import os
print("link to the git repository?")
a = input("(y/n)")
if a!="y":
    exit()
a = input("Your repository(http/https):")
file = open("package/gitrepository")
file.write(a)
file.close()
print("OK")