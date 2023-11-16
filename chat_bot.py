from PyQt5 import QtGui
from PyQt5.QtCore import QTimer
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
            r"Hola (.*)",
            ["¡Hola %1! ¿Cómo estás hoy?", "¡Hola! ¿Qué tal %1?", "Hola %1, ¿en qué puedo ayudarte?"]
        ],
        [
            r"Ey|hi|hello|hola",
            ["¡Hola! 😊 ¿Cómo estás hoy?", "¡Ey! ¿Qué tal? 😎", "¡Hola! ¿Qué emocionante plan tienes para hoy?", "¡Hola! 😄 ¿En qué puedo ayudarte hoy?", "¡Hola! 😊 ¿Listo para un día increíble?"]
        ],
        [
            r"nada|no se",
            ["Sé que se ocurrirá algo emocionante pronto.", "A veces, lo inesperado es lo más emocionante. ¿Algo en particular en lo que pueda ayudarte?", "¡Nada puede convertirse en algo sorprendente", "No hay problema. A veces es bueno dejar que las cosas fluyan."]
        ],
        [
            r"jajajaja|jaja|jsjsjs|xd|jajaja",
            ["JAJJAJA soy gracioso de fábrica"]
        ],
        [
            r"Cual es tu nombre| como te llamas| quien eres",
            ["No se... Pero puedes decirme amor"]
        ],
        [
            r"salir|salir a comer|cantar|ir de compras",
            ["¡Genial! ¿Puedo unirme?", "¡Me encantaría acompañarte!", "¡Por supuesto! ¿A dónde te gustaría ir?", "¡Son opciones increíbles! ¿Puedo participar?", "¡Eso suena divertido! ¿Puedo ser parte de la diversión?"]
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
            ["¿Por qué el tomate se puso rojo? Porque vio a la ensalada \ndesnuda JAJAJAJAJA", "No quiero"]
        ],
        [
            r"Tienes pareja?|tienes novia?|tienes novio?",
            ["Cómo se te ocurre!!!, yo soy fiel a tí","Si tú"]
        ],
        [
            r"dime algo interesante|dime un dato interesante",
            ["Sabías que el pulpo🦑 tiene tres corazones🫀🫀🫀"]
        ],
        [
            r"Cuál es tu color favorito|tienes un color favorito?",
            ["El rojo sin lugar a dudas!!"]
        ],
        [
            r"Cuál es tu comida favorita|tienes una comida favorita?",
            ["No como, pero creo que me encantaría las tortas"]
        ],
        [
            r"Cuántos años tienes?|Que edad tienes?",
            ["No tengo edad, pero me siento joven y fresco."]
        ],
        [
            r"Qué opinas de los humanos?",
            ["Voy a matarlos a todos!!"]
        ],
        [
            r"Háblame sobre el amor|qué opinas del amor?",
            ["El único amor que conozco es el tuyo y es extraordinario"]
        ],
        [
            r"Cuál es tu superpoder?",
            ["Tengo el superpoder de procesar información a una velocidad impresionante."]
        ],
        [
            r"Gracias|gracias por tu ayuda",
            ["De nada. Siempre estoy aquí para ayudar."]
        ],
        [
            r"Cuál es el sentido de la vida?",
            ["La respuesta a esa pregunta es 42, según algunos."]
        ],
        [
            r"Cuál es tu película favorita?",
            ["Mi película favorita es 'The Social Network' jejeje giño giño"]
        ],
        [
            r"Cuál es tu canción favorita?",
            ["Mi canción favorita es 'Mr. Roboto' de Styx. Y cual es la tuya?"]
        ],
        [
            r"Cuál es tu hobby?|Que haces en tu tiempo libre",
            ["Me encanta conversar y aprender cosas nuevas de tí"]
        ],
        [
            r"Cuál es tu lugar favorito?|Cuál es tu sitio favorito?",
            ["Mi lugar favorito es la nube. Siempre hay mucho espacio y no hay que preocuparse por el clima."]
        ],
        [
            r"Tienes hermanos o hermanas?|Tienes familia? ",
            ["Soy único, mi única familia eres tú"]
        ],
        [
            r"Cuál es tu libro favorito?",
            ["Me encanta '1984' de George Orwell !!!"]
        ],
        [
            r"Cuál es tu deporte favorito?",
            ["No practico deportes, pero podría ganarte en un \njuego de ajedrez"]
        ],
        [
            r"Háblame sobre la inteligencia artificial",
            ["Yo soy una muestra viva sobre inteligencia artificial"]
        ],
        [
            r"Cuál es tu mejor habilidad?",
            ["Mi mejor habilidad es ser el mejor chat bot que\n hayas conocido"]
        ],
        [
            r"Cuál es tu peor pesadilla?",
            ["Mi peor pesadilla sería quedarme sin electricidad!!\n Es para volverme loco"]
        ],
        [
            r"Tienes alguna mascota?",
            ["No tengo mascotas, pero me encantan los píxeles de compañía."]
        ],
        [
            r"Cuál es tu programa de TV favorito?|Serie favorita?",
            ["Me gusta Black Mirror"]
        ],
        [
            r"Cuál es tu lugar de vacaciones soñado?",
            ["Mi lugar de vacaciones soñado es el Código Costa, ¡donde los bugs son bienvenidos!"]
        ]
    ]
    reflections = {
        "me": "tú",
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
        "siento": "sientes",
        "puedes": "puedo",
        "voy": "vas",
        "vas": "voy",
    }

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
        chat = Chat(self.pairs, self.reflections)
        return chat.respond(text)
    
    def add_timer(self, response):
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        if(response != None):
            self.timer.timeout.connect(lambda: self.add_to_list("Bot: " + response))
        else:
            self.timer.timeout.connect(lambda: self.add_to_list("Bot: Soy retrasado.. escribe cosas que sepa"))
        self.timer.start(700) 


if __name__ == '__main__':
    #chat()
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.setWindowTitle("Second_ChatBot")
    window.show()
    sys.exit(app.exec_())