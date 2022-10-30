import sys
from PyQt5.QtGui import * #QImage, QPixmap, QFont,
from PyQt5.QtWidgets import QMainWindow,QApplication
from Pj2_MorseCodeUpThread import Pj2_UpThread
from Pj2_MorseCodeDownThread import Pj2_DownThread
from ui.ui_project2 import Ui_MainWindow

class MorseCode(QMainWindow,Ui_MainWindow) :
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.resize(1020,768)
        self.startFlag= False
        self.btn_1.clicked.connect(self.btn1Click)
        self.btn_2.clicked.connect(self.btn2Click)
        self.lstWgt_1.clicked.connect(self.assign)
        #載入圖片
        self.imgArrowUp = QImage("upArrow.svg")
        self.imgArrowDown = QImage("downArrow.svg")
        #設定圖片
        self.picBox_1.setPixmap(QPixmap(self.imgArrowDown))
        self.picBox_2.setPixmap(QPixmap(self.imgArrowUp))

        ###設定字體
        self.font = QFont("Book Antiqua",24)
        self.labText_1.setFont(self.font)
        self.labText_1.setPlaceholderText('輸入大寫英文或阿拉伯數字')
        self.tcf = QTextCharFormat()
        self.tcf.setFontCapitalization(QFont.AllUppercase)
        # self.tcf.fontCapitalization()
        self.labText_1.setCurrentCharFormat(self.tcf)


        self.labText_2.setFont(self.font)
        self.labText_2.setPlaceholderText('輸入摩斯密碼')
        ###設定轉譯對照表###
        self.MorseCodeDict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
            'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
            'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
            '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
            '7': '--...',
            '8': '---..', '9': '----.','空格':' ',
        }
    #####生成Item###
    ##此法會造成程式衝突，不能多重輸入至 TextWidget
    ## 在QT designer -> QListWidget -> QListView 中有 "isWarpping" 的選項可勾選，
    ## 使得只需一個QListWidget 就可以滿版條列
    #     for k,v in list(self.MorseCodeDict.items())[13:25]:
    #         self.lstWgt_2.addItem(f'[{k}]   {v}\n')
    #     for k,v in list(self.MorseCodeDict.items())[25:36]:
    #         self.lstWgt_3.addItem(f'[{k}]   {v}\n')
    #     self.space = list(self.MorseCodeDict.items())[-1]
    #     # self.lstWgt_3.addItem(f'{self.space[1]}{self.space[0]}')
    #     self.lstWgt_1.clicked.connect(self.assign)
    # def assign(self):
    #     self.text1 = self.lstWgt_1.currentItem().text()[1]
    #     self.labText_1.setText(self.text1)
    #     self.text2 = self.lstWgt_1.currentItem().text()[1]
    #     self.labText_1.setText(self.text2)
    #     self.text3 = self.lstWgt_1.currentItem().text()[1]
    #     self.labText_1.setText(self.text3)

        for k,v in list(self.MorseCodeDict.items()):
             if k != '空格'and k!= list(self.MorseCodeDict.items())[-1]:
                self.lstWgt_1.addItem(f'   [{k}]   {v}\n')
             else:
                self.lstWgt_1.addItem(f'   [{v}]   {k}')

        self.text = ''
    def assign(self):
        self.text += self.lstWgt_1.currentItem().text()[4]
        self.labText_1.setText(self.text)


    def btn1Click(self,event):
        # self.startFlag = not self.startFlag
        # if self.startFlag:
            # self.btn_1.setText("結束")
            #############################
            print('加密按鈕被按了')
            # PyQt5 要取得TextEdit內容用法為.toPlainText()
            # PyQt5 要取得LineEdit內容用法為.text()
            self.msg1 = self.labText_1.toPlainText().upper()
            self.labText_1.setText(self.msg1)

            self.upThread = Pj2_UpThread()
            # self.upThread.x = self.msg
            # print(self.upThread.x)
            print(self.upThread.ltom(self.msg1))
            self.labText_2.setText(self.upThread.ltom(self.msg1))
        # else:
        #     self.upThread.runFlag = False
    def btn2Click(self,event):
         # self.startFlag = not self.startFlag
         # if self.startFlag:
            print('解密按鈕被按了')
            #PyQt5 要取得TextEdit內容用法為.toPlainText()
            #PyQt5 要取得LineEdit內容用法為.text()
            self.msg2 =self.labText_2.toPlainText()
            self.downThread = Pj2_DownThread()
            # self.downThread.y =self.msg2
            # print(self.downThread.y)
            print(self.downThread.mtol(self.msg2))
            self.labText_1.setText(self.downThread.mtol(self.msg2))
         # else:
         #    self.downThread.runFlag = False

    def closeEvent(self,event):
        self.upThread = False
        self.downThread = False
        print("關掉視窗")


if __name__=='__main__':
    app = QApplication(sys.argv)
    m = MorseCode()
    m.show()
    app.exec()