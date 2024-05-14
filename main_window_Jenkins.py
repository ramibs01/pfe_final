import sys
import os
from PyQt5.QtCore import QRectF, pyqtSlot, QSize, QRect, Qt
from PyQt5.QtGui import QFont, QBrush, QPixmap, QIcon, QKeySequence, QPainter, QIntValidator
from PyQt5.QtWidgets import QMainWindow, QGraphicsTextItem, QGraphicsItem, QHBoxLayout, QWidget, QAbstractButton, \
    QGraphicsView, QMessageBox, QToolButton, QGridLayout, QLabel, QListWidgetItem, QAction, QButtonGroup, QListWidget, \
    QToolBox, QSizePolicy, QMenu, QFontComboBox, QComboBox, QApplication,QTreeWidgetItem,QTreeWidget,QVBoxLayout

from PyQt5.QtWidgets import QTreeWidgetItem
import subprocess
from diagram_scene import DiagramScene, DiagramItem
from cell_list_widget import CellListWidget
from diagram_view import DiagramView
from arrow import Arrow
from parameters_extraction import parameter_xml_file
from generate import GenerateWidget

from generate_pom import GeneratePomWidget
from generate_jelly import GenerateJellyWidget
from check_generated import CheckGeneratedWidget
from generate_hpi import GenerateHPIWidget

InsertTextButton = 10

COLORKEY = {'black': Qt.black, 'white': Qt.white, 'red': Qt.red, 'blue': Qt.blue, 'yellow': Qt.yellow}


def create_color_tool_button_icon(image_file, color):
    pixmap = QPixmap(50, 80)
    pixmap.fill(Qt.transparent)
    painter = QPainter(pixmap)
    image = QPixmap(image_file)
    # Draw icon centred horizontally on button.
    target = QRect(4, 0, 42, 43)
    source = QRect(0, 0, 42, 43)
    painter.fillRect(QRect(0, 60, 50, 80), color)
    painter.drawPixmap(target, image, source)
    painter.end()

    return QIcon(pixmap)


