import sys
from datetime import datetime
from extentions.start_project import handle_project_inicialization

def get_month_and_year():
    now = datetime.now()
    return f"{now.year}_{now.month}"

if __name__ == "__main__":
    command = sys.argv[1].strip()
    if command == "start_project":
        file_language = sys.argv[2].strip()
        handle_project_inicialization(file_language, get_month_and_year())

    else:   
        print("command not recognized") 
                
            
