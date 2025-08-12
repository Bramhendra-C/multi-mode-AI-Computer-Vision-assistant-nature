import cv2
import speech_recognition as sr 
import pyttsx3

engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():                                                     # Function to take voice command from the user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("..",end=" ")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("..",end=" ")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except Exception:
        print("Sorry, I didn't catch that.")
        return "None"
    return query.lower()

def face():                                                                #Face detection mode
    face_data = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    webcam = cv2.VideoCapture(0)

    while True:
        success, frame = webcam.read()
        if not success:
            break

        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_co = face_data.detectMultiScale(gray_img, scaleFactor=1.5, minNeighbors=5)

        thumb_size = (150, 150)

        if len(face_co) > 0:
            (x, y, w, h) = face_co[0]
            face_roi = frame[y:y+h, x:x+w]
            thumbnail = cv2.resize(face_roi, thumb_size)
            border_color = (0, 255, 0)
            label = "FOCUSED"
            label_color = (0, 255, 0)
        else:
            blurred = cv2.GaussianBlur(frame, (55, 55), 0)
            thumbnail = cv2.resize(blurred, thumb_size)
            border_color = (0, 0, 255) 
            label = "UNFOCUSED"
            label_color = (0, 0, 255)
        thumbnail_with_border = cv2.copyMakeBorder(
            thumbnail, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=border_color
        )
        cv2.putText(thumbnail_with_border, label, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, label_color, 2)

        h_thumb, w_thumb, _ = thumbnail_with_border.shape
        x_offset = frame.shape[1] - w_thumb - 10
        y_offset = 10
        frame[y_offset:y_offset+h_thumb, x_offset:x_offset+w_thumb] = thumbnail_with_border

        cv2.imshow('Face Detection - bramii', frame)
        query = take_command()
        if query.lower() == 'exit' or query.lower() == 'stop':
            speak("Exiting face detection mode.")
            break