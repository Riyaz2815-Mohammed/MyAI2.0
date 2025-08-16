import tasksf as tasks  

def perform_task(command: str):
    command = command.lower()
    if "chrome" in command:
        return tasks.open_chrome()
    elif "youtube" in command:
        return tasks.open_youtube()
    elif "whatsapp" in command:
        return tasks.open_whatsapp()
    elif "notes" in command:
        return tasks.open_notes()
    elif "camera" in command:
        return tasks.open_camera()
    elif "calculate" in command:
        expression = command.replace("calculate", "").strip()
        return tasks.calculate(expression)
    else:
        return None
