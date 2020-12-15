from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex


class DevicesModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data
        self._headers = [
            "Путь",
            "Модель",
            "Размер"
        ]

    def data(self, index, role):
        if len(self._data) == 0:
            return None
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
       return 3

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._headers[section]

    def setDevices(self, devices):
        self._data = devices
        self.layoutChanged.emit()

