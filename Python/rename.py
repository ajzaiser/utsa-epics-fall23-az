import os

folder_path = 'C:\\Users\\ajzai\\Downloads\\New folder'  # Replace this with the actual path to your folder
new_prefix = 'allison_'  # The new prefix for the renamed files
extension = '.png'  # The file extension of your images

# Get a list of all files in the folder
file_list = os.listdir(folder_path)

# Filter the list to include only image files with the specified extension
image_files = [file for file in file_list if file.endswith(extension)]

# Sort the image files to maintain the desired order
image_files.sort()

# Rename and move the files sequentially
for index, old_name in enumerate(image_files, start=1):
    new_name = f'{new_prefix}{index:03d}{extension}'
    old_path = os.path.join(folder_path, old_name)
    new_path = os.path.join(folder_path, new_name)
    
    os.rename(old_path, new_path)
    print(f'Renamed: {old_name} -> {new_name}')

print('Renaming complete.')
