#import library scikit-image.
import skimage
#import datas from skimage. will be used for the function load.
import skimage.data
#importing only the corner_harris, corner_peaks
from skimage.feature import corner_harris, corner_peaks
import os

#assigning variables
correctAnswers = 0
fileNum = 0

correctAnswersTri = 0
fileNumTri = 0

correctAnswersQua = 0
fileNumQua = 0

correctAnswersPen = 0
fileNumPen = 0
#function
def nameTheShape (file):
    coords = corner_peaks(corner_harris(file), min_distance=5)
    noCorners = len (coords)
    if (noCorners == 3):
        shapeName = "triangle"
        return (shapeName)
    elif (noCorners == 4):
        shapeName = "quadrilateral"
        return (shapeName)
    elif (noCorners == 5):
        shapeName = "pentagon"
        return (shapeName)
    else:
        shapeName = "ERROR!!!"
        return (shapeName)
        
path = "C:\\python code\\shape recognition\\AI test folder\\GeneratedShape\\Test\\triangle\\"

for filename in os.listdir(path):
    if filename.endswith(".bmp"):
        fileNum = fileNum + 1
        fileNumTri = fileNumTri + 1
        shape = nameTheShape (skimage.data.load (path+filename))
        if (shape in path):
            correctAnswers = correctAnswers + 1
            correctAnswersTri = correctAnswersTri + 1
print (str(fileNumTri)+" total triangle files")
print (str(correctAnswersTri)+" correct answers")
methodEfficency = correctAnswersTri / fileNumTri * 100
print (methodEfficency)
path = "C:\\python code\\shape recognition\\AI test folder\\GeneratedShape\\Test\\quadrilateral\\"
for filename in os.listdir(path):
    if filename.endswith(".bmp"):
        fileNum = fileNum + 1
        fileNumQua = fileNumQua + 1
        shape = nameTheShape (skimage.data.load (path+filename))
        if (shape in path):
            correctAnswers = correctAnswers + 1
            correctAnswersQua = correctAnswersQua + 1

print (str (fileNumQua)+" total quadrilateral files")
print (str (correctAnswersQua)+" correct answers")
methodEfficency = correctAnswersQua / fileNumQua * 100
print (methodEfficency)
path = "C:\\python code\\shape recognition\\AI test folder\\GeneratedShape\\Test\\pentagon\\"
for filename in os.listdir(path):
    if filename.endswith(".bmp"):
        fileNum = fileNum + 1
        fileNumPen = fileNumPen + 1
        shape = nameTheShape (skimage.data.load (path+filename))
        if (shape in path):
            correctAnswers = correctAnswers + 1
            correctAnswersPen = correctAnswersPen + 1

print (str (fileNumPen)+" total pentagon files")
print (str (correctAnswersPen)+" correct answers")
methodEfficency = correctAnswersPen / fileNumPen * 100
print (methodEfficency)

print (str (fileNum)+" total files")
print (str (correctAnswers)+" total correct answers")
methodEfficency = correctAnswers / fileNum * 100
print (methodEfficency)
