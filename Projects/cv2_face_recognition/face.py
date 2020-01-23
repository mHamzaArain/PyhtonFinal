import cv2
import time
import os

def onlyImageFiles(folderName=None):
    if folderName == None:
        folderName = os.getcwd()
    else:
        os.chdir(folderName)
        folderName = os.getcwd()

    # fileList = os.listdir() # ['6.png', '5.jpeg', '1.jpg', '4.jpg', '2.jpg', '3.jpg']
    allFiles = list()
    # print(os.walk(os.chdir('pictures')))
    for path, folders, files in os.walk(str(folderName)):
        for file in files:
            if file.endswith('.jpeg') or file.endswith('.jpg') or file.endswith('.png'): 
                finalPath = os.path.join(path, file)
                allFiles.append(finalPath)
                
    return allFiles


def main():
    folderName = 'pictures'
    imageFilesList = onlyImageFiles(folderName)

    for imageFile in  imageFilesList:
        casePath = 'haarcascade_frontalface_default.xml'
        faceCascade = cv2.CascadeClassifier(casePath)
        image = cv2.imread(imageFile)
        width, height = image.shape[:2]
        image = cv2.resize(image, (int(height/2), int(width/2)))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(gray, 
                                    scaleFactor=1.1,
                                    minNeighbors=5,
                                    minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w,y+h), (0, 255, 0), 2)

        cv2.imshow("ImageWindow", image)
        cv2.waitKey(0)
        # time.sleep(3)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()