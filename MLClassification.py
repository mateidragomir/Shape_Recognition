import sklearn.datasets 
import skimage.data 
from sklearn import svm
import numpy
import os
flatTestImage = []
correctAnswers = 0
fileNum = 0

correctAnswersTri = 0
fileNumTri = 0

correctAnswersQua = 0
fileNumQua = 0

correctAnswersPen = 0
fileNumPen = 0

def loadFlatData (fileName):
    #load the image as a black and white two dimensional array
    testImage = skimage.data.imread(fileName, asGrey=True)
    #flatten the data into a 1D array
    flatTestImage = numpy.reshape(testImage, 255*255)
    return flatTestImage

def loadDataFromPath(path):
    theData = sklearn.datasets.load_files(path, description=None, categories=None, load_content=False, shuffle=True, encoding=None, decode_error='strict', random_state=0)

    #create an empty array to put the content of the files in
    theData.data =[]

    #for all files in the list
    for fileName in theData.filenames:
        #add the 1D array to trainingData.data
        theData.data.append(loadFlatData(fileName))
    return theData

path = 'C:\\python code\\shape recognition\\AI test folder\\GeneratedShape\\training\\'

#load training data from the root folder.
trainingData = loadDataFromPath(path)

#create a svm SVC classifier
classifier = svm.SVC(kernel='poly')

#fit the data with the training
classifier.fit(trainingData.data, trainingData.target)

print ('training complet')

testPath  = "C:\\python code\\shape recognition\\AI test folder\\GeneratedShape\\Test\\"
testData = loadDataFromPath(testPath)

#predict the shapes in the test data  
testData.predictedShape = classifier.predict(testData.data)

#check how many are right
for i in range(0, len(testData.predictedShape)):
    fileNum = fileNum + 1

    if testData.target_names [testData.target[i]]=='triangle':
        fileNumTri = fileNumTri + 1
        if testData.predictedShape[i] == testData.target[i]:
            correctAnswers = correctAnswers + 1
            correctAnswersTri = correctAnswersTri + 1
    elif testData.target_names [testData.target[i]]=='quadrilateral':
        fileNumQua = fileNumQua + 1
        if testData.predictedShape[i] == testData.target[i]:
            correctAnswersQua = correctAnswersQua + 1
            correctAnswers = correctAnswers + 1
    else:
        fileNumPen = fileNumPen + 1
        if testData.predictedShape[i] == testData.target[i]:
            correctAnswersPen = correctAnswersPen + 1
            correctAnswers = correctAnswers + 1
         


print (str(fileNumTri)+" total triangle files")
print (str(correctAnswersTri)+" correct answers")
methodEfficency = correctAnswersTri / fileNumTri * 100
print (methodEfficency)

print (str (fileNumQua)+" total quadrilateral files")
print (str (correctAnswersQua)+" correct answers")
methodEfficency = correctAnswersQua / fileNumQua * 100
print (methodEfficency)

print (str (fileNumPen)+" total pentagon files")
print (str (correctAnswersPen)+" correct answers")
methodEfficency = correctAnswersPen / fileNumPen * 100
print (methodEfficency)

print (str (fileNum)+" total files")
print (str (correctAnswers)+" total correct answers")
methodEfficency = correctAnswers / fileNum * 100
print (methodEfficency)
