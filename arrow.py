import math

from PyQt5.QtCore import Qt, QLineF, QPointF, QRectF, QSizeF
from PyQt5.QtGui import QPolygonF, QColor, QPen
from PyQt5.QtWidgets import QGraphicsLineItem, QGraphicsItem


class Arrow(QGraphicsLineItem):
    type = QGraphicsItem.UserType + 4

    def __init__(self, start_item, end_item, parent=None):
        super().__init__(parent=parent)

        self.myStartItem = start_item
        self.myEndItem = end_item

        self.arrowHead = QPolygonF()
        self.myColor = QColor(Qt.black)

        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setPen(QPen(self.myColor, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))

    def setColor(self, color):
        self.myColor = color

    def startItem(self):
        return self.myStartItem

    def endItem(self):
        return self.myEndItem

    def boundingRect(self):
        extra = (self.pen().width() + 20) / 2.0

        return QRectF(
            self.line().p1(),
            QSizeF(self.line().p2().x() - self.line().p1().x(),
                   self.line().p2().y() - self.line().p1().y())
        ).normalized().adjusted(-extra, -extra, extra, extra)

    def shape(self):
        path = super().shape()  # QGraphicsLineItem.shape(self)
        path.addPolygon(self.arrowHead)

        return path

    def updatePosition(self):
        line = QLineF(
            self.mapFromItem(self.myStartItem, 0, 0),
            self.mapFromItem(self.myEndItem, 0, 0)
        )
        self.setLine(line)

    def paint(self, painter, option, widget):
        if self.myStartItem.collidesWithItem(self.myEndItem):
            return

        my_pen = self.pen()
        my_pen.setColor(self.myColor)
        arrow_size = 20
        painter.setPen(my_pen)
        painter.setBrush(self.myColor)

        center_line = QLineF(self.myStartItem.pos(), self.myEndItem.pos())
        end_polygon = self.myEndItem.polygon()
        p1 = end_polygon.first() + self.myEndItem.pos()
        intersect_point = QPointF()
        for i in range(1, end_polygon.count()):
            p2 = end_polygon.at(i) + self.myEndItem.pos()
            poly_line = QLineF(p1, p2)
            intersection_type = poly_line.intersect(center_line, intersect_point)
            if intersection_type == QLineF.BoundedIntersection:
                break
            p1 = p2

        self.setLine(QLineF(intersect_point, self.myStartItem.pos()))

        angle = math.atan2(-self.line().dy(), self.line().dx())

        arrow_p1 = self.line().p1() + + QPointF(math.sin(angle + math.pi / 3) * arrow_size,
                                                math.cos(angle + math.pi / 3) * arrow_size)

        arrow_p2 = self.line().p1() + QPointF(math.sin(angle + math.pi - math.pi / 3) * arrow_size,
                                              math.cos(angle + math.pi - math.pi / 3) * arrow_size)

        self.arrowHead.clear()
        self.arrowHead << self.line().p1() << arrow_p1 << arrow_p2

        painter.drawLine(self.line())
        painter.drawPolygon(self.arrowHead)
        if self.isSelected():
            painter.setPen(QPen(self.myColor, 1, Qt.DashLine))
            my_line = self.line()
            my_line.translate(0, 4.0)
            painter.drawLine(my_line)
            my_line.translate(0, -8.0)
            painter.drawLine(my_line)
