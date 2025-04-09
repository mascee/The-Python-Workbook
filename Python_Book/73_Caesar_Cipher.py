# This program implements Caesar Cipher.
# It begins with prompting the user to write the message and encodes it using Caesar Cipher. 
# Each letter in the original message is shifted by 3 places. A becomes D, B becomes E etc.
# The last three letters in the alphabeth are wrapped around to the begining.

message = input("What message do you have? ").upper()
shift = int(input("What shift number? "))

encoded_message = ""

for i in message:
    if 'A' <= i <= 'Z':
            shifted = chr((ord(i) - ord('A') + shift) % 26 + ord('A'))
            encoded_message += shifted
    else:
            encoded_message += i
print(f"Encoded message: {encoded_message}. ")