from PySide.QtCore import *
from PySide.QtGui import *
import icons
import about_UIs

class aboutClass(QDialog, about_UIs.Ui_Dialog):
    def __init__(self, parent):
        super(aboutClass, self).__init__(parent)
        self.setupUi(self)
        self.title_lb.setText(self.title_lb.text()+str(parent.ver))
        self.text_link_lb.setText(text)
        self.icon_lb.setPixmap(QPixmap(icons.icons['pw']).scaled(40,40, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.donate_btn.setMinimumHeight(35)
        self.donate_btn.setIconSize(QSize(24,24))
        self.donate_btn.setIcon(QIcon(icons.icons['donate']))
        self.donate_btn.clicked.connect(lambda :parent.openLink('donate'))


text = '''PaulWinex 2015
Any question or bug report: paulwinex@gmail.com'''