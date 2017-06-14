import numpy as np
from skimage import io

''' Returns average value for each channel in array form: [r,b,g] '''
def getAverageColor(image):
    r = 0
    g = 0
    b = 0
    averages = np.empty(3)
    for i in range(3):
        val = np.average(img[:,:,i])
        averages[i] = val
    return averages


if __name__ == '__main__':
    filename = 'images/da.jpg'
    img = io.imread(filename)

    averages = getAverageColor(img)

    out = np.empty([20,20,3])
    for i in range(3):
        out[:,:,i].fill(averages[i])
    io.imshow(out)
    io.show()



