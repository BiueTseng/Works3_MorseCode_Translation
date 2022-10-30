from PyQt5.QtCore import QThread, pyqtSignal

class Pj2_UpThread(QThread):
    phoneUP = pyqtSignal(str)
    def __init__(self,parent=None):
        super().__init__(parent)
        # self.runFlag = True
        # 設定Morse Code字典
        self.MorseCodeDict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
            'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
            'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
            '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
            '7': '--...',
            '8': '---..', '9': '----.',
        }
        # 將MorseCodeDict 字典轉向
        # self.revMorseCodeDict = {v: k for k, v in self.MorseCodeDict.items()}
        # print(revMorseCodeDict)
        ###加密
    def ltom(self,x):
        self.transLetter = ''
        for unit in x:
            if unit != ' ':
                self.transLetter += self.MorseCodeDict[unit] + ' '
            # print(transResult)
            else:
                self.transLetter += ' '
        return self.transLetter
    # def run(self):
    #     self.phoneUP.emit(self.transLetter)
# message = "I YOU"
# print(Pj2_UpThread.run(message))






















