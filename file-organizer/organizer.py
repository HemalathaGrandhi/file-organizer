import os
import shutil

# Define mapping: extension -> folder name
FILE_TYPES = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".csv"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".java", ".cpp"]
}

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("❌ Folder not found!")
        return
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isdir(file_path):
            continue

        file_ext = os.path.splitext(filename)[1].lower()

        moved = False
        for folder, extensions in FILE_TYPES.items():
            if file_ext in extensions:
                folder_name = os.path.join(folder_path, folder)
                os.makedirs(folder_name, exist_ok=True)
                shutil.move(file_path, os.path.join(folder_name, filename))
                print(f"✅ Moved {filename} → {folder}/")
                moved = True
                break

        if not moved:
            other_folder = os.path.join(folder_path, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, filename))
            print(f"📦 Moved {filename} → Others/")

if __name__ == "__main__":
    folder = input("📂 Enter folder path to organize: ").strip()
    organize_files(folder)
