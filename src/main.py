import os
from copyfilestodestination import copy_static_to_destination_directory
from generatepage import generate_pages_recursive
from pathlib import Path

def main():
    copy_static_to_destination_directory()
    root_path = Path(__file__).parent.parent
    from_path = os.path.join(root_path, 'content')
    template_path = os.path.join(root_path, 'template.html')
    dest_path = os.path.join(root_path, 'public',)
    generate_pages_recursive(from_path, template_path, dest_path)

if __name__ == "__main__":
    main()