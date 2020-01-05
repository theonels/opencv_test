import cv2

'''
return lists of rectangle examples on both sides of the line given
points: [], the list of the key points of the boundary line    
gap: int, Sampling interval
dis: int, the distance from the bottom edge of sample to the boundary line
width: int, the width of sample area
height: int, the height of sample area

'''
def get_rectangle_examples(img,points,gap,dis,width,height):
    if len(points)<2:
        return None
    topAreas = []
    bottomAreas = []
    imgHeight,imgWidth = img.shape[0],img.shape[1]
    for index,point in enumerate(points[:-1]):
        # when there is no K for this line segment
        if point[0]==points[index+1][0]:
            #left parts
            topLeft = 0 if point[0]-dis-width<0 else point[0]-dis-width
            topRight = 0 if point[0]-dis<0 else point[0]-dis
            bottom = point[1] if point[1]<imgHeight else imgHeight
            top = 0 if bottom-height<0 else bottom-height
            topAreas.append(img[top:bottom,topLeft:topRight])
            # right parts
            bottomRight = imgWidth if point[0] + dis + width > imgWidth else point[0] + dis + width
            bottomLeft = imgWidth if point[0] + dis > imgWidth else point[0] + dis
            bottomAreas.append(img[top:bottom, bottomLeft:bottomRight])
            while top < points[index + 1][1]:
                bottom = point[1]-height-gap if point[1]-height-gap < imgHeight else imgHeight
                top = 0 if bottom - height < 0 else bottom - height
                topAreas.append(img[top:bottom, topLeft:topRight])
                bottomAreas.append(img[top:bottom, bottomLeft:bottomLeft])
        # when there is a K for this line segment
        else:
            pass




if __name__=="__main__":

    matrix = cv2.imread("./resource/image/test.png")
    print(matrix.shape)             # width,height,band
    print(type(matrix)) # width,height,band
    cv2.namedWindow("test",cv2.WINDOW_NORMAL)     # create a window with a certain size
    cv2.imshow("test",matrix)                     # show image matrix in window

    k = cv2.waitKey(0)                            # keyboard binding function
    if k == 27:  # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == ord("s"):  # wait for S key to save and exit
        cv2.imwrite("./res/image/test.png",matrix)
        cv2.destroyWindow("test")

