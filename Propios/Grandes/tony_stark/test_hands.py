# ============================================
# IMPORTAR LIBRERÍAS NECESARIAS
# ============================================

import cv2                     # Librería para cámara, ventanas y dibujo
import mediapipe as mp         # Librería de visión artificial
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import random                  # Para generar posiciones aleatorias
import time                    # Para timestamps del detector
import math                    # Para cálculos matemáticos (distancia, ángulos)


# ============================================
# CONFIGURAR EL MODELO DE DETECCIÓN DE MANOS
# ============================================

# Ruta al modelo que detecta manos
model_path = r"E:\Codigos\Propios\Grandes\tony_stark\hand_landmarker.task"

# Opciones base del modelo
base_options = python.BaseOptions(model_asset_path=model_path)

# Configuración del detector
options = vision.HandLandmarkerOptions(

    base_options=base_options,             # usar el modelo especificado
    running_mode=vision.RunningMode.VIDEO, # modo optimizado para video en tiempo real
    num_hands=2                            # máximo número de manos a detectar

)

# Crear el detector de manos
detector = vision.HandLandmarker.create_from_options(options)


# ============================================
# CLASE PARTÍCULA
# ============================================

# Cada objeto Particle representa una partícula individual en pantalla
class Particle:

    def __init__(self, x, y):

        # Posición inicial de la partícula
        self.x = x
        self.y = y

        # Velocidad inicial aleatoria pequeña
        # Esto evita que todas empiecen completamente quietas
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)

    def update(self):

        # Actualizar posición según la velocidad
        self.x += self.vx
        self.y += self.vy


# ============================================
# ACTIVAR LA CÁMARA
# ============================================

# 0 = cámara principal del computador
cap = cv2.VideoCapture(0)


# ============================================
# CREAR PARTÍCULAS
# ============================================

# Cantidad total de partículas en pantalla
NUM_PARTICLES = 500

# Lista donde se almacenarán todas las partículas
particles = []

# Crear partículas en posiciones aleatorias
for i in range(NUM_PARTICLES):

    # posición aleatoria inicial
    x = random.randint(0, 1280)
    y = random.randint(0, 720)

    # añadir partícula a la lista
    particles.append(Particle(x, y))


# ============================================
# CONFIGURAR VENTANA EN PANTALLA COMPLETA
# ============================================

cv2.namedWindow("cam", cv2.WINDOW_NORMAL)

# Cambiar propiedad de la ventana para que sea fullscreen
cv2.setWindowProperty(
    "cam",
    cv2.WND_PROP_FULLSCREEN,
    cv2.WINDOW_FULLSCREEN
)


# ============================================
# BUCLE PRINCIPAL DEL PROGRAMA
# ============================================

