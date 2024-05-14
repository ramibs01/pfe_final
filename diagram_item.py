
from parameters_extraction import dict_module_name_number, parameter_xml_file


from PyQt5.QtCore import QPointF, Qt
from PyQt5.QtGui import QPolygonF, QPixmap, QPainter, QPen
from PyQt5.QtWidgets import QGraphicsPolygonItem, QGraphicsItem


class DiagramItem(QGraphicsPolygonItem):
    Type = QGraphicsItem.UserType + 15
    diagram_type = dict_module_name_number()
    diagram_item = parameter_xml_file()

    def __init__(self, diagram_type, context_menu, parent=None):
        super().__init__(parent=parent)
        self.textItem = None
        self.myPolygon = QPolygonF()
        self.arrows = []
        self.myName = ''
        self.widget = None
        self.myDiagramType = diagram_type
        self.myContextMenu = context_menu

        for module_name in list(self.diagram_type.keys()):
            if self.myDiagramType == module_name:
                self.myPolygon << QPointF(-50, -50) << QPointF(50, -50) << QPointF(50, 50) << QPointF(-50,
                                                                                                      50) << QPointF(
                    -50, -50)

        self.setPolygon(self.myPolygon)
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges, True)

    def setMyName(self, my_name):
        self.myName = my_name

    def getMyName(self):
        return self.myName

    def diagramType(self):
        return self.myDiagramType

    def polygon(self):
        return self.myPolygon

    def type(self):
        return self.Type

    def setTextItemOwnership(self, text_item):
        self.textItem = text_item

    def getTextItem(self):
        return self.textItem

    def removeArrow(self, arrow):
        for arr in self.arrows:
            if arr == arrow:
                self.arrows.remove(arr)

    def removeArrows(self):
        # need a copy here since removeArrow() will
        # modify the arrows container
        arrows_copy = self.arrows.copy()
        for arr in arrows_copy:
            arr.startItem().removeArrow(arr)
            arr.endItem().removeArrow(arr)
            self.scene().removeItem(arr)

    def addArrow(self, arrow):
        self.arrows.append(arrow)

    def image(self):
        pixmap = QPixmap(250, 250)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        painter.setPen(QPen(Qt.black, 8))
        painter.translate(125, 125)
        painter.drawPolyline(self.myPolygon)
        painter.end()

        return pixmap

    def contextMenuEvent(self, event):
        self.scene().clearSelection()
        self.setSelected(True)
        self.myContextMenu.exec_(event.screenPos())

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionChange:
            for arr in self.arrows:
                arr.updatePosition()

        return value

   
