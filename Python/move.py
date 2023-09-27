import os
import shutil

source_folder = 'C:\\Users\\ajzai\\Downloads\\New folder'  # Replace with the source folder path
prefix = 'allison_'
extension = '.png'

# Get a list of all files in the source folder
file_list = os.listdir(source_folder)

# Filter the list to include only image files with the specified extension and prefix
image_files = [file for file in file_list if file.startswith(prefix) and file.endswith(extension)]

# Sort the image files to maintain the desired order
image_files.sort()

# Create destination folders if they don't exist
for i in range(5):
    folder_name = f'folder_{i + 1}'
    folder_path = os.path.join(source_folder, folder_name)
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Organize images into destination folders
folder_counter = 1
images_per_folder = len(image_files) // 5

for index, image_file in enumerate(image_files, start=1):
    source_path = os.path.join(source_folder, image_file)
    destination_folder = f'folder_{folder_counter}'
    destination_path = os.path.join(source_folder, destination_folder, image_file)
    
    shutil.move(source_path, destination_path)
    print(f'Moved: {image_file} to {destination_folder}')
    
    if index % images_per_folder == 0:
        folder_counter += 1

print('Image organization complete.')
