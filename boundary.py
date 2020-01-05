import cv2

matrix = cv2.imread("./resource/image/test.png")
print(matrix.shape)             # width,height,band
cv2.namedWindow("test",cv2.WINDOW_NORMAL)     # create a window with a certain size

cv2.imshow("test",matrix)                     # show image matrix in window
k = cv2.waitKey(0)                            # keyboard binding function
if k == 27:  # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord("s"):  # wait for S key to save and exit
    cv2.imwrite("./res/image/test.png",matrix)
    cv2.destroyWindow("test")

