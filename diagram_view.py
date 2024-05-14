from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QGraphicsView


class DiagramView(QGraphicsView):
    zoomScale = 100

    zoomSignal = pyqtSignal(int)

    def __init__(self, scene, parent=None):
        super().__init__(parent=parent)

        self.setScene(scene)

        self.setAcceptDrops(True)

    def setupMatrix(self, value):
        if value > 0:
            self.zoomScale += 25
        else:
            self.zoomScale -= 25

        if self.zoomScale > 150:
            self.zoomScale = 150
        elif self.zoomScale < 50:
            self.zoomScale = 50

        new_scale = self.zoomScale / 100.

        old_matrix = self.transform()
        self.resetTransform()
        self.translate(old_matrix.dx(), old_matrix.dy())
        self.scale(new_scale, new_scale)

        self.zoomSignal.emit(self.zoomScale)

    def wheelEvent(self, event):
        self.setupMatrix(event.angleDelta().y())
        event.accept()
