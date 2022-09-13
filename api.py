from cgitb import reset
from cryptography.fernet import Fernet
from flask import Flask,jsonify

app= Flask(__name__)
# we will be encrypting the below string.
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/encrypt/<string:message>')
def encrypt(message):
    # message = "hello geeks"

# generate a key for encryption and decryption
# You can use fernet to generate
# the key or use random key generator
# here I'm using fernet to generate key

    key = Fernet.generate_key()
    print(key)
    

# Instance the Fernet class with the key

    fernet = Fernet(key)

# then use the Fernet class instance
# to encrypt the string string must
# be encoded to byte string before encryption
    encMessage = fernet.encrypt(message.encode())

    print("original string: ", message)
    print("encrypted string: ", encMessage)
    prikey=str(key)
    result={
        "key":prikey,
        "message":str(encMessage)
    }

# decrypt the encrypted string with the
# Fernet instance of the key,
# that was used for encrypting the string
# encoded byte string is returned by decrypt method,
# so decode it to string with decode methods
 
    
    # print("decrypted string: ", decMessage)
    return jsonify(result)

@app.route('/decrypt/<string:message>/<string:key>')
def decrypt(message,key):
    fernet1 = Fernet(key)
    try:
           decMessage = fernet1.decrypt(message).decode()
           result={
                "key":key,
                "message":str(decMessage)
    }
    except:
        print("An exception occurred")
        # return "Key and message"
        return jsonify("Key and message mismatch")

if __name__=="__main__":
    app.run(debug=True)
