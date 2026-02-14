import lasio
import numpy as np
from pathlib import Path

# function to remove spaces in file name in a given folder
from pathlib import Path

def remove_spaces(folder_path: str) -> int:
    folder = Path(folder_path)
    renamed = 0

    for file in folder.iterdir():
        if file.is_file() and " " in file.name:
            new_path = file.with_name(file.name.replace(" ", ""))
            if new_path.exists():
                raise FileExistsError(f"Target exists: {new_path}")
            file.rename(new_path)
            renamed += 1

    return renamed

