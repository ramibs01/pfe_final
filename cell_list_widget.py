from PyQt5.QtCore import Qt, QMimeData, QSize
from PyQt5.QtGui import QDrag
from PyQt5.QtWidgets import QListWidget


class CellListWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def mouseMoveEvent(self, event):
        item = self.currentItem()
        item_id = item.data(Qt.UserRole)

        drag = QDrag(self)
        mime_data = QMimeData()
        mime_data.setText(str(item_id))
        drag.setMimeData(mime_data)

        icon = item.icon()
        icon_pixmap = icon.pixmap(icon.actualSize(QSize(48, 48)))
        drag.setPixmap(icon_pixmap)

        drag.exec_()
