import cv2
from ultralytics import YOLO

modelo = YOLO("yolov8n.pt")
camera = cv2.VideoCapture(0)

while True:
    sucesso, frame = camera.read()
    resultados = modelo(frame)
    cv2.imshow("YOLO", resultados[0].plot())
   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()

