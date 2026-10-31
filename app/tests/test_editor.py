import os
import unittest

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication

from src.models.search_options import SearchOptions
from src.services.text_search import TextSearch
from src.services.zoom import MAX_ZOOM_PERCENT
from src.widgets.text_editor import TextEditor

APPLICATION = QApplication.instance() or QApplication([])


class EditorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.editor = TextEditor()
        self.editor.setPlainText("Hola mundo\nhola Mundo\nholanda")
        self.search = TextSearch(self.editor)


class TextSearchTest(EditorTestCase):
    def test_finds_case_insensitively_and_wraps_around(self) -> None:
        options = SearchOptions("mundo")
        self.assertTrue(self.search.find(options))
        self.assertEqual(self.editor.cursor_line, 1)
        self.assertTrue(self.search.find(options))
        self.assertEqual(self.editor.cursor_line, 2)
        self.assertTrue(self.search.find(options))
        self.assertEqual(self.editor.cursor_line, 1)

    def test_respects_wrap_around_option(self) -> None:
        options = SearchOptions("holanda", wrap_around=False)
        self.assertTrue(self.search.find(options))
        self.assertFalse(self.search.find(options))

    def test_finds_backward(self) -> None:
        self.assertTrue(self.search.find(SearchOptions("hola"), backward=True))
        self.assertEqual(self.editor.cursor_line, 3)

    def test_respects_case_and_whole_words(self) -> None:
        self.assertEqual(self.search.replace_all(SearchOptions("hola", case_sensitive=True), "x"), 2)
        self.assertEqual(self.editor.toPlainText(), "Hola mundo\nx Mundo\nxnda")

    def test_whole_words_skip_partial_matches(self) -> None:
        self.assertEqual(self.search.replace_all(SearchOptions("hola", whole_words=True), "adiós"), 2)
        self.assertEqual(self.editor.toPlainText(), "adiós mundo\nadiós Mundo\nholanda")

    def test_replace_all_is_a_single_undo_step(self) -> None:
        original = self.editor.toPlainText()
        self.search.replace_all(SearchOptions("o"), "oo")
        self.assertNotEqual(self.editor.toPlainText(), original)
        self.editor.undo()
        self.assertEqual(self.editor.toPlainText(), original)

    def test_replace_changes_current_match_and_selects_next(self) -> None:
        options = SearchOptions("mundo")
        self.search.find(options)
        self.assertTrue(self.search.replace(options, "planeta"))
        self.assertEqual(self.editor.toPlainText().splitlines()[0], "Hola planeta")
        self.assertEqual(self.editor.textCursor().selectedText(), "Mundo")

    def test_empty_search_does_nothing(self) -> None:
        self.assertFalse(self.search.find(SearchOptions("")))
        self.assertEqual(self.search.replace_all(SearchOptions(""), "x"), 0)


class TextEditorTest(EditorTestCase):
    def test_goes_to_line(self) -> None:
        self.editor.go_to_line(3)
        self.assertEqual((self.editor.cursor_line, self.editor.cursor_column), (3, 1))

    def test_ignores_lines_out_of_range(self) -> None:
        self.editor.go_to_line(2)
        self.editor.go_to_line(99)
        self.assertEqual(self.editor.cursor_line, 2)

    def test_counts_characters(self) -> None:
        self.assertEqual(self.editor.character_count, len(self.editor.toPlainText()))

    def test_zoom_scales_base_font(self) -> None:
        self.editor.set_base_font(QFont("Consolas", 10))
        self.editor.set_zoom(200)
        self.assertEqual(self.editor.font().pointSizeF(), 20)
        self.editor.reset_zoom()
        self.assertEqual(self.editor.font().pointSizeF(), 10)

    def test_zoom_emits_clamped_percent(self) -> None:
        emitted = []
        self.editor.zoom_changed.connect(emitted.append)
        self.editor.set_zoom(10_000)
        self.assertEqual(emitted, [MAX_ZOOM_PERCENT])

    def test_delete_forward_removes_next_character(self) -> None:
        self.editor.go_to_line(1)
        self.editor.delete_forward()
        self.assertTrue(self.editor.toPlainText().startswith("ola mundo"))


if __name__ == "__main__":
    unittest.main()
