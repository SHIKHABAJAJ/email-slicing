email=input("Enter Your email address :").strip()
find=email.index('@')
username=email[:find]
domain=email[find+1:]
print("Username : " ,username)
print("Domain   : ", domain)
