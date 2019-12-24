class Network:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges

class Vertice:
    def __init__(self, x, y, travelled, batteryCharge):
        self.travelled = travelled
        self.batteryCharge = batteryCharge
        self.x = x
        self.y = y
        

class Edge:
    def __init__(self, v1, v2, weight):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight
