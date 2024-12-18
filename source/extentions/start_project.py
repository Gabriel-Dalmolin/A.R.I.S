import subprocess
import os 

def handle_project_inicialization(file_language, month_and_year):
    if file_language == "python":
        folder_path = "C:\\Users\\gabid\\.vscode\\Python\\" + month_and_year
        os.makedirs(folder_path, exist_ok=True)
        subprocess.run("code " + folder_path, shell=True)  

    elif file_language == "c++":
        folder_path = "C:\\Users\\gabid\\.vscode\\C++\\" + month_and_year
        os.makedirs(folder_path, exist_ok=True)
        subprocess.run("code " + folder_path, shell=True)  
        
    elif file_language == "java":
        folder_path = "C:\\Users\\gabid\\JavaProjects\\" + month_and_year
        intelliJ_path = '"C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2024.3\\bin\\idea64.exe"'
        os.makedirs(folder_path, exist_ok=True)
        subprocess.run(intelliJ_path + " " + folder_path, shell=True) 
    
    