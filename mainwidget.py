from PySide6.QtWidgets import QWidget, QAbstractItemView
from PySide6.QtGui import QPixmap, QIcon
from ui_mainwidget import Ui_MainWidget
from devicesmodel import DevicesModel
import rc_intercom_flasher
import parted


class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.ui = Ui_MainWidget()
        self.ui.setupUi(self)

        self.ui.refreshButton.clicked.connect(self.updateDevices)

        self.devices = []

        self.setWindowIcon(QIcon(QPixmap(":/icons/logo.png")))
        # data = [
        #     ["/dev/sda", "Hitachi AT-60", "37 Gb"],
        #     ["/dev/sdb", "Massive Storage", "3,7 Gb"]
        # ]

        self.ui.devicesView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.devicesView.setSelectionMode(QAbstractItemView.SingleSelection)

        self.model = DevicesModel([])
        self.ui.devicesView.setModel(self.model)
        self.updateDevices()

    def updateDevices(self):
        self.devices = [dev for dev in parted.getAllDevices()]
        data = [[d.path, d.model, str(d.length * 512 / 1024 / 1024 / 1024) + " Гб"] for d in self.devices]
        self.model.setDevices(data)
        self.ui.devicesView.resizeColumnsToContents()

        # usb = parted.getDevice('/dev/sdb')
        # print(usb)
        # disk = parted.newDisk(usb)
        # partitionsDesc = [(part.type, part.number) for part in disk.partitions]
        # print(disk.partitions[0])
        # # print(disk.partitions[1])
        # print(partitionsDesc)
        # print(disk.partitions[0].fileSystem.type)