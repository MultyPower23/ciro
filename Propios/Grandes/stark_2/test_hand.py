# ===============================
# IMPORTACIÓN DE LIBRERÍAS
# ===============================

import cv2  # Librería de visión por computadora
import mediapipe as mp  # Framework de detección de manos
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import random
from particles import Particle  # Nuestra clase de partículas
import time


# ===============================
# RUTA DEL MODELO DE MANOS
# ===============================

# Modelo que usa :contentReference[oaicite:0]{index=0}
# para detectar la posición de los dedos
model_path = r"E:\Codigos\Propios\Grandes\stark_1\hand_landmarker.task"


# ===============================
# CONFIGURACIÓN DEL DETECTOR
# ===============================

base_options = python.BaseOptions(model_asset_path=model_path)

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.VIDEO,  # activo el modo vidvideo con timestamp
    num_hands=2,  # máximo de manos detectadas
    min_hand_detection_confidence=0.5,  # confianza mínima para detectar mano
    min_tracking_confidence=0.5  # confianza mínima para seguir la mano
)

# Crear el detector de manos
detector = vision.HandLandmarker.create_from_options(options)


# ===============================
# ACTIVAR CÁMARA
# ===============================

cap = cv2.VideoCapture(0)


# ===============================
# CREACIÓN DE PARTÍCULAS FIJAS
# ===============================

particles = []

NUM_PARTICLES = 800  # número fijo de partículas en pantalla

for i in range(NUM_PARTICLES):

    # generar posición aleatoria dentro de la pantalla
    x = random.randint(0, 640)
    y = random.randint(0, 480)

    # crear partícula y añadirla a la lista
    p = Particle(x, y)

    # pequeña velocidad inicial aleatoria
    # evita que el sistema se vea muerto
    p.vx = random.uniform(-1, 1)
    p.vy = random.uniform(-1, 1)

    particles.append(p)


# ===============================
# CREAR VENTANA EN PANTALLA COMPLETA
# ===============================

# Crear la ventana manualmente
cv2.namedWindow("cam", cv2.WINDOW_NORMAL)

# Cambiar la ventana a pantalla completa
cv2.setWindowProperty(
    "cam",
    cv2.WND_PROP_FULLSCREEN,
    cv2.WINDOW_FULLSCREEN
)


# ===============================
# BUCLE PRINCIPAL DEL PROGRAMA
# ===============================

while True:

    # Leer un frame de la cámara
    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)


    # Convertir la imagen al formato que usa MediaPipe
    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=frame
    )


    # Generar timestamp para modo video
    timestamp = int(time.time() * 1000)

    # Detectar manos en el frame
    result = detector.detect_for_video(mp_image, timestamp)


    # ===============================
    # INTERACCIÓN DE MANOS CON PARTÍCULAS
    # ===============================

    if result.hand_landmarks:

        for hand in result.hand_landmarks:

            # centro aproximado de la mano (palma)
            palm = hand[9]

            # convertir coordenadas normalizadas (0-1) a píxeles
            hand_x = int(palm.x * frame.shape[1])
            hand_y = int(palm.y * frame.shape[0])

            # ===============================
            # DETECTAR ESTADO DE LOS DEDOS
            # ===============================

            # comprobar si cada dedo está extendido
            index_open = hand[8].y < hand[6].y
            middle_open = hand[12].y < hand[10].y
            ring_open = hand[16].y < hand[14].y
            pinky_open = hand[20].y < hand[18].y

            # ===============================
            # CLASIFICAR GESTO
            # ===============================

            open_fingers = sum([
                index_open,
                middle_open,
                ring_open,
                pinky_open
            ])

            # ===============================
            # GESTO: MANO ABIERTA
            # CAMPO ORBITAL ESTABLE
            # ===============================

            if open_fingers >= 3:

                for p in particles:

                    # vector desde partícula hacia la mano
                    dx = hand_x - p.x
                    dy = hand_y - p.y

                    # distancia
                    dist_sq = dx*dx + dy*dy + 0.0001
                    dist = dist_sq ** 0.5

                    # ===============================
                    # ATRACCIÓN FUERTE CUANDO ESTÁN LEJOS
                    # ===============================

                    gravity = 800 / dist_sq

                    p.vx += dx/dist * gravity
                    p.vy += dy/dist * gravity

                    # ===============================
                    # FUERZA TANGENCIAL (ÓRBITA)
                    # ===============================

                    swirl = 6 / (dist + 20)

                    p.vx += -dy/dist * swirl
                    p.vy += dx/dist * swirl

                    # ===============================
                    # FRENO SI SE ALEJAN MUCHO
                    # ===============================

                    if dist > 300:

                        p.vx *= 0.9
                        p.vy *= 0.9

            # ===============================
            # GESTO: DOS DEDOS
            # ARRASTRAR PARTÍCULAS CERCANAS
            # ===============================

            elif open_fingers == 2:

                for p in particles:

                    dx = hand_x - p.x
                    dy = hand_y - p.y

                    dist = (dx*dx + dy*dy) ** 0.5

                    # solo mover partículas cercanas
                    if dist < 120:

                        p.x += dx * 0.1
                        p.y += dy * 0.1

    # ===============================
    # ACTUALIZAR PARTÍCULAS
    # ===============================

    # Recorrer copia de la lista
    for p in particles[:]:

        # actualizar física de la partícula
        p.update()

        # ===============================
        # FRICCIÓN GLOBAL
        # ===============================

        # reduce lentamente la velocidad
        # evita acumulación infinita
        # fricción más suave para que el movimiento dure más
        p.vx *= 0.99
        p.vy *= 0.99

        # ===============================
        # LIMITADOR DE VELOCIDAD
        # ===============================

        max_speed = 12  # velocidad máxima permitida

        speed = (p.vx*p.vx + p.vy*p.vy) ** 0.5

        if speed > max_speed:
            
            scale = max_speed / speed
            
            p.vx *= scale
            p.vy *= scale

        # ===============================
        # COLISIÓN CON LOS BORDES
        # ===============================

        # si la partícula toca el borde izquierdo
        if p.x < 0:
            p.x = 0              # la colocamos dentro de la pantalla
            p.vx *= -0.8         # invertimos velocidad para que rebote

        # borde derecho
        if p.x > frame.shape[1]:
            p.x = frame.shape[1]
            p.vx *= -0.8

        # borde superior
        if p.y < 0:
            p.y = 0
            p.vy *= -0.8

        # borde inferior
        if p.y > frame.shape[0]:
            p.y = frame.shape[0]
            p.vy *= -0.8

        # Dibujar la partícula en pantalla
        cv2.circle(frame, (int(p.x), int(p.y)), 3, (0, 255, 255), -1)


    # ===============================
    # MOSTRAR CÁMARA
    # ===============================

    cv2.imshow("cam", frame)


    # ===============================
    # CERRAR PROGRAMA
    # ===============================

    # ESC = salir
    if cv2.waitKey(1) == 27:
        break


# ===============================
# LIBERAR RECURSOS
# ===============================

cap.release()
cv2.destroyAllWindows()