import sys
import folium
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import os

class MapViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Map Viewer")
        self.setGeometry(100, 100, 1200, 600)  # Adjust the size to fit both maps

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QHBoxLayout()
        central_widget.setLayout(layout)

        # Create and save maps
        self.create_and_save_maps()

        # Create QWebEngineView widgets for each map
        self.map1_view = QWebEngineView()
        self.map2_view = QWebEngineView()

        # Add the map views to the horizontal layout
        layout.addWidget(self.map1_view)
        layout.addWidget(self.map2_view)

        # Load HTML files
        self.map1_view.setUrl(QUrl.fromLocalFile(os.path.abspath('map1.html')))
        self.map2_view.setUrl(QUrl.fromLocalFile(os.path.abspath('map2.html')))

    def create_and_save_maps(self):
        # Create the first map centered on La Jolla, CA
        map1 = folium.Map(location=[32.9, -117.2], zoom_start=10)
        map1.save('map1.html')

        # Create the second map centered on Torrance, CA
        map2 = folium.Map(location=[33.8358, -118.3406], zoom_start=10)
        map2.save('map2.html')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = MapViewer()
    viewer.show()
    sys.exit(app.exec_())
