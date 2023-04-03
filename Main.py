#PyQt5 är en Python-bindning för Qt-biblioteket, som är en populär plattformsoberoende ramverk för att skapa grafiska användargränssnitt. PyQt5 ger möjlighet att skapa kraftfulla GUI-applikationer för Windows, Mac OS X och Linux, och det är helt skrivet i Python.

#Det används för att skapa grafiska användargränssnitt för applikationer som har många användningsområden, inklusive datavisualisering, simuleringsprogram, bilddesignverktyg, datorspel och mycket mer.

#PyQt5 innehåller många verktyg som kan användas för att skapa en mängd olika grafiska användargränssnitt, inklusive knappar, rullgardinsmenyer, rullningsfält, rutor, listor och dialogrutor. Det ger också möjlighet att skapa anpassade grafiska element som är utformade för att passa specifika applikationer. PyQt5 kan också användas för att skapa avancerade program som inkluderar flera fönster, verktygsfält och menyer.

import sys
import random
from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QPainter, QColor, QFont, QBrush
from PyQt5.QtWidgets import QApplication, QWidget

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Uppg9')

    def paintEvent(self, event):
        qp = QPainter(self)
        # Rita text
        qp.setFont(QFont('Arial', 20))
        qp.drawText(self.rect(), Qt.AlignCenter, 'YES!')

        # Rita punkter
        qp.setPen(QColor(255, 0, 0))
        qp.drawPoint(50, 50)
        for i in range(2000):
            y = random.randint(0, self.width())
            x = random.randint(0, self.height())
            qp.drawPoint(x, y)
            

        # Rita rektanglar
        qp.setPen(QColor(0, 0, 255))
        qp.drawRect(200, 200, 100, 50)

        # Rita fyllda rektanglar med QBrush
        brush = QBrush(Qt.DiagCrossPattern)
        qp.setBrush(brush)
        qp.fillRect(QRect(50, 200, 100, 50), QColor(0, 255, 0))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())