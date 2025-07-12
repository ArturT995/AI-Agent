import os
from google.genai import types

def write_file(working_directory, file_path, content):
    
    join_path = os.path.join(working_directory, file_path)
    full_path = os.path.abspath(join_path)
    dir_path = os.path.abspath(working_directory)
    
    if not full_path.startswith(dir_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    

    #write file
    try:
        if not os.path.exists(full_path):
            os.makedirs(os.path.dirname(full_path), exist_ok = True)
            

    except Exception as e:
        return f"Error:  {str(e)}"
    
    with open(full_path, "w") as f:
            file_content_string = f.write(content)

    return f'Successfully wrote to "{file_path}" wrote {content} .'



schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file within the working directory. Creates the file if it doesn't exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)