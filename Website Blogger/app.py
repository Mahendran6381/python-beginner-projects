from datetime import datetime as dt
import time

FILEPATH = r"C:\Windows\System32\drivers\etc\hosts"
REDIRECT = "127.0.0.1"


WEBISTE = ['www.pubs.acs.org','www.csoonline.com/in/']

while True:
    if(dt.now().year,dt.now().month,dt.now().day,11) < (dt.now().year,dt.now().month,dt.now().day,12):
        print("Website is not allowed")
        with open(FILEPATH,"r+") as file:
           content = file.read()
           for web in WEBISTE:
               if web not in content:
                   file.write(REDIRECT + " " + web +"\n")
               else:
                    pass

    else:
        print("Wait 5 sec ...Refreshing...")
        with open(FILEPATH,"r+") as file:
            contents  = file.readline() 
            file.seek(0)
            for content in contents:
              if not any(site in content for site in WEBISTE):
                  file.write(content)
              file.truncate()
            print("Website Removed") 
time.sleep(5)                
                             
