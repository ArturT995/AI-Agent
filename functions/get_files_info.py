import os

def get_files_info(working_directory, directory=None):
    
    joined_path = os.path.join(working_directory, directory)
    full_path = os.path.abspath(joined_path)
    dir_path = os.path.abspath(working_directory)
    
    if not full_path.startswith(dir_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    
    #contents
    try:
        directory_contents = os.listdir(full_path)  #list
        lines = []
        for file in directory_contents:
            #item_path is essentially a workaround for os.path stuff because I gotta put a path in them.
            item_path = os.path.join(full_path, file) 
            file_size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            lines.append(f"- {file}: file_size={file_size} bytes, is_dir={is_dir}")
    except Exception as e:
        return f"Error: {str(e)}"

    return "\n".join(lines)
    