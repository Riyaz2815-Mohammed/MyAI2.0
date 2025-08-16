import cv2

def handle_file(file_path):
    if file_path.lower().endswith((".png", ".jpg", ".jpeg")):
        img = cv2.imread(file_path)
        cv2.imshow("Uploaded Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return "Image displayed!"
    elif file_path.lower().endswith(".txt"):
        with open(file_path, "r") as f:
            content = f.read()
        return f"Text file content:\n{content}"
    else:
        return "File type not supported."
