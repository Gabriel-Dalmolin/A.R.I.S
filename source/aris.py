import sys
from datetime import datetime
from extentions.start_project import handle_project_inicialization
from extentions.open_tkinter_designer import open_tkinter_designer
from extentions.speech_handler import listen

def get_month_and_year():
    now = datetime.now()
    return f"{now.year}_{now.month}"

if __name__ == "__main__":
    command = listen()

    if "project" in command or "projects" in command:
        file_language = None
        if "python" in command:
            file_language = "python"
        elif "java" in command:
            file_language = "java"
        elif "c++":
            file_language = "c++"
        if file_language:
            handle_project_inicialization(file_language, get_month_and_year())
    
    elif "designer" in command:
        open_tkinter_designer()

    else:   
        print("command not recognized") 
        print(command)
                
            
