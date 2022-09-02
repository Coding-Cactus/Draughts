import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


def var(name):
    return {
        "--main-highlight": "#70AD47"
    }[name]


def url(path):
    path = os.path.join(BASE_DIR, path).replace("\\", "/")
    return f"url({path})"


stylesheet = f"""
    QMainWindow {{
        background-image: {url("imgs/background.jpg")};
        background-position: center;
        min-width: 800px;
        min-height: 800px;
    }}

    QLabel {{
        color: {var("--main-highlight")};
        margin: 0px;
    }}

    QLabel#title {{
        margin-bottom: 50px;
    }}

    QPushButton {{
        background-position: center;
    }}

    QPushButton {{
        border: 1px solid {var("--main-highlight")};
        border-radius: 5px;
        color: {var("--main-highlight")};
        padding: 20px;
    }}

    QPushButton#home {{
        background-image: {url("imgs/button.jpg")};
        margin: 50px 75px;
    }}

    QPushButton#how {{
        background-image: {url("imgs/button.jpg")};
        margin: 50px 225px;
        width: 200px;
    }}

    QScrollArea#content {{
        background-color: rgba(0, 0, 0, 0.4);
        padding: 20px;
        border-radius: 20px;
        max-width: 1500px;
    }}

    QLabel#content, QWidget#content-text {{
        background-color: transparent;
    }}

    QPushButton#tile-active {{
        padding: 0px;
        margin: 0px;
        border-radius: 0px;
        border: 1px solid {var("--main-highlight")};
        background-color: rgba(13, 13, 13, 0.75);
        background-repeat: no-repeat;
    }}

    QPushButton#tile-inactive {{
        padding: 0px;
        margin: 0px;
        border: none;
        border-radius: 0px;
        background-color: transparent;
        background-repeat: no-repeat;
    }}
"""
