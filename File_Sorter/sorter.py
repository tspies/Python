import os
import shutil

base_path = "/Users/tristyn/"
search_path = "/Users/tristyn/Downloads/"

extentions = {
	'.jpg' : "Downloads/Images/",
	'.jpeg': "Downloads/Images/",
	'.zip' : "Downloads/CompressedFiles/",
	'.dmg' : "Downloads/CompressedFiles/",
	'.exe' : "Downloads/Executables/",
	'.png' : "Downloads/Images/",
	'.mp3' : "Downloads/Music/",
	'.pdf' : "Documents/pdfs/",
	'.docx': "Documents/docs/",
	'.xlsx': "Documents/sheets/"
}

def sort(extention, folder_name):
	file_list = os.listdir(search_path)
	if not os.path.exists(base_path + folder_name):
		os.makedirs(base_path + folder_name)
	for file in file_list:
		if file.lower().endswith(extention):
			shutil.move(search_path + file, base_path + folder_name + file)

for key, value in extentions.items():
	sort(key, value)