from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


import operator
#Importando configuração da tela da calculadora
from Interface import Ui_MainWindow 

# Estado da Calculadora.
READY = 0
INPUT = 1
class MainWindow(QMainWindow, Ui_MainWindow): #configurando a calculadora
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Inserindo os números
        for n in range(0, 10):
            getattr(self, 'pushButton_n%s' % n).pressed.connect(lambda v=n: self.input_number(v))

        # Configurando os operadores.
        self.pushButton_add.pressed.connect(lambda: self.operation(operator.add))
        self.pushButton_sub.pressed.connect(lambda: self.operation(operator.sub))
        self.pushButton_mul.pressed.connect(lambda: self.operation(operator.mul))
        self.pushButton_pot.pressed.connect(lambda: self.operation(operator.pow))
        self.pushButton_div.pressed.connect(lambda: self.operation(operator.truediv))  # operator.div para Python2.7

        self.pushButton_pc.pressed.connect(self.operation_pc) #porcentagem
        self.pushButton_eq.pressed.connect(self.equals)

        # Ações que podem ser realizadas
        self.actionReset.triggered.connect(self.reset)
        self.pushButton_ac.pressed.connect(self.reset) # para apagar

        self.actionExit.triggered.connect(self.close)
        #Ações de memória
        self.pushButton_m.pressed.connect(self.memory_store)
        self.pushButton_mr.pressed.connect(self.memory_recall)

        self.memory = 0
        self.reset()

        self.show()

    #Implementação da operação com stack,state e current operation
    #stack = armazenmaneto de curta memória, com no máximo 2 elementos
    def display(self):
        self.lcdNumber.display(self.stack[-1])

    def reset(self):
        self.state = READY
        self.stack = [0]
        self.last_operation = None
        self.current_op = None
        self.display()
    #pega o valor lido no display e o leva a variavel self.memory
    def memory_store(self):
        self.memory = self.lcdNumber.value()
    #pega o valor de self.memory e o coloca na ultima posição do staack
    def memory_recall(self):
        self.state = INPUT
        self.stack[-1] = self.memory
        self.display()
    #stat = realiza a variação entre os estados ready e input, para que o valor inserido seja direcionado ao stack ou na logica de shift+add
    def input_number(self, v):
        if self.state == READY:
            self.state = INPUT
            self.stack[-1] = v
        else:
            self.stack[-1] = self.stack[-1] * 10 + v

        self.display()
    #current_op = armazena a operação ativa,até que o usuário pressione igual
    def operation(self, op):
        if self.current_op:   #Raliza a operação.
            self.equals()

        self.stack.append(0)
        self.state = INPUT
        self.current_op = op

    def operation_pc(self):
        self.state = INPUT
        self.stack[-1] *= 0.01
        self.display()

    def equals(self):
        # Função para que igual realiza  a função ANS, repetindo o cálculo previamnete realizado
        # se mais nenhum valor for inserido
        if self.state == READY and self.last_operation:
            s, self.current_op = self.last_operation
            self.stack.append(s)

        if self.current_op:
            self.last_operation = self.stack[-1], self.current_op

            try:
                self.stack = [self.current_op(*self.stack)]
            except Exception:
                self.lcdNumber.display('Err')
                self.stack = [0]
            else:
                self.current_op = None
                self.state = READY
                self.display()


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Calculadora com PyQt5")

    window = MainWindow()
    app.exec_()