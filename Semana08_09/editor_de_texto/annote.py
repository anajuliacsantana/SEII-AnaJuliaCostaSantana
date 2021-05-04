
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import os
import sys


#Configurando as opções do editor
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        layout = QVBoxLayout()
        #Iniciando como um Plan Text
        self.editor = QTextEdit() 
        self.editor.setAcceptRichText(False)

        # Ajustando a configuração do QTextEdit
        fixedfont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        fixedfont.setPointSize(12)
        self.editor.setFont(fixedfont)

        self.path = None  # Se o caminha = None, um arquivo não foi criado ou aberto ainda

        layout.addWidget(self.editor)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        #Ações que o editor me permite no Menu superior
        file_toolbar = QToolBar("Arquivo")
        file_toolbar.setIconSize(QSize(14, 14))
        self.addToolBar(file_toolbar)
        file_menu = self.menuBar().addMenu("&Arquivo")
        #Abrir já existente
        open_file_action = QAction( "Abrir...", self)
        open_file_action.setStatusTip("Abrir um arquivo já existente")
        open_file_action.triggered.connect(self.abrir)
        file_menu.addAction(open_file_action)
        file_toolbar.addAction(open_file_action)
        
        save_file_action = QAction("Salvar", self)
        save_file_action.setStatusTip("Salvar conteúdo")
        save_file_action.triggered.connect(self.file_save)
        file_menu.addAction(save_file_action)
        file_toolbar.addAction(save_file_action)
        
        #Salvar como..

        saveas_file_action = QAction("Salvar Como...", self)
        saveas_file_action.setStatusTip("Salvar o conteúdo para um arquivo específico")
        saveas_file_action.triggered.connect(self.file_saveas)
        file_menu.addAction(saveas_file_action)
        file_toolbar.addAction(saveas_file_action)

        #Sair 

        file_menu.addSeparator()
        exit_action = QAction("Sair", self)
        exit_action.setStatusTip("Sair do editor")
        exit_action.triggered.connect(self.close)
        file_menu.addAction( exit_action)
        file_toolbar.addAction( exit_action)
        
        self.update_title()
        self.show()

    def dialog_critical(self, s):
        dlg = QMessageBox(self)
        dlg.setText(s)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()


    def abrir(self):
        path, _ = QFileDialog.getOpenFileName(self, "Abrir", "", "Text documents (*.txt);All files (*.*)")
        
        if path:
            try:
                with open(path, 'rU') as f:
                    text = f.read()

            except Exception as e:
                self.dialog_critical(str(e))

            else:
                self.path = path
                self.editor.setPlainText(text)
                self.update_title()
       

    def file_save(self):
        if self.path is None:
            # Se não houver um caminho chama Salvar Como..
            return self.file_saveas()
        self._save_to_path(self.path)

    def file_saveas(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "Text documents (*.txt);All files (*.*)")

        if not path:
            # Se a caixa for fechada antes de salvar retorna ''
            return

        self._save_to_path(path)

    def _save_to_path(self, path):
        text = self.editor.toPlainText()
        try:
            with open(path, 'w') as f:
                f.write(text)

        except Exception as e:
            self.dialog_critical(str(e))

        else:
            self.path = path
            self.update_title()

    def update_title(self):
        self.setWindowTitle("%s - An Note" % (os.path.basename(self.path) if self.path else "Untitled"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("An Note")
    window = MainWindow()
    app.exec_()
