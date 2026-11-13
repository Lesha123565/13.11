from PyQt6.QtWidgets import QMainWindow,QFrame , QHBoxLayout, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from modules.app import app 
from PyQt6.QtGui import QMouseEvent, QKeyEvent


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.WIDTH_WINDOW = 1024
        self.HEIGHT_WINDOW  = 800

        # получаем обьект экрана
        primary_screen = app.primaryScreen()
        # получаем размеры экрана
        screen_size = primary_screen.size()
        # получаем ширину экрана
        width_screen = screen_size.width()
        # получаем высоту экрана
        height_screen = screen_size.height()


        self.setGeometry(
            (width_screen // 2) - (self.WIDTH_WINDOW // 2), 
            (height_screen // 2) - (self.HEIGHT_WINDOW // 2), 
            self.WIDTH_WINDOW, 
            self.HEIGHT_WINDOW
        )

        
        
        self.horizonal_layout = QHBoxLayout()

        self.frame_0 = Frame(self, "#353535", 800, 1024, layout = self.horizonal_layout) 
    def keyPressEvent(self, event: QKeyEvent):
        key = event.key()
        if key == Qt.Key.Key_Escape:
            for frame in frames_list:
                frame.deleteLater()
            frames_list.clear()
            frame_counter[0] = 0
            frame_count.setText(f"всього фреймів:{str(frame_counter[0])}")
        return super().keyPressEvent(event)
        
class Frame(QFrame):        
    def __init__(self, parent, color: str, height: int, width: int, x = None , y = None, layout = None, blue_frames = False ):
        super().__init__(parent = parent)  
        self.BLUE_FRAMES = blue_frames
        if x != None and y != None:
            self.setGeometry(x, y, width, height)
            self.show()
        else:
            self.setFixedSize(width, height)
            
            layout.addWidget(self)
        self.setStyleSheet(f"background-color: {color}")
    def mousePressEvent(self, event : QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton and self.BLUE_FRAMES == True:
            blue_frame = Frame(self, "blue", 50,50, event.pos().x(), event.pos().y() )
            frame_counter[0] += 1
            frame_count.setText(f"всього фреймів:{str(frame_counter[0])}")
            frames_list.append(blue_frame)
        # return super().mousePressEvent(event)

        
        
frame_counter = [0]    
frames_list = []


main_window = MainWindow()        
vertikal_layout2 = QVBoxLayout()
vertikal_layout2.setAlignment(Qt.AlignmentFlag.AlignCenter)
vertikal_layout2.setContentsMargins(0,0,0, 110)
main_window.frame_0.setLayout(vertikal_layout2)
frame1 = Frame(main_window.frame_0, "white", 550, 950, layout = vertikal_layout2, blue_frames = True ) 

instruction =  QLabel(parent = main_window.frame_0, text =  "Ліва кнопка миші - додати фрейм, Escape: очистити")


frame_count = QLabel(parent = main_window.frame_0, text = f"всього фреймів:{str(frame_counter[0])}")

vertikal_layout2.addWidget(instruction)    
vertikal_layout2.addWidget(frame_count)    
