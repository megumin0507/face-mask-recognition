# face-mask-recognition

To run this file, you need to go environment set-up first. Go to to the net and download "Anaconda Distribution".
To download the OpenCV module using in this project, enter the code below in the Anaconda Prompt, which should be in the folder of Anaconda Distribution after you've download it.

   pip install -v opencv-python==4.2.0.34

After set-up, you should be able to run this file. Open face_mask_detection.py and run it. Notice that you should also have "haar_mask.xml" be in the same folder.
The camera on your device should be turn on. The program would detect the people in the camera whether they are wearing face mask.
If it is a person with mask on, the program would circle it with green color, otherwise it is red.
To end the program, just type "q" on your keyboard. The camera would be turn off and take a screenshot the time you turn off it, which sholud be saved in the same folder as the .py file.
If you don't want that, just remove line 26 and it would be fine.

The process I train this detection module is actully highly rely on the repository for haar-training not attributed to me.
Go to the link below for further imformations.
  
  https://github.com/sauhaardac/haar-training