class MainWindowJenkins(QMainWindow):
    def __init__(self):
        super().__init__()

        self.message = ""
        self.createActions()
        self.createMenus()
        self.createToolBox()

        self.scene = DiagramScene(self.itemMenu, self)
        self.scene.setSceneRect(QRectF(0, 0, 5000, 5000))
        self.scene.itemInserted[DiagramItem].connect(self.itemInserted)
        
        self.scene.itemSelected[QGraphicsItem].connect(self.itemSelected)
        self.createToolbars()

        layout = QHBoxLayout()
        layout.addWidget(self.toolBox)
        self.view = DiagramView(self.scene)  # QGraphicsView(self.scene)
        self.view.zoomSignal[int].connect(self.sceneScaleAutoChanged)
        layout.addWidget(self.view)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        self.setWindowTitle('Generate your plugin')
        self.setUnifiedTitleAndToolBarOnMac(True)
        self.setWindowIcon(QIcon("Icons_home/Mon projet.png"))
        self.parameters_dict = parameter_xml_file()

        self.generate_pom_widget = None
        
    @pyqtSlot(DiagramItem)
    def itemInserted(self, item):
        self.pointerTypeGroup.button(DiagramScene.mode.MoveItem.value).setChecked(True)
        self.scene.setMode(DiagramScene.mode(self.pointerTypeGroup.checkedId()))
        list_widget = self.toolBox.currentWidget()
        list_widget.clearSelection()
        self.setDragOrNoDrag()
        #self.buttonGroup.button(item.diagram_type().value).setChecked(False)

    @pyqtSlot(QGraphicsTextItem)
    def textInserted(self, item):
        # self.buttonGroup.button(InsertTextButton).setChecked(False)
        self.scene.setMode(DiagramScene.mode(self.pointerTypeGroup.checkedId()))

    @pyqtSlot(QGraphicsItem)
    def itemSelected(self, text_item):
        font = text_item.font()
        #self.fontCombo.setCurrentFont(font)
        self.fontSizeCombo.setEditText(str(font.pointSize()))
        self.boldAction.setChecked(font.weight() == QFont.Bold)
        self.italicAction.setChecked(font.italic())
        self.underlineAction.setChecked(font.underline())

    @pyqtSlot()
    def bringToFront(self):
        if len(self.scene.selectedItems()) == 0:
            return

        selected_item = self.scene.selectedItems()[0]
        overlap_items = selected_item.collidingItems()

        z_value = 0
        for item in overlap_items:
            if item.zValue() >= z_value and item.type() == DiagramItem.Type:
                z_value = item.zValue() + 0.1
        selected_item.setZValue(z_value)

    @pyqtSlot()
    def sendToBack(self):
        if len(self.scene.selectedItems()) == 0:
            return

        selected_item = self.scene.selectedItems()[0]
        overlap_items = selected_item.collidingItems()

        z_value = 0.
        for item in overlap_items:
            if item.zValue() <= z_value and item.type() == DiagramItem.Type:
                z_value = item.zValue() - 0.1
        selected_item.setZValue(z_value)

    @pyqtSlot()
    def deleteItem(self):
        selected_items = self.scene.selectedItems()
        for item in selected_items:
            if isinstance(item, Arrow):
                self.scene.removeItem(item)
                arrow = item
                arrow.startItem().removeArrow(arrow)
                arrow.endItem().removeArrow(arrow)

        selected_items = self.scene.selectedItems()
        for item in selected_items:
            if item.type() == DiagramItem.Type:
                item.removeArrows()
                text_item = item.getTextItem()
                self.scene.removeItem(text_item)
                self.scene.removeItem(item)

        selected_items = self.scene.selectedItems()
        for item in selected_items:
            self.scene.removeItem(item)

    @pyqtSlot(QAbstractButton)
    def pointerGroupClicked(self, button):
        self.scene.setMode(DiagramScene.mode(self.pointerTypeGroup.checkedId()))
        self.setDragOrNoDrag()

    def setDragOrNoDrag(self):
        if self.scene.myMode == DiagramScene.mode.DragScene:
            self.view.setDragMode(QGraphicsView.ScrollHandDrag)
        else:
            self.view.setDragMode(QGraphicsView.NoDrag)

 
    @pyqtSlot()
    def textButtonTriggered(self):
        self.scene.setTextColor(self.textAction.data())

    @pyqtSlot()
    def fillButtonTriggered(self):
        self.scene.setItemColor(self.fillAction.data())

    @pyqtSlot()
    def lineButtonTriggered(self):
        self.scene.setLineColor(self.lineAction.data())

  

    @pyqtSlot(str)
    def sceneScaleChanged(self, scale):
        new_scale = float(scale.strip('%')) / 100.
        old_matrix = self.view.transform()
        self.view.resetTransform()
        self.view.translate(old_matrix.dx(), old_matrix.dy())
        self.view.scale(new_scale, new_scale)

    @pyqtSlot(int)
    def sceneScaleAutoChanged(self, scale):
        scale_str = str(scale) + '%'
        self.sceneScaleCombo.currentTextChanged[str].disconnect()
        self.sceneScaleCombo.setCurrentText(scale_str)
        self.sceneScaleCombo.currentTextChanged[str].connect(self.sceneScaleChanged)

    @pyqtSlot()
    def about(self):
        QMessageBox.about(self, 'About Application',
                          "The <b>Plugin Generator</b> prototype <br>"
                          """To generate a plugin:<br> - First, you will be happy because this application can 
                          do more than you can imagine.<br> - With a simple diagram, you can configure your specific 
                          plugin.<br> - However, you need to be careful and respect the hierarchy and links 
                          between items. """)


    def refresh_my_app(self):
        self.close()
        self.show()

    def createCellWidget(self, text, type):
        item = DiagramItem(type, self.itemMenu)
        icon = QIcon(item.image())

        button = QToolButton()
        button.setIcon(icon)
        button.setIconSize(QSize(50, 50))
        button.setCheckable(True)
        self.buttonGroup.addButton(button, type)

        layout = QGridLayout()
        layout.addWidget(button, 0, 0, Qt.AlignHCenter)
        layout.addWidget(QLabel(text), 1, 0, Qt.AlignCenter)

        widget = QWidget()
        widget.setLayout(layout)

        return widget



    def check_linked_items_present(self):
    # Iterate through all items in the scene
        for item in self.scene.items():
        # If the item is a DiagramItem and has arrows (linked to other items), return True
            if isinstance(item, DiagramItem) and item.arrows:
                return True
    # If no linked items are found, return False
        return False

    def showMessageBox(self):
        # Create and show the message box
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Java File Generated successfully!")
        msgBox.setWindowTitle("Java File")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgBox.buttonClicked.connect(self.msgButtonClick)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')

    def msgButtonClick(self, i):
        print("Button clicked is:", i.text())

    def generate_widget(self):
        if self.scene.items():
            linked_items_present = self.check_linked_items_present()
            if linked_items_present:
                generator = GenerateWidget( "C:/Users/rami dob/Downloads/pfe_application - Copy/pfe_application/check_generated")
                generator.generate_java_file()
                self.showMessageBox()
               
            else:
                print("No linked items present in the scene.")
        else:
            print("No dropped items in the scene.")
    def generate_pom(self):
        self.generate_pom_widget = GeneratePomWidget()
        self.generate_pom_widget.show()

    def generate_jelly(self):
        self.generate_jelly_widget = GenerateJellyWidget()
        self.generate_jelly_widget.show()

    def check_generated(self):
        self.check_generated_widget = CheckGeneratedWidget()
        self.check_generated_widget.show()

    def generate_hpi(self):
        self.generate_hpi_widget = GenerateHPIWidget()
        self.generate_hpi_widget.show()

   # def delete_files(self):
   #     directory = "C:/Users/rami dob/Downloads/pfe_application - Copy/pfe_application/check_generated"
    #    for file_name in os.listdir(directory):
     #       file_path = os.path.join(directory, file_name)
      #      os.remove(file_path)
       # print("Files deleted successfully!")

    def closeEvent(self, event):
        # Delete files before closing the window
        #self.delete_files()
        event.accept()

    def createCellListWidgetItem(self, kay):
        item = DiagramItem(kay, self.itemMenu)
        icon = QIcon(item.image())

        list_widget_item = QListWidgetItem(kay)
        list_widget_item.setIcon(icon)
        list_widget_item.setData(Qt.UserRole, DiagramItem.diagram_type[kay])

        return list_widget_item
    def createActions(self):
        self.toFrontAction = QAction(QIcon("Icons_home/images/bringtofront.png"),
                                     'Bring to &Front', self)
        self.toFrontAction.setShortcut('Ctrl+F')
        self.toFrontAction.setStatusTip('Bring item to front')
        self.toFrontAction.triggered.connect(self.bringToFront)

        self.sendBackAction = QAction(QIcon("Icons_home/images/sendtoback.png"),
                                      'Send to &Back', self)
        self.sendBackAction.setShortcut('Ctrl+T')
        self.sendBackAction.setStatusTip('Send item to back')
        self.sendBackAction.triggered.connect(self.sendToBack)

        self.deleteAction = QAction(QIcon("Icons_home/images/delete.png"),
                                    '&Delete', self)
        self.deleteAction.setShortcut('Delete')
        self.deleteAction.setStatusTip('Delete item from diagram')
        self.deleteAction.triggered.connect(self.deleteItem)

        self.refreshAction = QAction(QIcon("Icons_home/refresh_48px.png"),
                                     '&Refresh', self)
        self.refreshAction.setShortcut('Refresh')
        self.refreshAction.setStatusTip('Refreshing')
        self.refreshAction.triggered.connect(self.refresh_my_app)
                                

        self.generateAction = QAction(QIcon("Icons_home/Code_48px.png"),
                                      '&Generate Java File', self)
        self.generateAction.setShortcut('Generate')
        self.generateAction.setStatusTip('Generate')
        self.generateAction.triggered.connect(self.generate_widget)

        self.generatePom = QAction(QIcon("Icons_home/xml-removebg-preview.png"),
                                      '&Generate pom.xml', self)
        self.generatePom.setShortcut('GeneratePom')
        self.generatePom.setStatusTip('GeneratePom')
        self.generatePom.triggered.connect(self.generate_pom)

        self.generateJelly = QAction(QIcon("Icons_home/jelly-removebg-preview.png"),
                                      '&Generate index.jelly', self)
        self.generateJelly.setShortcut('GenerateJelly')
        self.generateJelly.setStatusTip('GenerateJelly')
        self.generateJelly.triggered.connect(self.generate_jelly)


        self.generatehpi = QAction(QIcon("Icons_home/hpi-removebg-preview.png"),
                                      '&Generate your .HPi', self)
        self.generatehpi.setShortcut('generatehpi')
        self.generatehpi.setStatusTip('generatehpi')
        self.generatehpi.triggered.connect(self.generate_hpi)


        self.CheckGenerated = QAction(QIcon("Icons_home/preview-removebg-preview.png"),
                                      '&Check your generated files', self)
        self.CheckGenerated.setShortcut('CheckGenerated')
        self.CheckGenerated.setStatusTip('CheckGenerated')
        self.CheckGenerated.triggered.connect(self.check_generated)


        self.exitAction = QAction(QIcon('Icons_home/logout_rounded_left_64px.png'), 'E&xit', self)
        self.exitAction.setShortcut(QKeySequence.Quit)
        self.exitAction.setStatusTip('Quit Scenediagram example')
        self.exitAction.triggered.connect(self.close)
    

        self.aboutAction = QAction('A&bout', self)
        self.aboutAction.setShortcut('F1')
        self.aboutAction.triggered.connect(self.about)

    def createToolBox(self):
        self.buttonGroup = QButtonGroup(self)
        self.buttonGroup.setExclusive(False)

        layout = QGridLayout()


        text_button = QToolButton()
        text_button.setCheckable(True)
        text_button.setIconSize(QSize(500, 50))
        text_layout = QGridLayout()
        text_layout.addWidget(text_button, 0, 0, Qt.AlignHCenter)
        text_layout.addWidget(QLabel('Text'), 1, 0, Qt.AlignCenter)
        text_widget = QWidget()
        text_widget.setLayout(text_layout)
        layout.addWidget(text_widget, 1, 1)
        layout.setRowStretch(3, 10)
        layout.setColumnStretch(2, 10)
        item_widget = QWidget()
        item_widget.setLayout(layout)

        
        list_widget = CellListWidget()
        list_widget.setViewMode(QListWidget.IconMode)
        list_widget.setAcceptDrops(False)
        list_widget.setSpacing(10)

        for names in DiagramItem.diagram_type.keys():
            list_widget.addItem(self.createCellListWidgetItem(names))

        self.toolBox = QToolBox()
        self.toolBox.setSizePolicy(QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Ignored))
        self.toolBox.setMinimumWidth(list_widget.sizeHint().width())
        self.toolBox.addItem(list_widget, 'Classes') 


    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu('&File')
        self.fileMenu.addAction(self.exitAction)

        self.itemMenu = self.menuBar().addMenu('&Item')
        self.itemMenu.addSeparator()
        self.itemMenu.addAction(self.toFrontAction)
        self.itemMenu.addAction(self.sendBackAction)

        self.aboutMenu = self.menuBar().addMenu('&Help')
        self.aboutMenu.addAction(self.aboutAction)
 

    def createToolbars(self):
        self.editToolBar = self.addToolBar('Edit')
        self.editToolBar.addAction(self.refreshAction)
        self.editToolBar.addAction(self.deleteAction)
        self.editToolBar.addAction(self.toFrontAction)
        self.editToolBar.addAction(self.sendBackAction)


        pointer_button = QToolButton()
        pointer_button.setCheckable(True)
        pointer_button.setChecked(True)
        pointer_button.setIcon(QIcon('Icons_home/images/pointer.png'))
        line_pointer_button = QToolButton()
        line_pointer_button.setCheckable(True)
        line_pointer_button.setIcon(QIcon('Icons_home/images/linepointer.png'))
        hand_grab_button = QToolButton()
        hand_grab_button.setCheckable(True)
        hand_grab_button.setIcon(QIcon('Icons_home/images/hand.png'))

        self.pointerTypeGroup = QButtonGroup(self)
        self.pointerTypeGroup.addButton(pointer_button, DiagramScene.mode.MoveItem.value)
        self.pointerTypeGroup.addButton(line_pointer_button, DiagramScene.mode.InsertLine.value)
        self.pointerTypeGroup.addButton(hand_grab_button, DiagramScene.mode.DragScene.value)

        self.pointerTypeGroup.buttonClicked[QAbstractButton].connect(self.pointerGroupClicked)

        self.sceneScaleCombo = QComboBox()
        scales = ["50%", "75%", "100%", "125%", "150%"]
        self.sceneScaleCombo.addItems(scales)
        self.sceneScaleCombo.setCurrentIndex(2)
        self.sceneScaleCombo.currentTextChanged[str].connect(self.sceneScaleChanged)

        self.pointerToolbar = self.addToolBar('Pointer type')
        self.pointerToolbar.addWidget(pointer_button)
        self.pointerToolbar.addWidget(line_pointer_button)
        self.pointerToolbar.addWidget(hand_grab_button)
        self.pointerToolbar.addWidget(self.sceneScaleCombo)

        self.generateToolBar = self.addToolBar('Generate')  
        self.generateToolBar.addAction(self.generateAction)

        #self.generateToolBar = self.addToolBar('GeneratePom')
        self.generateToolBar.addAction(self.generatePom)

        self.generateToolBar.addAction(self.generateJelly)

        self.generateToolBar = self.addToolBar('CheckGenerated')
        self.generateToolBar.addAction(self.CheckGenerated)

        self.generateToolBar = self.addToolBar('Generatehpi')
        self.generateToolBar.addAction(self.generatehpi)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindowJenkins()
    window.show()
    app.exec_()
