import regex as re
email=input("Enter Your email address :").strip()
s=re.split('@',email)
print("Username : ",s[0],"\n","Domain : ",s[1])

