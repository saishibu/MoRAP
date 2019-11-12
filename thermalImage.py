import sys
import numpy as np
import cv2
import matplotlib as mpl
import matplotlib.cm as mtpltcm

def main(argv):
	cap = cv2.VideoCapture(0)
#initialize the colormap
	colormap = mpl.cm.hot
	cNorm = mpl.colors.Normalize(vmin=0, vmax=128)
	scalarMap = mtpltcm.ScalarMappable(norm=cNorm, cmap=colormap)

#	cap=cv2.imread('image.jpg')
#	while (True):
        # Capture frame-by-frame
	ret, frame = cap.read()
	cv2.imwrite('raw.jpg',frame)

        # Our operations on the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imwrite('gray.jpg',gray)
	blur = cv2.GaussianBlur(gray,(15,15),0)
		#assign colormap
#	colors = scalarMap.to_rgba(gray, bytes=False)
	colors = cv2.applyColorMap(blur, cv2.COLORMAP_JET)
#	colors = cv2.bitwise_not(colors)
        # Display the resulting frame
#        cv2.imshow('frame', colors)

#	if cv2.waitKey(1) & 0xFF == ord('q'):
	cv2.imwrite('thermal1.jpg',colors)
#break

    # When everything done, release the capture
   # cap.release()
    #cv2.destroyAllWindows()

if __name__ == '__main__':
	sys.exit(main(sys.argv))

