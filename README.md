# PySimpleGUI 5.0.7

A rebuilt version of the PySimpleGUI package. This is a local copy of the original PySimpleGUI package that was removed from PyPI.

## Installation

You can install this package directly from GitHub:

```bash
pip install git+https://github.com/pfgoting/pysimplegui-5.0.7.git
```

## Usage

```python
import PySimpleGUI as sg

layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]
window = sg.Window("Demo", layout)

while True:
    event, values = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()
```

## License

This package is distributed under the original license of PySimpleGUI.
