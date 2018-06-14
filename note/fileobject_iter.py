file = "./fox.txt"

target = "me"

with open(file, "r") as fileobj:
    while True:
        try:
            line = next(fileobj)
            if line.find(target) >= 0 :
                text = f"{target} is found."
                print(text)
                print(line, end = "")
                break
        except StopIteration:
            print("target can not be found")
            break
