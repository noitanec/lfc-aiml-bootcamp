import shutil
from pathlib import Path

import kagglehub


def download_dataset(handle: str, output_dir: str | None = None) -> Path:
    """Download a Kaggle dataset using kagglehub.

    Args:
        handle: Kaggle dataset handle in the form 'owner/dataset-name'.
        output_dir: Directory to copy the downloaded files into.
                    Defaults to 'data/' relative to the current working directory.

    Returns:
        Path to the directory containing the downloaded files.
    """
    dest = Path(output_dir) if output_dir else Path("data")
    dest.mkdir(parents=True, exist_ok=True)

    cached_path = Path(kagglehub.dataset_download(handle))

    for item in cached_path.iterdir():
        target = dest / item.name
        if item.is_dir():
            shutil.copytree(item, target, dirs_exist_ok=True)
        else:
            shutil.copy2(item, target)

    return dest
