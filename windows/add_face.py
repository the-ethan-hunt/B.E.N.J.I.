import cv2

def add_face_detect(link):
    name = link[1]				# Add Username
    path = 'C:/dataset' 		# Directory location
    cam = cv2.VideoCapture(0)	# To capture images of the user
    ret, img = cam.read()
    cv2.imwrite(path + "/" + str(name) + ".jpg", img)
    cam.release()
    cv2.destroyAllWindows()
