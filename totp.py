# THIS CODE RUNS ON YOUR PC'S LOCALHOST PROJECT
import requests

def request_otp_from_phone(target_user_number):
    # 1. Put your Phone's exact Wi-Fi IP address here
    # Make sure to include http:// and :5000/send-sms
    phone_url = "http://192.168.1.15:5000/send-sms"
    
    # 2. Package the data your phone needs
    payload = {
        "phone_number": target_user_number
    }
    
    try:
        # 3. Shoot the data across the Wi-Fi room to the phone
        print("Sending request to phone over Wi-Fi...")
        response = requests.post(phone_url, json=payload)
        
        # 4. Read the response the phone sends back
        result = response.json()
        print("Success! The phone responded with:", result)
        
        # You would save this 'result' to your local database here
        return result['code_to_verify']
        
    except requests.exceptions.ConnectionError:
        print("Failed to connect. Is the Flask server running on the phone? Are they on the same Wi-Fi?")

# Test it out!
if __name__ == "__main__":
    request_otp_from_phone("+918091950952")