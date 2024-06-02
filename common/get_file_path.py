import sys
from PyQt5.QtWidgets import QApplication, QFileDialog
from common.context import Context

context = Context()


def get_file_path():
    app = QApplication(sys.argv)
    file_path, _ = QFileDialog.getOpenFileName(None, 'Select file', '', 'Tous les fichiers (*)')
    context.set("FILE_PATH", file_path)
