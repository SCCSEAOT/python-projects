
# GalleryAI
Directory with several python scripts to filter out and count the images from a given directory, on the basis of some provided criterion.

# Tech Used
I have used OpenCV's haar cascade object classifiers to detect front_faces in the image-set. (Pretty Basic)
## Appendix

### FaceCounts
A Basic script which reads through a given directory and scans all ".jpg" images to count the number of faces.

It keeps seperate count for potraits and group pictures and displays the count therafter.

  
## Documentation

To use to script,
Clone the repo using
git clone 

Setup up any Python editor (I use VS code generally)

### Requirements:

Python v3.9.4


### Install the following dependencies:
cv2 , using:
pip install opencv-contrib-python

### Libraries Used :
os : for path manipulation (pre-installed with Python) \
cv2 : OpenCV library used here for all image recognition features
  
### Setup :
Navigate to the dirName.txt file and paste there, the complete path name for your image directory.
Use Double backslashes to omit read errors. \
Save the file. \
Open the terminal inside the current directory and run the command :

#### python filterFace.py

The program stats will be displayed after the scanning process is completed. <br /><br />
![demo](https://drive.google.com/uc?export=view&id=1TLXnMc54ohuBstpluuDYMYqQh9S3C5JD)
### Example:

#### Correct :
C:\\\Users\\\soham\\\Pictures\\\Photos\\\
#### Incorrect :
C:\Users\soham\Pictures\Photos    (missing double slash)\
      or,  
C:\\\Users\\\soham\\\Pictures\\\Photos  (missing end slash)           




## Authors

- [@soham ;)](https://www.github.com/code-soham)

