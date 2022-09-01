def var(name):
    return {
        "--main-highlight": "#70AD47"
    }[name]


stylesheet = f"""
    QMainWindow {{
        background-image: url(imgs/background.jpg); 
        background-repeat: no-repeat;
        background-position: center;
        min-width: 1280px;
        max-width: 1280px;
        min-height: 720px;
        max-height: 720px;
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
        background-image: url(imgs/button.png);
        margin: 50px 75px;
        width: 200px;
    }}
    
    QPushButton#how {{
        background-image: url(imgs/button.png);
        margin: 50px 225px;    
        width: 200px;    
    }}
    
    QPushButton#tile-active {{
        padding: 0px;
        margin: 0px;
        border-radius: 0px;
        border: 1px solid {var("--main-highlight")};
        background-color: #0D0D0D;
    }}
    
    QPushButton#tile-inactive {{
        padding: 0px;
        margin: 0px;
        border: none;
        border-radius: 0px;
        background-color: transparent;
    }}
"""
