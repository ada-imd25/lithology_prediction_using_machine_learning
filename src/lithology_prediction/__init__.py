#__init__.py

from .preprocess import remove_spaces

__all__ = [
    "remove_spaces",
    "merge_las_by_depth",
    "batch_merge",
]

__version__ = "0.1.0"