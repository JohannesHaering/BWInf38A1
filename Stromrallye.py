def parse(toParse):
    return 0

def input(path):
    f = open(path, "r")
    text = f.read()
    network = parse(text)
    return network

def output(feasable):
    print(feasable)



