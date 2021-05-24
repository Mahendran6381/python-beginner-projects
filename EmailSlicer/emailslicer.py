import random
usernames = []
domains = []
email = input("Enter Your Email: ")
num = random.randint(10,10000)
temp_name = email[:5]
random = list(temp_name)
random.append(str(num))
username = "".join(random)
if username not in usernames:
    usernames.append(username)
    print("Your Username is : " +username)
domain ="www."+username +".com"
if domain not in domains:
    domains.append(domain)
    print("Your Domain is : " + domain)
else:
    print("sorry The Domain Isn't available ")    


