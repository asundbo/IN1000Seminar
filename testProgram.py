from node import Node
from rack import Rack
from regneklynge import Regneklynge

n1 = Node(32, 2)
n2 = Node(4, 1)
n3 = Node(8, 2)

r = Regneklynge(10)

r.test(33, 2, 2)
