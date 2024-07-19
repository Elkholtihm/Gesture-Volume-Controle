import HandTrackingModule as htm
import numpy as np
import cv2
import math
import time
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import HandTrackingModule as hm




def main():
    # initialize previous time and currnent time variables to draw the frame rate
    pTime = 0
    cTime = 0

    # capturing videos via the webcam (used to open a video file or webcam)
    cap = cv2.VideoCapture(0)

    # define an instance of the class
    detector = hm.HandDetector()

    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    # volume.GetMute()
    range = volume.GetVolumeRange()
    #volume.GetMasterVolumeLevel()


    while True:
        # success to whether the frame is successfully read, img capture image 
        success, img = cap.read()

        # use the track methode of the class 
        img, lmlist = detector.Track(img)

        minV = range[0]
        maxV = range[1]

        if len(lmlist) != 0:
            # get x and y positions of landmark 4 and 8 
            x4, x8 = lmlist[4][1], lmlist[8][1]
            y4, y8 = lmlist[4][2], lmlist[8][2]
            
            # center position between the landmarks 4 and 8
            xc, yc = (x4 + x8) // 2, (y4 + y8) // 2

            # leght between landmark 4 and 8
            lenght = math.hypot(x8 - x4, y8 - y4)

            # convert range of the lenght (200-0) to the volume (-96, 0)
            vol = np.interp(lenght, [15, 250], [minV, maxV])
            volBar = np.interp(lenght, [15, 250], [60, 300])
            vol_porcentage = np.interp(lenght, [15, 250], [0, 100])

            # set the master volume
            volume.SetMasterVolumeLevel(vol, None)

            # create a bare for volume
            cv2.rectangle(img, (30, 300), (100, 60), (255, 255, 0), 2)
            cv2.rectangle(img, (30, int(volBar)), (100, 60), (255, 255, 0), cv2.FILLED)
            cv2.putText(img, f'volume is {int(vol_porcentage)}', (30, 40), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 255), 2)

            # drawing a circle in landmarks 4 and 8 and between them
            cv2.circle(img, (x4, y4), 5, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x8, y8), 5, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (xc, yc), 5, (255, 0, 0), cv2.FILLED)

            # drwing a line betwen the landmark 4 and 8
            cv2.line(img, (x4, y4), (x8, y8), (255, 0, 255), 2)
        # calculating the frame rate 
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        # display the frame rate
        cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

        # show frames with landmarks
        cv2.imshow('Image', img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()




