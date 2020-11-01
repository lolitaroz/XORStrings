import sys
mode = sys.argv[1]
keyfile = sys.argv[2]
inpfile = sys.argv[3]

key = open(keyfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
inp = open(inpfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
debug = False

if(debug):
    print("mode: "+mode)
    print("key: "+key)
    print("inp: "+inp)

def loopKey(text, key):
    fullKey = ""
    x = 0
    while x != len(text):
        fullKey = fullKey + key[x % len(key)]
        x = x + 1
    return fullKey

def human(text, key):
    ans = ""
    for i in range(len(text)):
        ans = ans + chr(ord(text[i]) ^ ord(key[i]))
    return ans

def numOut(text, key):
    ans = ""
    for i in range(len(text)):
        ans = ans + hex(ord(text[i]) ^ ord(key[i]))[2:] + " "
    return ans

if (len(key) < len(inp)):
    key = loopKey(inp, key)
if (mode == "human"):
    print(human(inp, key))
else:
    print(numOut(inp, key))
