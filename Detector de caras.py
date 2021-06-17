import cv2
import dlib
from skimage import io


detector = dlib.get_frontal_face_detector() ##función que detecta caras##

img = io.imread('image.jpg')##bajar la imagen##

faces = detector(img) ##aplicar la función a la imagen##
i = 0 ##contador de caras##
for face in faces:
    x1 = face.left() ##coordenadas de referencia para dibujar el rectángulo##
    y1 = face.top()
    x2 = face.right()
    y2 = face.bottom()


    i = i+1 ##aumento del contador por iteración de caras##
    cv2.rectangle(img=img, pt1=(x1, y1), pt2=(x2, y2), color=(0, 255, 0), thickness=4) ##dibuja un rectangulo alrededor de la cara##
texto = "Hay "+ str(i) + " caras" ##esta y las siguientes 5 lineas dan las condiciones del texto que da el numero de caras""
ubicacion = (200,700)
font = cv2.FONT_HERSHEY_TRIPLEX
tamañoLetra = 5
colorLetra = (221,82,196)
grosorLetra = 10

##Escribir texto en la imagen##
cv2.putText(img, texto, ubicacion, font, tamañoLetra, colorLetra, grosorLetra)
cv2.imshow(winname="Face", mat=img)  ##muestra la imagen##

cv2.waitKey(delay=0) ##tocar una tecla para cerrar la imágen en la subsiguiente linea##

cv2.destroyAllWindows()##hace que se cierre la ventana de la imagen##


