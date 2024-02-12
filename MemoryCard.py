from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)
from random import shuffle

app = QApplication([])
window = QWidget()

verno = 0
neverno = 0

while print('Верные ответы:', verno, 'Не Верные Ответы:', neverno) == app.exec:
    print('Аналитика')

# def __init__(self, text: typing.Optional[str], parent: typing.Optional[QWidget] = ..., flags: typing.Union[QtCore.Qt.WindowFlags, QtCore.Qt.WindowType] = ...) -> None: ...

class Question():
    def __init__(self, question:str, right_answer:str, wrong1:str, wrong2:str, wrong3:str) -> None:
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('В каком году появилась Российская Федерация?', '1991', '2000', '1900', '1994'))
question_list.append(Question('Сколько стоит вода?', '50р', '100р', '200р', '60р'))
question_list.append(Question('Какой у меня телефон?', 'Крутой', 'норм', 'фигня', 'что такое телефон'))




window.setWindowTitle('MemoryCard')
button = QPushButton('Ответить')
label = QLabel('В каком году была основана Москва?')

radioGroupBox = QGroupBox('Вырианты ответов')

vop1 = QRadioButton('114754545454')
vop2 = QRadioButton('1242')
vop3 = QRadioButton('1861')
vop4 = QRadioButton('194343434344444')

radioGroup = QButtonGroup()
radioGroup.addButton(vop1)
radioGroup.addButton(vop2)
radioGroup.addButton(vop3)
radioGroup.addButton(vop4)


layout_1 = QVBoxLayout()
layout_2 = QVBoxLayout()

layout_1.addWidget(vop1)
layout_1.addWidget(vop2)
layout_2.addWidget(vop3)
layout_2.addWidget(vop4)

layout_R = QHBoxLayout()
layout_R.addLayout(layout_1)
layout_R.addLayout(layout_2)

radioGroupBox.setLayout(layout_R)

answerGroupBox = QGroupBox('Результат теста')
label_Res = QLabel('прав ты или нет?')
label_Res1 = QLabel('здесь ответ')
agb_vl = QVBoxLayout()
agb_vl.addWidget(label_Res, alignment = Qt.AlignmentFlag.AlignLeft)
agb_vl.addWidget(label_Res1, alignment = Qt.AlignmentFlag.AlignCenter)
answerGroupBox.setLayout(agb_vl)



layout_main = QVBoxLayout()
layout_check = QHBoxLayout()
layout_check.addWidget(radioGroupBox)
layout_check.addWidget(answerGroupBox)

layout_main.addWidget(label,alignment = Qt.AlignmentFlag.AlignHCenter)
layout_main.addLayout(layout_check)
layout_main.addWidget(button,alignment = Qt.AlignmentFlag.AlignCenter)
#radioGroupBox.hide()
answerGroupBox.hide()

def show_result():
    radioGroupBox.hide()
    answerGroupBox.show()
    button.setText('Следующий вопрос')

def show_qestion():
    radioGroupBox.show()
    answerGroupBox.hide()
    button.setText('Ответить')
    radioGroup.setExclusive(False)
    vop1.setChecked(False)
    vop2.setChecked(False)
    vop3.setChecked(False)
    vop4.setChecked(False)
    radioGroup.setExclusive(True)

answers = [vop1, vop2, vop3, vop4]

def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    label.setText(q.question)
    label_Res1.setText(q.right_answer)
    show_qestion()



def show_correct(res):
    label_Res.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Не верно')

def next_question():
    shuffle(question_list)
    ask(question_list[0])


#QRadioButton.clicked.connect()

def swow():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

def negr(n:Question):
    if answers == n.right_answer:
        verno += 1
    else:
        neverno += 1



        




button.clicked.connect(swow)
window.setLayout(layout_main)



window.show()
app.exec_()

