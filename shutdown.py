#import os
#response = os.system("ping" + " google.com")
#if response == 0:
#    pingstatus = "Network Active"
#else:
#    pingstatus = "Network Error"
#print(pingstatus)


import os, time, datetime
ip_address = 'google.com'
##Count in mins
count = 5
while count > 0:
    response = os.popen(f"ping {ip_address} -n 1").read()
    if "Received = 1" in response:
        print(f"UP {ip_address} ping successful")
        count = 5
        print("Count is: ", count)
        time.sleep(5)
    else:
        print(f"DOWN {ip_address} ping unsuccessful")
        count = count - 1
        print("Count is: ", count)
        f = open('log.txt', 'a')
        #f.write("{}\n".format("This works!"))
        f.write("{}\n".datetime.now().strftime("%d_%m_%Y"))
        time.sleep(5)

#time.sleep(2)
os.system('wmic process where name="ping.exe" delete')
os.system('wmic process where name="powershell.exe" delete')
#os.system("shutdown /r /t 10")



#wmic process where name="python.exe" delete
