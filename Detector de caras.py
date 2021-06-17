import cv2
import dlib
from skimage import color
from skimage import io


detector = dlib.get_frontal_face_detector()

img = io.imread('image.jpg')

faces = detector(img)
i = 0
for face in faces:
    x1 = face.left()
    y1 = face.top()
    x2 = face.right()
    y2 = face.bottom()


    i = i+1
    cv2.rectangle(img=img, pt1=(x1, y1), pt2=(x2, y2), color=(0, 255, 0), thickness=4)
texto = "Hay "+ str(i) + " caras"
ubicacion = (200,700)
font = cv2.FONT_HERSHEY_TRIPLEX
tamañoLetra = 5
colorLetra = (221,82,196)
grosorLetra = 10

#Escribir texto
cv2.putText(img, texto, ubicacion, font, tamañoLetra, colorLetra, grosorLetra)
cv2.imshow(winname="Face", mat=img)

cv2.waitKey(delay=0)

cv2.destroyAllWindows()
print("hola")

