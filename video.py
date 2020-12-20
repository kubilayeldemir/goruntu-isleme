import cv2 as cv




def video():    
    source = "video/world.mp4"
    cap = cv.VideoCapture(source)
    print(cap)
    while True:
        ret, frame = cap.read()        
        edges = cv.Canny(frame, 100, 200)

        cv.imshow("World", edges)
        if cv.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    cv.destroyAllWindows()









