# Run this on your LAPTOP in VS Code
import requests

def trigger_otp():
    url = "http://100.113.112.49:5000/send-sms" 
    # Put your own phone number here to test it!
    payload = {"phone_number": "+918091950952"} 
    
    print("Shooting data to the Android Phone...")
    response = requests.post(url, json=payload)
    print("The phone responded with:", response.json())

if __name__ == "__main__":
    trigger_otp()