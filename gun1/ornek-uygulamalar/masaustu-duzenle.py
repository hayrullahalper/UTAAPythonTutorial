import os
import shutil

# Hedef dizin
folder_path = "C:/Users/YourUsername/Desktop"

# Dosya türlerine göre klasörler oluştur
file_types = {
    "Resimler": [".jpg", ".png", ".jpeg", ".gif"],
    "Belgeler": [".pdf", ".docx", ".txt"],
    "Videolar": [".mp4", ".mkv", ".avi"]
}

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        for folder, extensions in file_types.items():
            if file.endswith(tuple(extensions)):
                folder_path_new = os.path.join(folder_path, folder)
                os.makedirs(folder_path_new, exist_ok=True)
                shutil.move(file_path, folder_path_new)
                print(f"{file} taşındı -> {folder}")