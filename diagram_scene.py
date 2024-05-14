from Component import Mode
from PyQt5.QtCore import pyqtSignal, Qt, QPointF, QLineF
from PyQt5.QtGui import QFont, QPen, QTransform
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsTextItem, QGraphicsItem, QGraphicsLineItem, QGraphicsView
from diagram_item import DiagramItem
from arrow import Arrow
from diagram_text_item import DiagramTextItem
from parameters_extraction import dict_module_name_number_0, number_of_parameters, dict_module_name_number_add, \
    appending_item_in_list, dict_item, appending_item_in_dict, list_of_item


class DiagramScene(QGraphicsScene):
    itemInserted = pyqtSignal(DiagramItem)
    textInserted = pyqtSignal(QGraphicsTextItem)
    itemSelected = pyqtSignal(QGraphicsItem)
    mode = Mode
    
    itemsDropped = pyqtSignal(str)
    def __init__(self, item_menu, item_type, parent=None):
        super().__init__(parent=parent)
        self.myItemType = item_type
        self.myItemMenu = item_menu
        self.myMode = DiagramScene.mode.MoveItem
        self.line = None
        self.textItem = None
        self.myItemColor = Qt.black
        self.myTextColor = Qt.black
        self.myLineColor = Qt.black
        self.myFont = QFont()
        self.typeCount = dict_module_name_number_0()
        self.module_name = ''
        self.all_dropped_items = []

    def font(self):
        return self.myFont

    def textColor(self):
        return self.myTextColor

    def itemColor(self):
        return self.myItemColor

    def lineColor(self):
        return self.myLineColor

    def isItemChange(self, type):
        items = self.selectedItems()
        for item in items:
            if item.type() == type:
                return True
        return False

    def setLineColor(self, color):
        self.myLineColor = Qt.GlobalColor(color)
        if self.isItemChange(Arrow.type):
            item = self.selectedItems()[0]
            item.setColor(self.myLineColor)
            self.update()



    def setItemColor(self, color):
        self.myItemColor = Qt.GlobalColor(color)
        if self.isItemChange(DiagramItem.Type):
            item = self.selectedItems()[0]
            item.setBrush(self.myItemColor)

    def setFont(self, font):
        self.myFont = font
        if self.isItemChange(DiagramTextItem.Type):
            item = self.selectedItems()[0]
            # At this point the selection can change so the first selected item might not be a DiagramTextItem
            if item is not None and isinstance(item, DiagramTextItem):
                item.setFont(self.myFont)

    def setMode(self, mode):
        self.myMode = mode

    def setItemType(self, type):
        self.myItemType = type

    def editorLostFocus(self, item):
        cursor = item.textCursor()
        cursor.clearSelection()
        item.setTextCursor(cursor)
        if item.getOwner() is None:
            if len(item.toPlainText()) == 0:
                self.removeItem(item)
        else:
            owner_item = item.getOwner()
            if len(item.toPlainText()) == 0:
                item.setPlainText(owner_item.getMyName())
            else:
                owner_item.setMyName(item.toPlainText())

    def insertItem(self, pos_f, text=''):
        if self.myMode == DiagramScene.mode.InsertItem:
            item = DiagramItem(self.myItemType, self.myItemMenu)
            item.setBrush(self.myItemColor)
            self.addItem(item)
            item.setPos(pos_f)
            item_label = self.myItemType + '_' + str(dict_module_name_number_add(self.myItemType)[self.myItemType])
            item.setMyName(item_label)
            text_pos = QPointF(pos_f.x(), pos_f.y() + item.boundingRect().height() / 2 + 5)
            self.setMode(DiagramScene.mode.InsertText)
            self.insertItem(text_pos, item_label)
            text_item = self.items()[0]
            text_item.setItemOwner(item)
            item.setTextItemOwnership(text_item)
            self.itemInserted.emit(item)
            self.typeCount[self.myItemType] += 1
        elif self.myMode == DiagramScene.mode.InsertLine:
            self.line = QGraphicsLineItem(
                QLineF(pos_f, pos_f)
            )
            self.line.setPen(QPen(self.myLineColor, 2))
            self.addItem(self.line)
        elif self.myMode == DiagramScene.mode.InsertText:
            self.textItem = DiagramTextItem()
            self.textItem.setFont(self.myFont)
            self.textItem.setTextInteractionFlags(Qt.TextEditorInteraction)
            self.textItem.setZValue(1000.)
            self.textItem.setPlainText(text)
            self.textItem.lostFocus[QGraphicsTextItem].connect(self.editorLostFocus)
            self.textItem.selectedChange[QGraphicsItem].connect(self.itemSelected)
            self.addItem(self.textItem)
            self.textItem.setDefaultTextColor(self.myTextColor)
            self.textItem.setPos(pos_f)
            self.textInserted.emit(self.textItem)

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.setAccepted(True)
            self.update()
        else:
            event.setAccepted(False)

    def dragMoveEvent(self, event):
        event.setAccepted(True)

    def dragLeaveEvent(self, event):
        self.update()

    def dropEvent(self, event):
        if event.mimeData().hasText():
            event.setAccepted(True)
            event_id = int(event.mimeData().text())
            self.myMode = DiagramScene.mode.InsertItem
            item_names = list(DiagramItem.diagram_type.keys())  # Get the list of item names
            dropped_items = []  # Initialize an empty list to store the dropped item names
            for i in number_of_parameters():
                if i == event_id:   
                    self.myItemType = item_names[i]  # Set the item type based on the event ID
                    dropped_item_name = self.myItemType  # Get the name of the dropped item
                    dropped_items.append(dropped_item_name)  # Add the item name to the list of dropped items
                    self.all_dropped_items.append(dropped_item_name)  # Append the dropped item name to the list of all dropped items
            self.insertItem(event.scenePos())
            print("Dropped item(s):", dropped_items)  # Print the list of dropped item names for this event
            print("All dropped items:", self.all_dropped_items)  # Print the list of all dropped item names
        self.update()


    def mousePressEvent(self, mouse_event):
        if mouse_event.button() != Qt.LeftButton or self.myMode == DiagramScene.mode.DragScene:
            return
        # insert line
        self.insertItem(mouse_event.scenePos())
        item_to_be_moved = self.itemAt(mouse_event.scenePos(), QTransform())
        if isinstance(item_to_be_moved, DiagramItem):
            item_text = item_to_be_moved.getTextItem()
            self.oldMouseX = mouse_event.scenePos().x()
            self.oldMouseY = mouse_event.scenePos().y()
            self.oldItemTextX = item_text.scenePos().x()
            self.oldItemTextY = item_text.scenePos().y()
        super().mousePressEvent(mouse_event)

    def mouseMoveEvent(self, mouse_event):
        if self.myMode == DiagramScene.mode.DragScene:
            return
        view = self.views()[-1]
        view.setDragMode(QGraphicsView.NoDrag)
        if self.myMode == DiagramScene.mode.InsertLine and self.line is not None:
            new_line = QLineF(self.line.line().p1(), mouse_event.scenePos())
            self.line.setLine(new_line)
        elif self.myMode == self.mode.MoveItem and self.mouseGrabberItem() is not None:
            item = self.mouseGrabberItem()
            if item is not None and isinstance(item, DiagramItem):
                text_item = item.getTextItem()
                new_x = mouse_event.scenePos().x()
                new_y = mouse_event.scenePos().y()
                dx = new_x - self.oldMouseX
                dy = new_y - self.oldMouseY
                text_item.setPos(QPointF(self.oldItemTextX, self.oldItemTextY) + QPointF(dx, dy))
            super().mouseMoveEvent(mouse_event)
        else:
            view.setDragMode(QGraphicsView.RubberBandDrag)
            super().mouseMoveEvent(mouse_event)

    def mouseReleaseEvent(self, mouse_event):
        if self.line is not None and self.myMode == self.mode.InsertLine:
            start_items = self.items(self.line.line().p1())
            if len(start_items) > 0 and start_items[0] == self.line:
                start_items.pop(0)
            end_items = self.items(self.line.line().p2())
            if len(end_items) > 0 and end_items[0] == self.line:
                end_items.pop(0)
            self.removeItem(self.line)
            if len(start_items) > 0 and len(end_items) > 0 and \
                    start_items[0].type() == DiagramItem.Type and \
                    end_items[0].type() == DiagramItem.Type and \
                    start_items[0] != end_items[0]:
                start_item = start_items[0]
                end_item = end_items[0]
                arrow = Arrow(start_item, end_item)
                arrow.setColor(self.myLineColor)
                start_item.addArrow(arrow)
                end_item.addArrow(arrow)
                arrow.setZValue(-1000.)
                self.addItem(arrow)
                arrow.updatePosition()
                appending_item_in_list(start_item.getMyName(), end_item.getMyName())
                print(appending_item_in_dict(list_of_item))
                
                print(dict_item)

        self.line = None
        super().mouseReleaseEvent(mouse_event)

    def get_module_name_from_diagram_scene(self):
        return self.module_name

 
