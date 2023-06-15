import pandas as pd
import os
import shutil

dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)

block = [['A1','B1','A2','B2']]
n_blocks = 18

trial_sequence = block * n_blocks

maps_per_block = 3

condition_file = pd.DataFrame()
trial_dfs = []



for i in range(int(n_blocks/maps_per_block)):
    for trial in trial_sequence[i]:
        tmt= trial[0]
        half = trial[1]
        iteration = i+1
        image_folder = f"TMT{tmt}_images"
        for j in range(maps_per_block):
            trial_df = pd.read_csv(fr"{dir}\{image_folder}\num_{iteration+j}\TMT-stop-{tmt}_{iteration+j}_{half}.csv", sep= ";")
            trial_dfs.append(trial_df)
        

#Move all images


source_dir1 = f"{dir}\TMTA_images"  # Replace with the actual path of the first source directory
source_dir2 = f"{dir}\TMTB_images"   # Replace with the actual path of the second source directory
destination_dir = f"{dir}\TMT_fmri_shorter\Images"   # Replace with the actual path of the destination directory

# Source folders
tmta_folder = 'TMTA_images'
tmtb_folder = 'TMTB_images'

# Destination folder
destination_folder = 'TMT_fmri_shorter/Images'

# Create the destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Process TMTA_images folder
for root, _, files in os.walk(tmta_folder):
    for file in files:
        # Check if the file is an image
        if file.endswith(('.jpg', '.jpeg', '.png')):
            source_path = os.path.join(root, file)
            destination_path = os.path.join(destination_folder, file)
            shutil.copy(source_path, destination_path)

# Process TMTB_images folder
for root, _, files in os.walk(tmtb_folder):
    for file in files:
        # Check if the file is an image
        if file.endswith(('.jpg', '.jpeg', '.png')):
            source_path = os.path.join(root, file)
            destination_path = os.path.join(destination_folder, file)
            shutil.copy(source_path, destination_path)

print('Images copied successfully.')


condition_file = pd.concat(trial_dfs)

condition_file.to_excel("TMT_fmri_shorter\Only_TMTA_TMTB.xlsx", index = False)