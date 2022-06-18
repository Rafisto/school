import math
import cv2
import numpy
import numpy.fft as Fourier
import matplotlib.pyplot as plt

# Grayscale_Cat source - wikimedia commons https://commons.wikimedia.org/wiki/File:Grayscale_Cat.jpg



image = cv2.imread('Grayscale_Cat.jpg', 0)
plt.title("Obraz wejściowy")
plt.imshow(image, "gray")
plt.show()

xsize = int(image.shape[0])
ysize = int(image.shape[1])
cxs = xsize/2
cys = ysize/2

size = 200
n = 1
k = 0.1
sigx = xsize/ysize
sigy = 20
Wc = 0.1

plt.title("Funkcja wyostrzająca")
expimage = numpy.zeros((xsize, ysize))
for x in range(xsize):
    for y in range(ysize):
        expimage[x, y] = math.exp(-((x-cxs)**2/(2*sigx**2)+(y-cys)**2)/(2*sigy**2))

# plt.title("Bessel")
# expimage = numpy.zeros((xsize, ysize))
# for x in range(xsize):
#     for y in range(ysize):
#         if (x-cxs) != 0 and (y-cys) != 0:
#             expimage[x, y] = abs((math.sin(Wc*(x-cxs))*math.sin(Wc*(y-cys)))/(Wc*(x-cxs)*Wc*(y-cys)))
#         # expimage[x, y] = math.exp(-((x - cxs) ** 2 / (sigy*2 * sigx ** 2)))
#         # expimage[x, y] = math.exp(-((y - cys) ** 2 / (sigx * 2 * sigy ** 2)))

plt.imshow(expimage, "gray")
plt.show()


image_fourier = Fourier.fftshift(Fourier.fft2(image))
plt.title("Przekształcenie obrazu wejściowego")
plt.imshow(numpy.log(1+abs(image_fourier)), "gray")
plt.show()

print(image_fourier)

# for x in range(int(image_fourier.shape[0]/2-size), int(image_fourier.shape[0]/2+size)):
#     for y in range(int(image_fourier.shape[1]/2 - size), int(image_fourier.shape[1]/2 + size)):
#         image_fourier[x, y] = 1/((x+y)/2)

center_x = int(image_fourier.shape[0])/2
center_y = int(image_fourier.shape[1])/2


# for x in range(0, int(image_fourier.shape[0]-1)):
#     for y in range(0, int(image_fourier.shape[1]-1)):
#             image_fourier[x, y] = image_fourier[x,y]*expimage[x,y]

image_fourier = image_fourier*expimage

plt.title("Przefiltrowane przekształcenie")
plt.imshow(numpy.log(1+abs(image_fourier)), "gray")
plt.show()

reverse_image = Fourier.ifft2(Fourier.ifftshift(image_fourier))
plt.title("Przekształcony obraz")
plt.imshow(numpy.abs(reverse_image), "gray")
plt.show()