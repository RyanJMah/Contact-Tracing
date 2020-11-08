import hashlib
mac_adr = input("Please input your UUID: ")
code = hashlib.sha256(mac_adr.encode('utf-8'))
print(code.hexdigest())