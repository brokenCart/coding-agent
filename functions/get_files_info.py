import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working_dir, directory))

        if not os.path.commonpath([abs_working_dir, target_dir]) == abs_working_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        files_info = []
        for entry in os.listdir(target_dir):
            entry_path = os.path.join(target_dir, entry)
            entry_str = f"- {entry}: file_size={os.path.getsize(entry_path)} bytes, is_dir={os.path.isdir(entry_path)}"
            files_info.append(entry_str)
        return "\n".join(files_info)
    except Exception as e:
        return f"Error: {e}"
