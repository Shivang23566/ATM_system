import pyotp 
import qrcode
import random

user_secret = pyotp.random_base32()

user_id = f"User - {random.randint(1000,9999)}"

uri = pyotp.totp.TOTP(user_secret).provisioning_uri(
    name=user_id,
    issuer_name='ATM system'
)

img = qrcode.make(uri)
img.show()
# 1. Pull the user_secret from your DB based on logged-in user
# 2. Instantiate the TOTP calculator using that secret
totp = pyotp.TOTP(user_secret)

# 3. Read what the user typed in your form
user_input_code = int(input("Enter the otp from mobile: "))

# 4. Verify (returns True if valid, False if incorrect/expired)
if totp.verify(user_input_code):
    print("Success! Access Granted.")
else:
    print("Invalid or expired code.")
