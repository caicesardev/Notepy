# Changelog

## [1.1.0] - 2026-10-31

### Added
- Find and replace dialog with *Match case*, *Whole words* and *Wrap around* options, *Replace* and *Replace all* (a single undo step).
- *Find next* (F3) and *Find previous* (Shift+F3) repeat the last search.
- *Recent files* menu (last 10 files) with an option to clear the list.
- Open files from the command line, from *Open with* and by dragging them onto the window (several files open in separate windows).
- Encoding detection (UTF-8, UTF-8 with BOM, UTF-16 LE/BE and ANSI) and line ending detection (CRLF, LF, CR); both are kept when saving.
- Status bar shows line, column, character count, zoom, line ending and encoding.
- Light, dark and system themes applied live, including dialogs.
- Font settings with family, style and size plus a live preview.
- *Delete* action, *About Notepy* dialog and print selection.
- Word wrap and status bar visibility are remembered between sessions.

### Fixed
- Saving an untitled file crashed or wrote nothing when the *Save as* dialog was cancelled, and *Save as* never cleared the unsaved marker.
- Choosing *Save* in the unsaved changes prompt did not continue with the new, open or close action, and closing with *Discard* asked again in a loop.
- Unsaved changes were detected from the cursor position, so undoing back to the saved text still showed the document as modified.
- Files were read and written with the system code page, corrupting accents and other non-ASCII characters.
- *New window* launched `./main.py` through a subprocess, which failed from the executable or from any other working directory.
- *Find next*, *Find previous*, *Replace* and *Replace all* did nothing; plain search matched whole words only and case-sensitive search ignored the direction.
- *Go to* moved the cursor to the wrong line and crashed with an empty value.
- Zoom percentage did not match the real font size, Ctrl + mouse wheel zoom was not reflected in the status bar and *Restore zoom* left a different size.
- Font and theme settings were not applied on startup, the dark theme could not be turned off and the system theme did nothing.
- Page setup was discarded before printing.
- Cursor position was not updated when moving the cursor and the column was off by one.
- Undo, redo, cut, copy and paste were enabled when they could not be used.
- Window position was stored even when closing was cancelled.

### Changed
- Standard shortcuts: Ctrl+F find, Ctrl+H replace, Ctrl+G go to line, Ctrl+A select all and Ctrl+, settings.
- *Settings* moved to the *File* menu; find, replace and settings are regular movable dialogs.
- Default font is Consolas 11 and word wrap is enabled by default.
- Code split into models, services, settings, widgets and windows with unit tests.
- Updated to Python 3.13 and PySide6-Essentials 6.12.0; removed unused development packages from the requirements.
- Added a PyInstaller build script that produces a single Windows executable.

## [1.0.0] - 2022-05-26

- First release.

[1.1.0]: https://github.com/caicesardev/Notepy/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/caicesardev/Notepy/releases/tag/v1.0.0
