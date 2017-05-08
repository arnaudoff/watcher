#wget http://www.linux-projects.org/listing/uv4l_repo/lrkey.asc && sudo apt-key add ./lrkey.asc
#sudo nano /etc/apt/sources.list
#     #add this to the bottom of the sources list
#     deb http://www.linux-projects.org/listing/uv4l_repo/raspbian/ wheezy main
#sudo apt-get update
#sudo apt-get install -y uv4l uv4l-raspicam uv4l-raspicam-extras uv4l-server
#sudo service uv4l-_raspicam start

from SimpleCV import *

cam = Camera()

display = Display((800,600))

#set a variable for the motion threshold
threshold = 5.0

while True:
    #grab the first image from the camera
    img01 = cam.getImage().toGray()
    
    time.sleep(0.5)
    #grab another image from the camera
    img02 = cam.getImage().toGray()
    #calculate the difference between the images
    #binarize the image to black and white and then invert the colors
    diff = (img01 - img02).binarize(50).invert()
    #show the results
    diff.show()

    #store all of the image values in a matrix array
    matrix = diff.getNumpy()
    #calculate the mean of the values to determine how much has changed
    mean = matrix.mean()

    #if the ammount changed is greater than our threshold, then save the image
    if mean >= threshold:
        
        i = 0
        while os.path.exists('image%s.png' % i):
            i += 1

        img02.save('image%s.png' % i)

        print('Motion Detected')