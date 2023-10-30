from dataclasses import dataclass

import pyperclip
import PySimpleGUI as sG
from PySimpleGUI import Window

from yt_link_converter.ytvid_replace import main as convert_link


@dataclass
class GUI:
    default_input_text = "Link:"
    sG.theme("Dark")
    input_text = sG.Text(default_input_text, key="-TEXTFIELD-")
    button_paste_copy = sG.Button("Paste & Copy", key="-PASTECOPY-")
    button_clear = sG.Button("Clear", key="-CLEAR-")
    layout = [[input_text], [button_paste_copy]]


def logic(window: Window, gui: GUI) -> None:
    from_clipboard = pyperclip.paste()
    result = convert_link(from_clipboard)
    to_show = "Not a valid youtube link"
    if result is not None:
        to_clipboard = result[0] + result[1]
        to_show = f"embed/{result[1]}"
        pyperclip.copy(to_clipboard)
    window["-TEXTFIELD-"].update(gui.default_input_text + " " + to_show)
    return


def main() -> None:
    gui = GUI()
    window = sG.Window("to_embed", layout=gui.layout)

    while True:
        event, values = window.read()
        if event == sG.WINDOW_CLOSED or event == sG.WIN_CLOSED:
            break
        if event == "-PASTECOPY-":
            logic(window, gui)

    window.close()


if __name__ == "__main__":
    main()
