# import cv2
# import mediapipe as mp
#
# # Настройка MediaPipe
# mp_hands = mp.solutions.hands
# hands = mp_hands.Hands(static_image_mode=False,
#                        max_num_hands=1,
#                        min_detection_confidence=0.7,
#                        min_tracking_confidence=0.7)
# mp_draw = mp.solutions.drawing_utils
#
# # Пальцы: [большой, указательный, средний, безымянный, мизинец]
# finger_tips = [4, 8, 12, 16, 20]
#
# # Захват с веб-камеры
# cap = cv2.VideoCapture(0)
#
# while True:
#     success, img = cap.read()
#     img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     results = hands.process(img_rgb)
#
#     fingers_up = []
#
#     if results.multi_hand_landmarks:
#         for hand_landmarks in results.multi_hand_landmarks:
#             lm_list = []
#             for id, lm in enumerate(hand_landmarks.landmark):
#                 h, w, _ = img.shape
#                 lm_list.append((int(lm.x * w), int(lm.y * h)))
#
#             # Определяем поднятые пальцы
#             if lm_list:
#                 # Большой палец — по оси X
#                 if lm_list[4][0] > lm_list[3][0]:
#                     fingers_up.append(1)
#                 else:
#                     fingers_up.append(0)
#
#                 # Остальные пальцы — по оси Y
#                 for tip in finger_tips[1:]:
#                     if lm_list[tip][1] < lm_list[tip - 2][1]:
#                         fingers_up.append(1)
#                     else:
#                         fingers_up.append(0)
#
#                 total_fingers = sum(fingers_up)
#
#                 if total_fingers == 0:
#                     gesture = "Кулак"
#                 else:
#                     gesture = str(total_fingers)
#
#                 cv2.putText(img, f"Жест: {gesture}", (10, 50),
#                             cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)
#
#             # Рисуем скелет руки
#             mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
#
#     cv2.imshow("Распознавание жестов", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


import turtle
pen = turtle.Turtle()
pen.speed(3)
pen.color("red")
pen.begin_fill()
pen.left(140)
pen.forward(180)
pen.circle(-90, 200)
pen.left(120)
pen.circle(-90, 200)
pen.forward(180)
pen.end_fill()
pen.hideturtle()
pen.up()
pen.goto(-50, 50)
pen.color("white")
pen.write("", font=("Arial", 24, "bold"))
turtle.done()