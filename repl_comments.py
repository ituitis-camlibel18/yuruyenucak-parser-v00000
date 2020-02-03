from hashlib import sha256
import socket
entries = list()
def create_hash(password):
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()





pw2 = input('Please enter your password:')
hsh2 = create_hash(pw2)


def printEntries():
    for x in entries:
        print(x)
while hsh2 != '16d3e6b0c5fa151197046b81d65d8f42155fd02e3dbc085a535bd297b2220d3c':
  print ('wrong password please try again')
  pw3 = input("Please enter your password again: ")
  hsh2 = create_hash(pw3)


while hsh2 == '16d3e6b0c5fa151197046b81d65d8f42155fd02e3dbc085a535bd297b2220d3c' :
      
 entry = input('Input [If you want to exit please write exit ] ')
 entries.append(entry)
 printEntries()
 if entry == 'exit' or entry == 'EXIT' or entry == 'Exit':
  break
     


print("Finished")
