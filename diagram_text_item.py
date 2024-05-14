from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QGraphicsTextItem, QGraphicsItem


class DiagramTextItem(QGraphicsTextItem):
    Type = QGraphicsItem.UserType + 3

    lostFocus = pyqtSignal(QGraphicsTextItem)
    selectedChange = pyqtSignal(QGraphicsItem)

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.itemOwner = None

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemSelectedHasChanged:
            self.selectedChange.emit(self)
        return value

    def focusOutEvent(self, event):
        self.setTextInteractionFlags(Qt.NoTextInteraction)
        self.lostFocus.emit(self)
        super().focusOutEvent(event)

    def mouseDoubleClickEvent(self, event):
        if self.textInteractionFlags() == Qt.NoTextInteraction:
            self.setTextInteractionFlags(Qt.TextEditorInteraction)
        super().mouseDoubleClickEvent(event)

    def setItemOwner(self, item):
        self.itemOwner = item

    def getOwner(self):
        return self.itemOwner
