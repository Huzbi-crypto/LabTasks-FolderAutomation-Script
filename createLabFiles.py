import os

# Define the name of the directory to be created
dir_name = "Lab-0"
sub_dir_name = "source-codes"

# Create target Directory
path = os.path.join(dir_name, sub_dir_name)
os.makedirs(path, exist_ok=True)

print("Directory ", dir_name, "/", sub_dir_name, " Created ")

# Ask user for number of files to create
num_files = int(input("Enter the number of .cpp files to create: "))

# Create .cpp files
for i in range(num_files):
    file_name = f"q{i+1}.cpp"
    open(os.path.join(path, file_name), 'w').close()
    print(f"{file_name} created")

print("All files created")
