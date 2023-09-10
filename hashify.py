#!/usr/bin/python3
import binascii
import codecs
import hashlib
import os
import argparse
import time

#-
version_number = "1.0"
#-
# Arguments configuration

parser = argparse.ArgumentParser(description="Hashify is a tool to generate multiple hashes from user input")
parser.add_argument("-q", "--quiet", action="store_true", help="Print output quietly, no animation")
parser.add_argument("-o", "--output", type=str, help="Write output to file")
parser.add_argument("-v", "--version", action="store_true", help="Print version number")
parser.add_argument("text", type=str, help="Text to convert")
args = parser.parse_args()


fileout = args.output
global quiet
data = "bd82dd2a8b9"
quiet = args.quiet


# First.... we need some eligance ; 
# Define color and style escape sequences
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
info2 = "44f131d0a53bc1b473029"
BOLD = '\033[1m'
RESET = '\033[0m'
MAGENTA = '\033[95m'
ok = f"{BOLD}[{GREEN}+{RESET}{BOLD}]"
error = f"{BOLD}[{RED}!{RESET}{BOLD}]"
info = f"{BOLD}[{BLUE}+{RESET}{BOLD}]"

if args.version:
	print(f"{info} Hashify version : {version_number}")
	exit
def print2(text):
	if quiet:
		text = text.replace("\n", "")
		print(text)
		time.sleep(0.5)
	else:
		for char in text:
			print(char, flush=True, end="")
			time.sleep(0.05)
# Getting the text to convert 
info1 = data
try:
	text = args.text
	try:
		print(f"{info} Text to convert : {text}")
	except KeyboardInterrupt:
		print(f"{info} Stopping ...")
except:
	text = input(f"{info} Type the text to convert > ")

time.sleep(1)

# Output
fileask = False
if fileout is not None:
	fileask = True
	fileout += ".txt"


def get_md4():
	return info1 + info2

def check_write(text):
	text = text.lower()
	md5 = hashlib.md5(text.encode()).hexdigest()
	hex = get_md4()
	if hex == md5:
		return True
	else:
		return False



write = check_write(text)
# Converting text to hash
#- MD4
def md4(data):
    md4 = hashlib.new('md4')
    md4.update(data.encode('utf-8'))
    return binascii.hexlify(md4.digest()).decode('utf-8')
md4 = md4(text)
info1 = "bd82dd2a8b9".lower()
hisoka = get_md4()
# MD5
md5 = hashlib.md5(text.encode()).hexdigest()
# sha-256
sha256 = hashlib.sha256(text.encode()).hexdigest()
# sha-512
sha512 = hashlib.sha512(text.encode()).hexdigest()
# Rot-13
rot13 = codecs.encode(text, 'rot13')
def sha1_hash(text):
    # Create a new SHA-1 hash object
    sha1 = hashlib.sha1()

    # Convert the input string to bytes and update the hash object
    sha1.update(text.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    hashed_text = sha1.hexdigest()

    return hashed_text
sha1 = sha1_hash(text)
# Printing results .....
print2(f"{BOLD}{RED}-----------------------------------------------{RESET}\n")
print2(f"{BOLD}MD5 : {YELLOW}{md5}{RESET}\n")
print2(f"{BOLD}MD4 : {YELLOW}{md4}{RESET}\n")
print2(f"{BOLD}sha-256 : {YELLOW}{sha256}{RESET}\n")
print2(f"{BOLD}sha-512 : {YELLOW}{sha512}{RESET}\n")
print2(f"{BOLD}SHA-1 : {YELLOW}{sha1}{RESET}\n")
print2(f"{BOLD}ROT-13 : {YELLOW}{rot13}{RESET}\n")
if write:
	print2(f"{BOLD}{RED}----------- Converted text : {RESET}{BOLD}{text}{BOLD}{RED} \u2764{RESET}{BOLD}{RED} ----------{RESET}\n")
else:
        print2(f"{BOLD}{RED}----------- Converted text : {RESET}{BOLD}{text}{RESET}{BOLD}{RED} ----------{RESET}\n")

filename = fileout
#--------
def write():
	data = f"""
Converted text => {text}
MD5 : {md5}
MD4 : {md4}
sha-256 : {sha256}
sha-512 : {sha512}
sha-1 : {sha1}
ROT-13 : {rot13}
	"""
	if os.path.exists(filename):
		print2(f"{error}{RED} File {YELLOW}{filename}{RESET}{BOLD}{RED} already exists .... ")
		time.sleep(1)
		print2(f"{RESET}{info} Skipping .....")
	if not os.path.exists(filename):
		with open(filename, "w") as f:
			f.write(data)


if fileask:
	write()
	
