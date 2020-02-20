from googletrans import Translator
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from os import path
import sys
FORM_CLASS,_ = loadUiType(path.join(path.dirname(__file__),'main.ui'))
class mainApp1(QMainWindow, FORM_CLASS):
    c = ['english', 'afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali',
         'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese (simplified)', 'chinese (traditional)',
         'corsican', 'croatian', 'czech', 'danish', 'dutch', 'esperanto', 'estonian', 'filipino',
         'finnish',
         'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian creole', 'hausa',
         'hawaiian', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish', 'italian',
         'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish (kurmanji)', 'kyrgyz', 'lao',
         'latin',
         'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy', 'malay', 'malayalam', 'maltese',
         'maori',
         'marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 'norwegian', 'pashto', 'persian', 'polish',
         'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona',
         'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish',
         'tajik',
         'tamil', 'telugu', 'thai', 'turkish', 'ukrainian', 'urdu', 'uzbek', 'vietnamese', 'welsh', 'xhosa',
         'yiddish',
         'yoruba', 'zulu', 'Filipino', 'Hebrew']
    def __init__(self, parent=None):
        super(mainApp1,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handel_ui()
        self.handle_button()

    def handle_button(self):
        self.pushButton.clicked.connect(self.trans_fun)
    def handel_ui(self):
        self.setFixedSize(800,600)
        for i in self.c :
             self.comboBox.addItem(i)
    def trans_fun(self):
        response0 = str(self.lineEdit.text())
        response1 = " to "
        trans_to = self.comboBox.currentIndex()
        response2=str(self.c[trans_to])
        translator = Translator()  # Create object of Translator.
        text = response0 + response1 + response2
        text = text.split()
        n = len(text)
        lang = text[n - 1]
        text[n - 2] = ''
        text[n - 1] = ''
        data = ' '.join(text)
        translated = translator.translate(data, dest='%s' % lang)
        data = (translated.text)
        self.lineEdit_2.setText(str(data))
def main():
    app = QApplication(sys.argv)
    window = mainApp1()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
