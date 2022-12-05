from PyQt5.QtCore import QThread, pyqtSignal

class Pj2_DownThread(QThread):
    phoneDown = pyqtSignal(str)
    def __init__(self,parent = None):
        super().__init__(parent)
        # self.runFlag = True
        # 設定Morse Code字典
        self.MorseCodeDict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..',
            'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
            'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
            '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
            '7': '--...',
            '8': '---..', '9': '----.',
        }
        # 將MorseCodeDict 字典轉向
        self.revMorseCodeDict = {v: k for k, v in self.MorseCodeDict.items()}
        # print(revMorseCodeDict)
        ###解密
    def mtol(self, y):
        self.transMorse = ''
        y = y.split(sep=' ')
        # print(y)
        for unit in y:
            if unit == '':
                self.transMorse += ' '
            else:
                self.transMorse += self.revMorseCodeDict[unit]
        return self.transMorse

        #y = '..  .-.. --- ...- .  -.-- --- ..-'
        #print(mtol(y))
        # ###split用法
        # bb=''
        # wd1='..  -.-- .....'
        # aa = wd1.split(sep=' ')
        # print(aa)
        # print(len(aa))
        # print(aa[1]=='')
        #####################################################
        # def decrypt(z):
        # z = '..  -.--'
        # z += ' '
        # decipher =''
        # citext =''
        # global i
        # for letter in z:
        #     if letter != ' ':
        #         i = 0
        #         print(f"起始 i 值:{i}")
        #         citext += letter
        #         print(f"citext值: {citext}")
        #     else:
        #         i += 1
        #         print(f"第{i}次 i 值:{i}")
        #         if i == 2:
        #             decipher += ' '
        #             print('='*6)
        #             print(f"decipher值: {decipher}")
        #         else:
        #             decipher += list(MorseCodeDict.keys())[list(MorseCodeDict.values()).index(citext)]
        #             print(f"citext值: {citext}")
        #             citext = ''
        #
        # #    return decipher
        # print(decipher)

