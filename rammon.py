import psutil
import requests

# threshold percentage of ram
threshold = 10

#getting percent of used memory
used_percentage = psutil.virtual_memory().percent

#alert api url
url = "http://127.0.0.1:5000/alert"

#checking percent
if used_percentage > threshold:

#set up message
    message = {"Alert": "RAM usage is over threshold","percent":used_percentage}
    response = requests.post(url=url,json=message)

#check status of response
    if response.status_code==200:
 
        print("Alert sent succesfully")
 
    else:
 
        print("Error due alert sending: ", response.text)