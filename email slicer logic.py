##email=input("Enter Your email address :").strip()
##find=email.index('@')
##username=email[:find]
##domain=email[find+1:]
##print("Username : " ,username)
##print("Domain   : ", domain)




import regex as re
email=input("Enter Your email address :").strip()
s=re.split('@',email)
print("Username : ",s[0],"\n","Domain : ",s[1])

