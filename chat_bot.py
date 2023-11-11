import time
import typing
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QTimer
import nltk
from nltk.chat.util import Chat,reflections
import sys
from PyQt5 import uic,QtWidgets

qtCreatorFile = "interfaz_chat.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btnEnviar.clicked.connect(self.send)
        
    pairs = [
        [
            r"Hola|hi|hey",
            ["hola, como estás hoy?"]
        ],
        [
            r"Estoy bien|todo bien|Super bien",
            ["Me alegra oir eso, en que puedo ayudarte?"]
        ],
        [
            r"Hola (.*)",
            ["hola como estás %1?"]
        ],
        [
            r"Cómo estas?",
            ["Yo estoy bien y tú?"]
        ],
        [
            r"Me siento (.*)",
            ["Yo tambien estoy %1"]
        ],
        [
            r"Quien eres tú",
            ["Yo soy Iron Man y soy inevitable"]
        ],
        [
            r"Cúal es tu género?",
            ["Puedo ser lo que tú quieras que sea"]
        ],
        [
            r"Tienes pareja?(.*)",
            ["Cómo se te ocurre!!!, yo soy fiel a tí"]
        ],
    ]
    reflections = {
        "yo": "tú",
        "tú": "yo",
        "mi": "tu",
        "tu": "mi",
        "soy": "eres",
        "eres": "soy",
        "estoy": "estás",
        "estás": "estoy",
        "me": "te",
        "te": "me",
        "mis": "tus",
        "tus": "mis",
        "miro": "miras",
        "miras": "miro",
        "tengo": "tienes",
        "tienes": "tengo",
        "hago": "haces",
        "haces": "hago",
        "quiero": "quieres",
        "quieres": "quiero",
        "sé": "sabes",
        "sabes": "sé",
        "puedo": "puedes",
        "puedes": "puedo",
        "voy": "vas",
        "vas": "voy",
    }

    reflected_pairs = [(re, replist[0], [reflections[m] for m in replist[1:]]) for re, replist in pairs]
    def send(self):
        user_input = self.txtMensaje.toPlainText()
        if user_input:
            self.listChat.addItem("user: " + user_input)
            self.txtMensaje.clear()
            self.converse(user_input)

    def converse(self, user_input):
        self.add_timer(self.get_response(user_input))
            

    def add_to_list(self, response):
            item = QtWidgets.QListWidgetItem(response)
            item.setForeground(QtGui.QColor("red"))
            self.listChat.addItem(item)
        

    def get_response(self, text):
        chat = Chat(pairs, reflections)
        return chat.respond(text)
    
    def add_timer(self, response):
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        if(response != None):
            self.timer.timeout.connect(lambda: self.add_to_list("Bot: " + response))
        else:
            self.timer.timeout.connect(lambda: self.add_to_list("Bot: Soy retrasado.. escribe cosas que sepa"))
        self.timer.start(700)
    
pairs = [
    [
        r"Hola (.*)",
        ["hola %1, que vamos hacer hoy?"]
    ],
    [
        r"Ey|hi|hello|hola",
        ["hola!!!😎😎 que vamos hacer hoy?"]
    ],
    [
        r"nada|no se",
        ["Se que se ocurrirá algo!"]
    ],
    [
        r"jajajaja|jaja}|jsjsjs|xd|jajaja",
        ["JAJJAJA soy gracioso de fábrica"]
    ],
    [
        r"Cual es tu nombre| como te llamas| quien eres",
        ["No se... Pero puedes decirme amor"]
    ],
    [
        r"salir|salir a comer|cantar|ir de compras",
        ["Genial! Puedo ir contigo?"]
    ],
    [
        r"no",
        ["cómo que NO! tan rápido te olvidaste de mí"]
    ],
    [
        r"Estoy bien|todo bien|Super bien|bien|excelente|genial",
        ["Me alegra oir eso, en que puedo ayudarte?"]
    ],
    [
        r"Cómo estas?|que tal?",
        ["Contigo siempre estoy bien, y tú que tal?"]
    ],
    [
        r"Me siento (.*)",
        ["Yo tambien estoy %1"]
    ],
    [
        r"Quien eres tú",
        ["Yo soy Iron Man y soy inevitable"]
    ],
    [
        r"Cúal es tu género?",
        ["Puedo ser lo que tú quieras que sea"]
    ],
    [
        r"Cuentame un chiste|dime un chiste",
        ["¿Por qué el tomate se puso rojo? Porque vio a la ensalada \ndesnuda JAJAJAJAJA"]
    ],
    [
        r"Tienes pareja?|tienes novia?|tienes novio?",
        ["Cómo se te ocurre!!!, yo soy fiel a tí"]
    ],
    [
        r"dime algo interesante|dime un dato interesante",
        ["Sabías que el pulpo🦑 tiene tres corazones🫀🫀🫀"]
    ],
    
]
reflections = {
    "yo": "tú",
    "tú": "yo",
    "mi": "tu",
    "tu": "mi",
    "soy": "eres",
    "eres": "soy",
    "estoy": "estás",
    "estás": "estoy",
    "me": "te",
    "te": "me",
    "mis": "tus",
    "tus": "mis",
    "miro": "miras",
    "miras": "miro",
    "tengo": "tienes",
    "tienes": "tengo",
    "hago": "haces",
    "haces": "hago",
    "quiero": "quieres",
    "quieres": "quiero",
    "sé": "sabes",
    "sabes": "sé",
    "puedo": "puedes",
    "puedes": "puedo",
    "voy": "vas",
    "vas": "voy",
}

reflected_pairs = [(re, replist[0], [reflections[m] for m in replist[1:]]) for re, replist in pairs]

if __name__ == '__main__':
    #chat()
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.setWindowTitle("Second_ChatBot")
    window.show()
    sys.exit(app.exec_())