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
        font-size: 20px;
        margin: 0px;
    }}
    
    QLabel#title {{
        font-size: 75px;
        margin-bottom: 50px;
    }}
    
    QPushButton {{
        background-repeat: no-repeat;
        background-position: center;
    }}
        
    QPushButton {{
        border: 1px solid {var("--main-highlight")};
        border-radius: 5px;
        font-size: 25px;
        color: {var("--main-highlight")};
        padding: 20px;
        max-width: 230px;
    }}
    
    QPushButton#home {{
        background-image: {url("imgs/button.png")};
        margin: 50px 75px;
        width: 200px;
    }}
    
    QPushButton#how {{
        background-image: {url("imgs/button.png")};
        margin: 50px 225px;    
        width: 200px;    
    }}
    
    QPushButton#tile-active {{
        padding: 0px;
        margin: 0px;
        border-radius: 0px;
        border: 1px solid {var("--main-highlight")};
        background-color: rgba(13, 13, 13, 0.75);
    }}
    
    QPushButton#tile-inactive {{
        padding: 0px;
        margin: 0px;
        border: none;
        border-radius: 0px;
        background-color: transparent;
    }}
"""
