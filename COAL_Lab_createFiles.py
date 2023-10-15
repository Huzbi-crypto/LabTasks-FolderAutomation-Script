import os
import shutil

# create the lab structure
lab_number = input("Enter your lab number: ")
result_folder = "Result"

lab_folder_name = f"Lab-{lab_number.zfill(2)}"
result_folder_name = os.path.join(lab_folder_name, result_folder)

os.makedirs(result_folder_name, exist_ok=True)

copy_lab_setup = "path/to/your/folder/for/basicsetup"
shutil.copytree(copy_lab_setup, os.path.join(lab_folder_name, os.path.basename(copy_lab_setup)), dirs_exist_ok=True)

print(f"Directory {lab_folder_name} created and setup from {copy_lab_setup} also done!")

input("Press a key to exit...")
