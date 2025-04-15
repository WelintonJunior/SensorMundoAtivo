import cv2
import mediapipe as mp
import time
import json
import numpy as np
import math

# ====== CONFIGURAÇÕES ======
with open('conf.json') as f:
    LIMITES_ANGULARES = json.load(f)

ALPHA = 1.3  
BETA = 20    
SHARPEN_KERNEL = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])

# ====== MEDIA PIPE SETUP ======
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

# ====== CÂMERA ======
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

prev_time = 0

# ====== FUNÇÃO PARA CÁLCULO DE ÂNGULO ======
def calcular_angulo(a, b, c):
    ang = math.degrees(
        math.atan2(c[1] - b[1], c[0] - b[0]) -
        math.atan2(a[1] - b[1], a[0] - b[0])
    )
    ang = abs(ang)
    if ang > 180:
        ang = 360 - ang
    return ang

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.convertScaleAbs(frame, alpha=ALPHA, beta=BETA)
    frame = cv2.filter2D(frame, -1, SHARPEN_KERNEL)

    results = pose.process(rgb)
    h, w, _ = frame.shape

    if results.pose_landmarks:
        lm = results.pose_landmarks.landmark

        pontos = {}
        for idx, ponto in enumerate(lm):
            pontos[idx] = (int(ponto.x * w), int(ponto.y * h))
            cv2.circle(frame, pontos[idx], 5, (0, 255, 255), -1)
            cv2.putText(frame, str(idx), (pontos[idx][0]+5, pontos[idx][1]-5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)

        def checar_limite(nome, p1, p2, p3, cor_ok, cor_alerta):
            if all(k in pontos for k in [p1, p2, p3]):
                angulo = calcular_angulo(pontos[p1], pontos[p2], pontos[p3])
                limite = LIMITES_ANGULARES.get(nome, 999)
                cor = cor_ok if angulo <= limite else cor_alerta

                cv2.line(frame, pontos[p1], pontos[p2], cor, 3)
                cv2.line(frame, pontos[p2], pontos[p3], cor, 3)
                cv2.putText(frame, f'{nome}: {int(angulo)}',
                            (pontos[p2][0] - 30, pontos[p2][1] - 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, cor, 2)

        checar_limite("braco_direito", 11, 13, 15, (0, 255, 0), (0, 0, 255))
        checar_limite("braco_esquerdo", 12, 14, 16, (0, 255, 0), (0, 0, 255))

        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    curr_time = time.time()
    fps = 1 / (curr_time - prev_time) if prev_time else 0
    prev_time = curr_time
    cv2.putText(frame, f'FPS: {int(fps)}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 255, 100), 2)

    cv2.imshow("Exoesqueleto Humano", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
