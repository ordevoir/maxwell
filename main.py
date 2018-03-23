import numpy as np
import math
import random
from PIL import Image, ImageDraw

image = Image.open("MNIST/mnist_train9.jpg")
width = image.size[0]
height = image.size[1]
pix = image.load()

print('size', width, height)

width_frame = 28 #width // 77
height_frame = 28 #height // 77
print(width_frame)
print(height_frame)


im_splitted = Image.new('L', (width_frame, height_frame))
draw = ImageDraw.Draw(im_splitted)

frame_number = 0

for i in range(75):
    for j in range(75):
        beginX = i * width_frame
        endX = beginX + width_frame
        beginY = j * height_frame
        endY = beginY + height_frame
        print(beginX, endX)
        print(beginY, endY)
        for k in range(beginX, endX):
            for l in range(beginY, endY):
                draw.point((k - beginX, l - beginY), pix[k, l])
#                print(k, l)
        path = "{0}_{1}.{2}".format(i, j, "jpg")
        print(i, j)
        im_splitted.save(path, "JPEG")

image.save("MNIST/example/1.jpg", "JPEG")

del draw

layer_count = 3
neuron_count = []
X = []
for i in range(16):
    X.append(random.random())

class Neuron:
    def __init__(self, layer=None, number=None):
        self.layer = layer
        self.number = number

    def init(self, N = None, W = None):
        self.N = N
        self.W = W

    def input(self, X = None):
        self.X = X

    def output(self, alpha=0.1):
        self.alpha = alpha
        i = 0
        sp = 0
        while i < self.N:
            sp += self.W[i]*self.X[i]
            i += 1
        return (1 / (1 + math.exp(-self.alpha * sp)))

map = []

for i in range(layer_count - 1):
    L = []
    for j in range(16):
        L.append(j)
    map.append(L)
L = []
for j in range(10):
    L.append(j)
map.append(L)

NeuMap = []
for i in range(layer_count):
    NeuL = []
    for j in (map[i]):
        NeuL.append(Neuron(i, j))
    NeuMap.append(NeuL)

for i in range(layer_count):
    for j in (map[i]):
        W = []
        for k in range(16):
            W.append(random.random())
        NeuMap[i][j].init(16, W)

for j in (map[0]):
    NeuMap[0][j].input(X)
for i in range(0, layer_count - 1):
    Y = []
    for j in map[i]:
        Y.append(NeuMap[i][j].output(1))
    for k in map[i+1]:
        NeuMap[i+1][k].input(Y)
out = []
for j in range(10):
    out.append(NeuMap[2][j].output(0.1))


example = Neuron(1, 3)
#weight = [0.1, 0.2, 0.0, 0.4, 0.6]
weight = [0.1, 0.1, 0.1, 0.1, 0.1]
#X = [1, 0.5, 0.3, 0.8, 0.9]
#X = [1, 0.1, 1, 0.1, 1]
example.init(len(weight), weight)
example.input(X)
#out = example.output(0.1)
print(NeuMap[2][5].layer)
print(NeuMap[1][15].number)
print(NeuMap[1][15].N)
print(NeuMap[1][15].W)
print(out)

#print(example.layer)
#print(example.number)
#print(example.N)
#print(example.W)
#print(example.X)
#print(out)

