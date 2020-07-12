import sys
from design import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.btnEscolherArquivo.clicked.connect(self.abrir_imagem)
        self.btnRedimensionar.clicked.connect(self.redimensionar_imagem)
        self.btnSalvar.clicked.connect(self.salvar_imagem)

    def colocar_imagem(self, imagem: QPixmap, caminho: str = None):
        self.nova_imagem = imagem
        self.inputCaminhoImagem.setText(caminho if caminho else self.caminho_original)
        self.labelImagem.setPixmap(imagem)
        self.inputLargura.setText(str(imagem.width()))
        self.inputAltura.setText(str(imagem.height()))

    def abrir_imagem(self):
        text = self.btnEscolherArquivo.text()
        self.btnEscolherArquivo.setText('Abrindo selecionador...')
        caminho_imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Selecione uma imagem',
            r'c:\users\%username%\pictures',
            # options=QFileDialog.DontUseNativeDialog
        )
        self.caminho_original = caminho_imagem
        self.imagem_original = QPixmap(caminho_imagem)
        self.colocar_imagem(self.imagem_original, self.caminho_original)
        self.btnEscolherArquivo.setText(text)

    def redimensionar_imagem(self):
        largura = int(self.inputLargura.text())
        self.colocar_imagem(self.imagem_original.scaledToWidth(largura))

    def salvar_imagem(self):
        caminho_imagem, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Escolha um local para salvar sua imagem',
            r'c:\users\%username%\pictures',
            # options=QFileDialog.DontUseNativeDialog
        )
        self.nova_imagem.save(caminho_imagem, 'PNG')


if __name__ == '__main__':
    qapp = QApplication(sys.argv)
    app = App()
    app.show()
    qapp.exec_()
