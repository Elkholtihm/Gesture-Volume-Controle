# Gesture Volume Controle
This project aims to demonstrate the use of pose estimation for controling volume using Mediapipe and pycaw. The goal is to mesure the distance between thumb and the index finger and to convert between 0 and 100 to controle volume.

## Project Structure
The project consists of the following files:

* HandTrackingModule.py: A custom module using Mediapipe for drawing hand landmarks and to mesure the distance between thumb and the index fingers.
* Gesture_Volume_Controle.py: A script use the this modele to change volume based on the distance between thumb and index fingers.

## Using the Project
To utilize this project, follow these steps:

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/Elkholtihm/Gesture-Volume-Controle.git
    ```
2. Once you've set the model path, you can execute the `app1.py` file to run the website:
    ```bash
    python Gesture_Volume_controle.py
    ```
   
## Hand tracking Module
The HandTrackingModule.py file contains the HandDetector class, which includes methods to:

1. Find and draw hand landmarks
2. Calculate distance between thumb and the index fingers.

## Personal Trainer Script
The script performs the following steps:

1. Capture video from a webcam or a video file.
2. Detect hand landmarks.
3. Calculate distance between the two fingers.
4. chnage volume based on this distance.
5. Display the video with landmarks, distance, and volume level.

## My Linkdin
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/hamza-kholti-075288209/)

## Acknowledgments
[![Mediapipe Documentation](https://img.shields.io/badge/Mediapipe-Documentation-0A66C2?style=for-the-badge&logo=mediapipe&logoColor=white)](https://ai.google.dev/edge/mediapipe/solutions/guide) 
[![OpenCV Documentation](https://img.shields.io/badge/OpenCV-Documentation-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
[![pycaw Documentation](https://img.shields.io/badge/pycaw-Documentation-FF0000?style=for-the-badge&logo=python&logoColor=white)](https://github.com/AndreMiras/pycaw)
