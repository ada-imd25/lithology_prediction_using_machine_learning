import lasio
import numpy as np
from pathlib import Path

# function to remove spaces in file name in a given folder
from pathlib import Path

# 1. Function to remove spaces in file names in a given folder
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

# 2. Function to merge 2 las files into one (LAS in litho_label with LAS in wireline)
def merge_las_by_depth(las1_path, las2_path, output_path):
    las1 = lasio.read(str(las1_path))
    las2 = lasio.read(str(las2_path))

    df1 = las1.df()               # depth index
    df2 = las2.df()               # depth index
    merged_df = df1.join(df2, how="inner")  # keep common depths only (safe)

    merged_las = lasio.LASFile()
    depth = merged_df.index.values
    merged_las.add_curve("DEPT", depth, unit=las1.index_curve.unit)

    for col in merged_df.columns:
        merged_las.add_curve(col, merged_df[col].values)

    merged_las.write(str(output_path))

# 3. Function to merge las files loop 

def batch_merge(wireline_dir="data/wireline",
                litho_dir="data/litho_label",
                out_dir="data/merged"):

    wireline_dir = Path(wireline_dir)
    litho_dir = Path(litho_dir)
    out_dir = Path(out_dir)
    out_dir.mkdir(exist_ok=True)

    for wl_file in wireline_dir.glob("*.las"):
        litho_file = litho_dir / wl_file.name

        if litho_file.exists():
            las1 = lasio.read(wl_file)
            las2 = lasio.read(litho_file)

            df = las1.df().join(las2.df(), how="inner")

            merged = lasio.LASFile()
            merged.add_curve("DEPT", df.index.values, unit=las1.index_curve.unit)

            for col in df.columns:
                merged.add_curve(col, df[col].values)

            merged.write(out_dir / wl_file.name)
            print(f"Merged: {wl_file.name}")

    print("Done.")