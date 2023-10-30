from dataclasses import dataclass
from webbrowser import open_new_tab

import pyperclip
import PySimpleGUI as sG
from PySimpleGUI import Window

from yt_link_converter.ytvid_replace import main as convert_link


@dataclass
class ButtonEvent:
    paste_copy = "-PASTECOPY-"
    paste_open = "-PASTEOPEN-"


@dataclass
class GUI:
    default_input_text = "Link:"
    sG.theme("Dark")
    title = "yt-embed"
    input_text = sG.Text(default_input_text, key="-TEXTFIELD-")
    button_paste_copy = sG.Button("Paste & Copy", key=ButtonEvent.paste_copy)
    button_paste_open = sG.Button("Paste & Open", key=ButtonEvent.paste_open)
    button_clear = sG.Button("Clear", key="-CLEAR-")
    layout = [[input_text], [button_paste_copy, button_paste_open]]


def paste_copy(to_clipboard: str):
    pyperclip.copy(to_clipboard)


def paste_open(link: str):
    open_new_tab(link)


def logic(event: str, window: Window, gui: GUI) -> None:
    from_clipboard = pyperclip.paste()
    result = convert_link(from_clipboard)
    to_show = "Not a valid youtube link"
    if result is not None:
        to_clipboard = result[0] + result[1]
        to_show = f"embed/{result[1]}"
        if event == ButtonEvent.paste_copy:
            paste_copy(to_clipboard)
        if event == ButtonEvent.paste_open:
            paste_open(to_clipboard)
    window["-TEXTFIELD-"].update(gui.default_input_text + " " + to_show)
    return


def main() -> None:
    gui = GUI()
    window = sG.Window(gui.title, layout=gui.layout)

    while True:
        event, values = window.read()
        if event == sG.WINDOW_CLOSED or event == sG.WIN_CLOSED:
            break
        if event in (ButtonEvent.paste_copy, ButtonEvent.paste_open):
            logic(event, window, gui)

    window.close()


if __name__ == "__main__":
    main()
