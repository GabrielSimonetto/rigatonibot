from pathlib import Path
import requests

def filepath_to_paste(filename: Path) -> str:
    """Sends a file contents to paste.rs and returns the web link to access it"""
    path = Path(filename).as_posix()

    with open(path, 'r') as file:
        data = file.read()
        web_address = requests.post('http://paste.rs', data=data)

    return web_address.text


# def file_to_paste(filename: Path) -> str:
#     """Sends a file contents to paste.rs and returns the web link to access it"""
#     path = Path(filename).as_posix()

#     with open(path, 'r') as file:
#         data = file.read()
#         web_address = requests.post('http://paste.rs', data=data)

#     return web_address.text
