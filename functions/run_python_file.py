import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    
    join_path = os.path.join(working_directory, file_path)
    full_path = os.path.abspath(join_path)
    dir_path = os.path.abspath(working_directory)
    
    if not full_path.startswith(dir_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        commands = ["python", file_path]
        if args:
            commands.extend(args)
        
        result = subprocess.run(commands, cwd=working_directory,
        capture_output=True, text=True, timeout=30
        )
        #subprocess.run(..capture_output=True..) returns CompletedProcess, and is assigned to result variable.
        
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")

        code = result.returncode
        if result.returncode != 0:
            output += f"\nProcess exited with code {code}"
        
        return "\n".join(output) if output else "No output produced."
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
    return output

    
