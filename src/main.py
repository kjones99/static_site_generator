import os
import sys
from copyfilestodestination import copy_static_to_destination_directory
from generatepage import generate_pages_recursive
from pathlib import Path

def main():

    base_path = '/' 
    if len(sys.argv) > 1:
        base_path = sys.argv[1]

    copy_static_to_destination_directory()

    root_path = Path(__file__).parent.parent
    from_path = os.path.join(root_path, 'content')
    template_path = os.path.join(root_path, 'template.html')
    dest_path = os.path.join(root_path, 'docs',)

    generate_pages_recursive(from_path, template_path, dest_path, base_path)

if __name__ == "__main__":
    main()