while True:

    # Capturar un frame de la cámara
    ret, frame = cap.read()

    # Si falla la captura, salir
    if not ret:
        break

    # Voltear la imagen horizontalmente
    # Esto hace que la cámara funcione como espejo
    frame = cv2.flip(frame, 1)

    # Obtener dimensiones del frame
    height, width = frame.shape[:2]


    # ============================================
    # DETECTAR MANOS EN EL FRAME
    # ============================================

    # Convertir frame a formato que usa mediapipe
    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=frame
    )

    # Timestamp necesario para el modo VIDEO
    timestamp = int(time.time()*1000)

    # Ejecutar detección de manos
    result = detector.detect_for_video(mp_image, timestamp)


    # Variables que guardarán el estado del gesto
    gesture = None
    hand_x = None
    hand_y = None


    # ============================================
    # ANALIZAR GESTOS DE LA MANO
    # ============================================

    if result.hand_landmarks:

        # Tomar la primera mano detectada
        hand = result.hand_landmarks[0]

                # ============================================
        # CALCULAR TAMAÑO DE LA PALMA
        # ============================================

        # base del dedo índice
        palm_left = hand[5]

        # base del meñique
        palm_right = hand[17]

        # convertir a coordenadas de pantalla
        px1 = palm_left.x * width
        py1 = palm_left.y * height

        px2 = palm_right.x * width
        py2 = palm_right.y * height

        # distancia entre los dos puntos = tamaño de la palma
        palm_size = math.sqrt((px2 - px1)**2 + (py2 - py1)**2)


        # Punto central aproximado de la mano (landmark 9)
        palm = hand[9]

        # Convertir coordenadas normalizadas a píxeles
        hand_x = int(palm.x * width)
        hand_y = int(palm.y * height)

        # Determinar si cada dedo está abierto
        index_open = hand[8].y < hand[6].y
        middle_open = hand[12].y < hand[10].y
        ring_open = hand[16].y < hand[14].y
        pinky_open = hand[20].y < hand[18].y

        # Contar dedos abiertos
        open_fingers = sum([index_open, middle_open, ring_open, pinky_open])

        # Clasificar gesto
        if open_fingers >= 3:
            gesture = "open"

        elif open_fingers == 0:
            gesture = "fist"

        elif index_open and open_fingers == 1:
            gesture = "index"


    # ============================================
    # ACTUALIZAR TODAS LAS PARTÍCULAS
    # ============================================

    for i, p in enumerate(particles):


        # ============================================
        # GESTO: MANO ABIERTA
        # formar círculo alrededor de la mano
        # ============================================

        if gesture == "open":

            # radio proporcional al tamaño de la mano
            radius = palm_size * 1.2

            # calcular posición objetivo dentro del círculo
            angle = (i / NUM_PARTICLES) * 2 * math.pi

            target_x = hand_x + math.cos(angle) * radius
            target_y = hand_y + math.sin(angle) * radius

            # vector hacia el objetivo
            dx = target_x - p.x
            dy = target_y - p.y

            # aplicar fuerza de atracción
            p.vx += dx * 0.05
            p.vy += dy * 0.05


        # ============================================
        # GESTO: PUÑO
        # repulsión desde la mano
        # ============================================

        elif gesture == "fist":

            # radio máximo de repulsión
            # radio proporcional al tamaño de la mano
            radius = palm_size * 2

            dx = p.x - hand_x
            dy = p.y - hand_y

            dist = math.sqrt(dx*dx + dy*dy)

            # solo aplicar fuerza si está dentro del radio
            if dist < radius and dist > 0:

                # la fuerza disminuye cuanto más lejos esté
                force = (radius - dist) / radius

                p.vx += (dx/dist) * force * 8
                p.vy += (dy/dist) * force * 8


        # ============================================
        # GESTO: SOLO ÍNDICE
        # frenar partículas
        # ============================================

        elif gesture == "index":

            p.vx *= 0.3
            p.vy *= 0.3


        # ============================================
        # FRICCIÓN GENERAL
        # evita que las partículas aceleren infinitamente
        # ============================================

        p.vx *= 0.98
        p.vy *= 0.98

        # pequeña variación aleatoria para evitar sincronización
        if gesture != "index":
            p.vx += random.uniform(-0.1, 0.1)
            p.vy += random.uniform(-0.1, 0.1)


        # ============================================
        # LIMITAR VELOCIDAD MÁXIMA
        # ============================================

        max_speed = 10

        speed = math.sqrt(p.vx*p.vx + p.vy*p.vy)

        if speed > max_speed:

            scale = max_speed / speed

            p.vx *= scale
            p.vy *= scale


        # ============================================
        # ACTUALIZAR POSICIÓN
        # ============================================

        # repulsión entre partículas cercanas
        for other in particles[::3]:

            if other is p:
                continue

            dx = p.x - other.x
            dy = p.y - other.y

            dist_sq = dx*dx + dy*dy

            if dist_sq < 100 and dist_sq > 0:

                dist = math.sqrt(dist_sq)

                force = (10 - dist) * 0.05

                p.vx += (dx/dist) * force
                p.vy += (dy/dist) * force

        # Actualizar posicion
        p.update()


        # ============================================
        # COLISIÓN CON BORDES DE PANTALLA
        # ============================================

        if p.x < 0:
            p.x = 0
            p.vx *= -0.7

        if p.x > width:
            p.x = width
            p.vx *= -0.7

        if p.y < 0:
            p.y = 0
            p.vy *= -0.7

        if p.y > height:
            p.y = height
            p.vy *= -0.7


        # ============================================
        # DIBUJAR PARTÍCULA
        # ============================================

        cv2.circle(

            frame,

            (int(p.x), int(p.y)),   # posición

            1,                      # tamaño pequeño

            (255, 120, 0),          # color azul (BGR)

            -1                      # círculo relleno
        )


    # ============================================
    # MOSTRAR FRAME EN PANTALLA
    # ============================================

    cv2.imshow("cam", frame)

    # salir al presionar ESC
    if cv2.waitKey(1) == 27:
        break


# ============================================
# LIBERAR RECURSOS AL TERMINAR
# ============================================

cap.release()
cv2.destroyAllWindows()