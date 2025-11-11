import os
from markdownconverting import markdown_to_html_node, extract_title
from pathlib import Path

def generate_page(from_path, template_path, dest_path, base_path):
    #read markdown text from the file at from_path
    try:
        with open(from_path, 'r') as file:
            markdown = file.read()
    except FileNotFoundError:
        print(f'Error: The file "{from_path}" was not found')

    #read template html code from file at template_path
    try:
        with open(template_path, 'r') as file:
            template = file.read()
    except FileNotFoundError:
        print(f'Error: The file "{template_path}" was not found')

    #convert the markdown text from the file at from_path and convert it to an HTML string and then extract the h1 heading title
    page_html_node = markdown_to_html_node(markdown)
    page_html_string = page_html_node.to_html()
    page_title = extract_title(markdown)

    #replace title and content placeholders in template with the page_title and html_string we got above
    template = template.replace('{{ Title }}', page_title)
    template = template.replace('{{ Content }}', page_html_string)
    #template = template.replace('href="/', f'href="{base_path}')
    #template = template.replace('src="/', f'src="{base_path}')

    #Try and create the destination parent directory, if it already exists do nothing
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    with open(dest_path, 'w') as file:
        file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path):
    #loop through items at the current source directory and check if they are files or subdirectories
    for item in os.listdir(dir_path_content):
        curr_source_path = Path(dir_path_content) / item
        curr_dest_path = Path(dest_dir_path) / item
        #if you find markdown file call the generate page function with appropriate paths
        #if its any other kind of file just move onto the next item in the directory
        if curr_source_path.is_file():
            if curr_source_path.suffix != '.md':
                continue
            generate_page(curr_source_path, template_path, curr_dest_path.with_suffix('.html'), base_path)
        #if you find a directory recursively call this function on that directory also updating the dest_path
        else:
            generate_pages_recursive(curr_source_path, template_path, curr_dest_path, base_path)
            