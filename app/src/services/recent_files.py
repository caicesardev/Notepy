import os
from pathlib import Path

MAX_RECENT_FILES = 10


def add_recent_file(recent_files: list[Path], path: Path) -> list[Path]:
    remaining = [recent for recent in recent_files if not is_same_path(recent, path)]
    return [path, *remaining][:MAX_RECENT_FILES]


def remove_recent_file(recent_files: list[Path], path: Path) -> list[Path]:
    return [recent for recent in recent_files if not is_same_path(recent, path)]


def is_same_path(first: Path, second: Path) -> bool:
    return os.path.normcase(first.absolute()) == os.path.normcase(second.absolute())
