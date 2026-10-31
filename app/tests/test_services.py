import unittest
from pathlib import Path

from main import files_to_open
from src.models.theme import Theme
from src.services.recent_files import MAX_RECENT_FILES, add_recent_file, remove_recent_file
from src.services.zoom import MAX_ZOOM_PERCENT, MIN_POINT_SIZE, MIN_ZOOM_PERCENT, clamp_zoom, zoomed_point_size
from src.windows.main_window import ALL_FILES_FILTER, TEXT_FILE_FILTER, with_text_suffix


class ZoomTest(unittest.TestCase):
    def test_clamps_zoom_to_supported_range(self) -> None:
        self.assertEqual(clamp_zoom(0), MIN_ZOOM_PERCENT)
        self.assertEqual(clamp_zoom(150), 150)
        self.assertEqual(clamp_zoom(9000), MAX_ZOOM_PERCENT)

    def test_scales_point_size(self) -> None:
        self.assertEqual(zoomed_point_size(12, 150), 18)
        self.assertEqual(zoomed_point_size(6, 10), MIN_POINT_SIZE)


class RecentFilesTest(unittest.TestCase):
    def test_moves_reopened_file_to_top(self) -> None:
        recent = [Path("a.txt"), Path("b.txt")]
        self.assertEqual(add_recent_file(recent, Path("b.txt")), [Path("b.txt"), Path("a.txt")])

    def test_limits_history_length(self) -> None:
        recent = [Path(f"{index}.txt") for index in range(MAX_RECENT_FILES)]
        updated = add_recent_file(recent, Path("new.txt"))
        self.assertEqual(len(updated), MAX_RECENT_FILES)
        self.assertEqual(updated[0], Path("new.txt"))

    def test_removes_file(self) -> None:
        self.assertEqual(remove_recent_file([Path("a.txt"), Path("b.txt")], Path("a.txt")), [Path("b.txt")])


class FileNamesTest(unittest.TestCase):
    def test_adds_text_suffix_only_for_text_filter(self) -> None:
        self.assertEqual(with_text_suffix(Path("nota"), TEXT_FILE_FILTER), Path("nota.txt"))
        self.assertEqual(with_text_suffix(Path("nota.md"), TEXT_FILE_FILTER), Path("nota.md"))
        self.assertEqual(with_text_suffix(Path("nota"), ALL_FILES_FILTER), Path("nota"))

    def test_opens_untitled_window_without_arguments(self) -> None:
        self.assertEqual(files_to_open([]), [None])
        self.assertEqual(files_to_open(["a.txt"]), [Path("a.txt")])


class ThemeTest(unittest.TestCase):
    def test_falls_back_to_system_theme(self) -> None:
        self.assertIs(Theme.from_key("dark"), Theme.DARK)
        self.assertIs(Theme.from_key("unknown"), Theme.SYSTEM)


if __name__ == "__main__":
    unittest.main()
