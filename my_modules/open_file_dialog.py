#! env python
# -*- coding: utf-8 -*-
# Date: 2017/12/14
# Filename: open_file_dialog

import sys

from PyQt5.QtWidgets import *
from my_modules.ui.open_file_dialog_ui import Ui_Dialog

__author__ = 'noda'
__date__ = "2017/12/14"


class OpenDialg(QDialog):
    def __init__(self, parent=None):
        super(OpenDialg, self).__init__(parent)
        # Initialize
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Button
        self.ui.pushButton_file.clicked.connect(self.open_file)
        self.ui.pushButton_folder.clicked.connect(self.open_folder)

        # Variables
        self.file_path = None
        self.folder_path = None

    def open_file(self):
        fd = QFileDialog()
        fp = fd.getOpenFileNames()[0]
        if len(fp) == 1:
            fp = fp[0]
        self.file_path = fp

    def open_folder(self):
        fd = QFileDialog()
        fp = fd.getExistingDirectory()
        self.folder_path = fp


def get_path():
    """
    ファイルパス及びフォルダパスの取得

    :return: file path, folder path
    """
    app = QApplication(sys.argv)
    dialog = OpenDialg()
    dialog.show()
    app.exec_()
    return dialog.file_path, dialog.folder_path


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = OpenDialg()
    window.show()
    sys.exit(app.exec_())
