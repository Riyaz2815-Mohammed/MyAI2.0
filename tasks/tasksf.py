import webbrowser
import os
import cv2

def open_chrome():
    webbrowser.open("https://www.google.com")
    return "Opened Chrome for you! 😎"

def open_youtube():
    webbrowser.open("https://www.youtube.com")
    return "YouTube open panniduren! 😏"

def open_whatsapp():
    webbrowser.open("https://web.whatsapp.com")
    return "WhatsApp Web ready da! 😎"

def open_notes():
    os.system("notepad")
    return "Notes open panniduren! 📝"

def open_camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return "Cannot access the camera"
    print("Press 'q' to quit camera")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    return "Camera closed"

def calculate(expression: str):
    try:
        allowed_chars = "0123456789+-*/(). "
        if any(c not in allowed_chars for c in expression):
            return "Invalid characters in expression"
        result = eval(expression)
        return f"The result is {result}"
    except Exception as e:
        return f"Error: {e}"
