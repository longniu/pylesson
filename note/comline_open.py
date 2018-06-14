import sys

if len(sys.argv) < 2 :
    print("Please input filename which you want to convert")
    sys.exit()

file = sys.argv[1]
with open(file) as fileobj:
    text = fileobj.read()
    print(text)
