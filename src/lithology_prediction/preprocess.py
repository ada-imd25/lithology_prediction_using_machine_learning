import lasio
import numpy as np
from pathlib import Path


def merge_wireline_and_lithology_las(
    wireline_las_path: Path,
    litho_las_path: Path,
    output_path: Path,
    litho_curve_name: str,
    litho_unit: str = "unitless",
    litho_description: str = "Lithology label"
):
    """
    Merge wireline log LAS with lithology/facies LAS.

    Parameters
    ----------
    wireline_las_path : Path
        Path to wireline LAS file
    litho_las_path : Path
        Path to lithology/facies LAS file
    output_path : Path
        Path to save merged LAS
    litho_curve_name : str
        Curve name in lithology LAS (e.g. 'FACIES', 'LITHO')
    """

    # Load LAS files
    wireline = lasio.read(wireline_las_path)
    litho = lasio.read(litho_las_path)

    # Extract depth
    depth_wire = wireline.index
    depth_litho = litho.index

    # Safety check (very important in real data)
    if not np.allclose(depth_wire, depth_litho):
        raise ValueError(
            f"Depth mismatch between {wireline_las_path.name} "
            f"and {litho_las_path.name}"
        )

    # Extract lithology curve
    litho_data = litho[litho_curve_name]

    # Append lithology curve to wireline LAS
    wireline.append_curve(
        litho_curve_name,
        litho_data,
        unit=litho_unit,
        descr=litho_description
    )

    # Save merged LAS
    output_path.parent.mkdir(parents=True, exist_ok=True)
    wireline.write(output_path)

    print(f"Merged LAS saved: {output_path.name}")
