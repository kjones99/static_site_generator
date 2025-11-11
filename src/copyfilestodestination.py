import os
import shutil
from pathlib import Path


def copy_static_to_destination_directory():
    #get the root directory of the project then create the path to public and static folders from that
    root_directory = Path(__file__).parent.parent
    target_directory = os.path.join(root_directory, 'docs')
    source_directory = os.path.join(root_directory, 'static')
    
    os.makedirs(target_directory, exist_ok=True)
    #loop through contents of the public directory and delete them
    for item in os.listdir(target_directory):
        current_path = os.path.join(target_directory, item)
        if os.path.isfile(current_path):
            os.remove(current_path)
            continue
        shutil.rmtree(current_path)
    
    recursive_copy(target_directory, source_directory)
    
def recursive_copy(target, source):
    for item in os.listdir(source):
        curr_path = os.path.join(source, item)
        if os.path.isfile(curr_path):
            shutil.copy(curr_path, target)
            continue
        else:
            new_target = os.path.join(target, item)
            new_source = os.path.join(source, item)
            os.mkdir(new_target)
            recursive_copy(new_target, new_source)