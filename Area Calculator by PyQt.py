#Final assignment of Python course in sophomore year

from PySide2.QtWidgets import *
from PySide2.QtUiTools import *

# 判断一个字符串是否只包含小数或浮点数
def is_number(num):
    s = str(num)
    if s.count('.') == 1:  # 小数
        new_s = s.split('.')
        left_num = new_s[0]
        right_num = new_s[1]
        if right_num.isdigit():
            if left_num.isdigit():
                return True
            elif left_num.count('-') == 1 and left_num.startswith('-'):  # 负小数
                tmp_num = left_num.split('-')[-1]
                if tmp_num.isdigit():
                    return False
    elif s.count(".") == 0:  # 整数
        if s.isdigit():
            return True
        elif s.count('-') == 1 and s.startswith('-'):  # 负整数
            ss = s.split('-')[-1]
            if ss.isdigit():
                return False
    return False


class Stats:

    def __init__(self):
        # 从文件中加载UI定义
        # 加载在QT designer画好的UI
        self.ui = QUiLoader().load('Area Calculator by PyQt.ui')
        # 连接三个botton类对象
        self.ui.T_get_count.clicked.connect(self.Triangle)
        self.ui.P_get_count.clicked.connect(self.parallelogram)
        self.ui.C_get_count.clicked.connect(self.circular)

    # 开始时的提示
    def tip(self):
        QMessageBox().warning(None, "提示", "请先选择图形再输入", QMessageBox.Yes)

    # 三角形面积
    def Triangle(self):
        # 获取plain text edit里的内容，并通过自己写的函数判断该字符串是否只包含浮点数或小数，以下同理
        T_base = self.ui.T_input_base.toPlainText()
        T_high = self.ui.T_input_high.toPlainText()
        if (is_number(T_high) == 0 or is_number(T_base) == 0):
            # 若字符串不是纯数字或负数的弹出提示框
            QMessageBox().warning(None, "提示", "输入数据有误，请检查", QMessageBox.Yes)
        else:
            # 计算面积并添加到count文本框内
            S = float(T_base) * float(T_high) / 2
            self.ui.count.setPlainText(str(S))
        print(S)

    # 平行四边形面积
    def parallelogram(self):
        P_base = self.ui.P_input_base.toPlainText()
        P_high = self.ui.P_input_high.toPlainText()
        if (is_number(P_high) == 0 or is_number(P_base) == 0):
            QMessageBox().warning(None, "提示", "输入数据有误，请检查", QMessageBox.Yes)
        else:
            S = float(P_base) * float(P_high)
            self.ui.count.setPlainText(str(S))
        print(S)

    def circular(self):
        C_r = self.ui.C_r.toPlainText()
        if (is_number(C_r) == 0):
            QMessageBox().warning(None, "提示", "输入数据有误，请检查", QMessageBox.Yes)
        else:
            S = float(C_r) ** 2 * 3.14
            self.ui.count.setPlainText(str(S))
        print(S)


app = QApplication([])
stats = Stats()
stats.tip()
stats.ui.show()
app.exec_()
