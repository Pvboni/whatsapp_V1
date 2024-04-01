import pywhatkit

phone_num = '+5511998995650'  # Enter recipient's phone number
message = 'hello'  # Enter your message

try:
    pywhatkit.sendwhatmsg(phone_num, message)
    print(f'Message sent to {phone_num} successfully!')
except Exception as e:
    print(f'Error: {str(e)}')
