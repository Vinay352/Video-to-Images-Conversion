import cv2,argparse

ap=argparse.ArgumentParser()
ap.add_argument('-i','--input',required=True,help='path to input video')
ap.add_argument('-o','--output',required=True,help='path to output images folders')
args=vars(ap.parse_args())

print("[INFO] processing video...")
stream = cv2.VideoCapture(args["input"])

cframe=0
while(True):
    grabbed,frame=stream.read()
    
    if not grabbed:
        break
    
    fileName=args['output'] + str(cframe) + '.jpg'
    print('Creating....'+fileName)
    cv2.imwrite(fileName,frame)
    
    cframe += 1
    
stream.release()
stream.stop()
cv2.destroyAllWindows()