
import cv2
import json
import random
from quiz_logic import Quiz
from head_tracker import HeadTracker
from playsound import playsound
import threading

def play_sound(path):
    threading.Thread(target=playsound, args=(path,), daemon=True).start()

def draw_button(frame, text, center, size=(200, 70), color=(0, 140, 255)):
    x, y = center
    w, h = size
    top_left = (x - w // 2, y - h // 2)
    bottom_right = (x + w // 2, y + h // 2)
    cv2.rectangle(frame, top_left, bottom_right, color, -1, cv2.LINE_AA)

    # Potong teks jika terlalu panjang
    max_width = 160
    text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_DUPLEX, 0.6, 1)[0]
    while text_size[0] > max_width:
        text = text[:-1]
        text_size = cv2.getTextSize(text + "...", cv2.FONT_HERSHEY_DUPLEX, 0.6, 1)[0]
        if len(text) <= 4:
            break
    if text_size[0] > max_width:
        text = text[:10] + "..."
    cv2.putText(frame, text + ("..." if text_size[0] > max_width else ""), (x - w // 2 + 10, y + 5),
                cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 0, 0), 1)

def draw_informatics_frame(frame):
    # Tambahkan border neon hijau + kotak sudut
    color = (0, 255, 0)
    thickness = 2
    h, w = frame.shape[:2]
    cv2.rectangle(frame, (10, 10), (w - 10, h - 10), color, thickness)

    # Tambahkan kotak sudut (terminal style)
    corner_size = 25
    for x in [10, w - 10 - corner_size]:
        for y in [10, h - 10 - corner_size]:
            cv2.rectangle(frame, (x, y), (x + corner_size, y + corner_size), color, 1)

def main():
    with open("assets/soal.json", "r") as f:
        questions = json.load(f)

    quiz = Quiz(questions)
    tracker = HeadTracker()

    cap = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX

    while quiz.has_next_question() and cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        frame = cv2.resize(frame, (480, 854))  # Portrait TikTok-style

        question = quiz.current_question()

        # Bubble pertanyaan
        overlay = frame.copy()
        cv2.rectangle(overlay, (20, 40), (460, 160), (10, 50, 90), -1, cv2.LINE_AA)
        alpha = 0.7
        frame = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)

        # Teks pertanyaan
        cv2.putText(frame, question['question'], (30, 100), font, 0.75, (0, 255, 0), 2)

        # Tombol jawaban
        draw_button(frame, f"A: {question['option_a']}", center=(140, 640), color=(0, 200, 255))
        draw_button(frame, f"B: {question['option_b']}", center=(340, 640), color=(0, 255, 100))

        # Tambahkan frame digital
        draw_informatics_frame(frame)

        direction = tracker.detect_direction(frame)

        if direction:
            answer = "A" if direction == "left" else "B"
            quiz.answer_current_question(answer)
            sound = "assets/sound_correct.mp3" if answer == question["answer"] else "assets/sound_wrong.mp3"
            play_sound(sound)
            quiz.next_question()
            continue

        cv2.imshow("Seberapa IF Kamu? [Informatics Frame]", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"Skor Akhir Anda: {quiz.score} / {len(questions)}")

if __name__ == "__main__":
    main()
