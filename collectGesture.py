import cv2,os,time

def collectGestureImages():
    '''
    Take a folder name as input from user and create it if not exisits
    Open camera capture each frame and save it in that folder
    '''
        
    folderName = input("Enter the folder name to save the images: ")
    if not os.path.exists(folderName):
        os.makedirs(folderName)
    cam = cv2.VideoCapture(0)
    time.sleep(1)
    img_counter = 0
    while True:
        ret, frame = cam.read()
        if ret:
            cv2.imwrite(folderName+"/frame%d.jpg" %img_counter, frame)
            img_counter += 1
            print("Current File %d \r" %img_counter, end = '')
            cv2.imshow('frame', frame)
        else:
            break
        #Break if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()
    print("Created folder: " + folderName)


collectGestureImages()