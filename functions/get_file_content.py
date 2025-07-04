import os

def get_file_content(working_directory, file_path):
    
    join_path = os.path.join(working_directory, file_path)
    full_path = os.path.abspath(join_path)
    dir_path = os.path.abspath(working_directory)
    
    if not full_path.startswith(dir_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    #read file and return contents
    MAX_CHARS = 10000
    try:
        with open(full_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            one_more = f.read(1)
            if one_more:
                # There was at least one more character, so the file is truly longer than MAX_CHARS
                file_content_string += f'[...File "{full_path}" truncated at {MAX_CHARS} characters]'
    except Exception as e:
        return f"Error:  {str(e)}"

    return file_content_string