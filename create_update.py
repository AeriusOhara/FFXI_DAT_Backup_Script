import os
import time
import shutil

def checkFolderExists(path):
	# Create the folder if it doesn't exist
	if not (os.path.exists(path)):
		os.makedirs(path)

# Final Fantasy XI directory
ffxi_directory = "C:\\Program Files (x86)\\PlayOnline\\SquareEnix\\Final Fantasy XI"

newfile_timestamp = time.mktime(time.strptime('2019-04-27 00:00:00', '%Y-%m-%d %H:%M:%S'))
work_directory = os.getcwd()
file_list = []
dir_list = []
dir_list.append("")

# Build the file and directory list
for directory in dir_list:
    for entry in os.listdir(f"{ffxi_directory}\\{directory}"):
        entry_path = f"{directory}\\{entry}"
        full_entry_path = f"{ffxi_directory}\\{directory}\\{entry}"

        if(os.path.isdir(full_entry_path)):
            # Don't back up the user folder, or the log files
            if(entry_path != "\\USER" and entry_path != "\\TEMP"):
                print(f"Adding directory: {entry_path}")
                dir_list.append(f"{entry_path}")
        else:
            if(directory != ""):
                # Don't touch the root files
                file_list.append([directory, entry])

# Process file list and copy over the files that are newer than the setup installs
for file in file_list:
    file_timestamp = os.path.getmtime(f"{ffxi_directory}\\{file[0]}\\{file[1]}")
    if(file_timestamp > newfile_timestamp):
        print(f"Backing up [{file[0]}\\{file[1]}]")
        
        checkFolderExists(f"{work_directory}\\BACKUP\\{file[0]}")
        shutil.copy2(f"{ffxi_directory}\\{file[0]}\\{file[1]}", f"{work_directory}\\BACKUP\\{file[0]}\\{file[1]}")
