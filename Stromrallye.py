import Network

def parse(toParse):
    lines = toParse.split("\n")
    size = int(lines[0])
    vertices = list()
    edges = list()
    for i in range(size):
        for j in range(size):
            v = Network.Vertice(j, i, False, 0)
            vertices.append(v)
            print()
            if(j > 0):
                e = Network.Edge(v, vertices[len(vertices) - 2], 1)
                edges.append(e)
            if(i > 0):
                e = Network.Edge(v, vertices[len(vertices) - 1 - size], 1)
                edges.append(e)

    for line in lines[1:]:
        if(bool(line)):
            chars = line.split(" ")
            x = int(chars[0])
            y = int(chars[1])
            batteryCharge = int(chars[2])
            vertices[y * size + x].batteryCharge = batteryCharge

    return Network.Network(vertices, edges)

def input(path):
    f = open(path, "r")
    text = f.read()
    network = parse(text)
    return network

def output(feasable, path):
    print(feasable, path)

network = input("BWINF38\BWInf38A1\Examples\example1.txt")



