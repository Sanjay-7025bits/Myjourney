from random import *
import time
import subprocess
import re

def check_lsb(new_mac):
    # Split MAC into bytes
    first_byte_str = new_mac.split(":")[0]
    
    # Convert from hex string to integer
    first_byte = int(first_byte_str, 16)

    # Use bitwise AND with 1 to check LSB
    lsb = first_byte & 1

    return lsb

def randmac(n):
    list1 = ["","","1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e"]
    i = 1
    mac = ""
    while True:
        if i >12:
            break
        else:
            c = randint(2,15)
            digit = list1[c]
            mac = mac+digit
            if i % 2 == 0 and i!=12:
                mac = mac+":"
            i +=1
    
    return mac
    
def macchanger(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    
def current_mac(interface):
    output = subprocess.check_output(["ifconfig", interface]).decode()
    match = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", output)
    print("[*] Current MAC:", match.group(0))

n = int(input("MAC changing timing in seconds: "))
interface = input("Please enter which interface: ")
    
while True:
    time.sleep(n)
    new_mac = randmac(n)
    c = check_lsb(new_mac)
    if  c != 0:
       continue
    macchanger(interface, new_mac)
    current_mac(interface)