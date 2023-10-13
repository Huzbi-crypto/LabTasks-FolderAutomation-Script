import os
import shutil

lab_number = input("Enter your lab number: ")

lab_folder_name = f"Lab-{lab_number.zfill(2)}"

os.makedirs(lab_folder_name, exist_ok=True)

copy_lab_setup = "F:\Huzbi's Folder\FAST NU\Fall 2023\Courses\COAL\Lab\COAL-BasicSetup"

shutil.copytree(copy_lab_setup, os.path.join(lab_folder_name, os.path.basename(copy_lab_setup)), dirs_exist_ok=True)

print(f"Directory {lab_folder_name} created and setup from {copy_lab_setup} also done!")

input("Press a key to exit...")