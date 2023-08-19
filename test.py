# Importing Image from PIL package
from PIL import Image
import matplotlib.pyplot as plt
import cv2

# creating a image object

image_path = r"C:\Users\hp\OneDrive\Desktop\sample images\purification1.jpg" # input the path of the image
print(image_path)
im = Image.open(image_path)
px = im.load()
# print(px[0, 0])
# print(sum(px[0, 0]))

# coordinate = x, y = 150, 59
#
# # using getpixel method
# print(im.getpixel(coordinate));
# print(im.size)
width = im.size[0]
height = im.size[1]

arr=[]
arr_sum = []
max_x =[]
max_y =[]


#algorithm
for i in range(0,width):
    for j in range(0,height):
        arr.append((sum(px[i,j]))/765)
    arr_sum.append((1-((sum(arr))/len(arr)))*1000)
    arr =[]
# print(arr_sum)
# print(len(arr_sum))

# x axis values
x = []
for k in range(0,width):
    x.append(k)
# y-axis value
y = arr_sum

#getting the peak values

for i in range(0,len(y)):
    if max(y) == y[i]:
        max_y.append(y[i])
        max_x.append(x[i])

print(len(max_y))
img = cv2.imread(image_path)
plt.title('image')
plt.plot(x, y)

plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.show()
fig, ax = plt.subplots()
ax.imshow(im, extent=[0, width, 0, max(y)])
ax.plot(x, y, '-', linewidth=2, color='firebrick')
ax.plot(max_x, max_y, '.', linewidth=1, color='black')
plt.show()