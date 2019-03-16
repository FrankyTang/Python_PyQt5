from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QMovie
import sys
from check_gif_main import *

import os
import glob
from shutil import move

class mWindow(QMainWindow, Ui_check_gif_window):
    def __init__(self, parent=None):
        super(mWindow, self).__init__(parent)
        self.setupUi(self)

        self.btn_load.clicked.connect(self.on_click_load)
        self.btn_save.clicked.connect(self.on_click_save)
        self.btn_discard.clicked.connect(self.on_click_discard)
        self.show()

        # pass folder and error folder
        self.pass_fodler = r'D:\gif\01_pass'
        self.error_folder = r'D:\gif\02_error'

        # record current path
        self.curr_path = None
        # record path need to move
        self.src_path = None

    def on_click_load(self):
        # dir_path = QFileDialog.getExistingDirectory(self, "choose directory", "D:")
        self.gif_list = glob.glob(os.path.join(r'D:\gif\true_positives', '*'))
        self.show_gif()


    def on_click_save(self):
        self.src_path = self.curr_path
        self.show_gif()

        # move current gif to save folder
        self.move_gif(self.pass_fodler)

    def on_click_discard(self):
        self.src_path = self.curr_path
        self.show_gif()

        # move current gif to discard folder
        self.move_gif(self.error_folder)

    def move_gif(self, dst_folder):
        # move gif to new folder
        basename = os.path.basename(self.src_path)
        new_path = os.path.join(dst_folder, basename)
        move(self.src_path, new_path)

    def show_gif(self):
        # show gif to label
        self.curr_path = self.gif_list.pop()
        self.gif = QMovie(self.curr_path)
        self.label_1.setMovie(self.gif)
        self.gif.start()


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = mWindow()
    window.show()
    sys.exit(app.exec_())