This read me is half completed As im building the product after building complete i will  uplaod it fully 



setup guide for termux mobile server..

install f-droid
install termux on f droid
install termux api on it
pkg install termux-api python
pip install  flask 

then enter nano server.py
paste this code for making server there 


# This script runs 24/7 inside Termux on your phone
from flask import Flask, request, jsonify
import subprocess
import random

app = Flask(__name__)

# This is the "Ear" that listens to your main website application
@app.route('/send-sms', methods=['POST'])
def handle_sms_request():
    # 1. Capture the data sent silently from your website's server
    data = request.get_json()
    target_phone = data.get('phone_number')
    
    # 2. Generate the code
    otp_code = str(random.randint(100000, 999999))
    message = f"Your verification code is: {otp_code}"
    
    # 3. Python automatically executes the Termux command behind the scenes
    command = ["termux-sms-send", "-n", target_phone, message]
    subprocess.run(command, check=True)
    
    # 4. Tell your website server what the code was so it can check it later
    return jsonify({
        "status": "success", 
        "sent_to": target_phone,
        "code_to_verify": otp_code
    })

if __name__ == '__main__':
    # Start the server listening on port 5000
    app.run(host='0.0.0.0', port=5000)


click ctrl o to save then enter then click ctrl x to exit 

then type python server.py


it must output something 


* Running on all addresses (0.0.0.0)
* Running on http://127.0.0.1:5000
* Running on http://192.168.43.1:5000     <----------------- Keep eye on this line whatever ip it has you have to type it in totp.py connection time so that connnection should listen to actual address   and bonus it changes every time you kill a server and created new