import hashlib
mac_adr = input("Please input your Mac Address: ")
code = hashlib.sha256(mac_adr.encode('utf-8'))
print(code.hexdigest())
