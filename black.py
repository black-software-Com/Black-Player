#!/usr/bin/python3
# Black-Player v1.0
#

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from MainWindow import Ui_MainWindow
from webbrowser import open_new, open_new_tab
from tkinter import *
from tkinter.ttk import *
from tkhtmlview import HTMLLabel
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math,sys
def hhmmss(ms):

    h, r = divmod(ms, 36000)
    m, r = divmod(r, 60000)
    s, _ = divmod(r, 1000)
    return ("%d:%02d:%02d" % (h,m,s)) if h else ("%d:%02d" % (m,s))

class ViewerWindow(QMainWindow):
    state = pyqtSignal(bool)

    def closeEvent(self, e):
        self.state.emit(False)


class PlaylistModel(QAbstractListModel):
    def __init__(self, playlist, *args, **kwargs):
        super(PlaylistModel, self).__init__(*args, **kwargs)
        self.playlist = playlist

    def data(self, index, role):
        if role == Qt.DisplayRole:
            media = self.playlist.media(index.row())
            return media.canonicalUrl().fileName()

    def rowCount(self, index):
        return self.playlist.mediaCount()


class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.help_m.triggered.connect(self.help)
        self.feedback_m.triggered.connect(self.feedback)
        self.about_m.triggered.connect(self.about)
        self.black_m.triggered.connect(self.black)
        self.dev_m.triggered.connect(self.dev)
        self.player = QMediaPlayer()


        self.player.error.connect(self.erroralert)
        self.player.play()

        self.playlist = QMediaPlaylist()
        self.player.setPlaylist(self.playlist)

        self.viewer = ViewerWindow(self)
        self.viewer.setWindowFlags(self.viewer.windowFlags() | Qt.WindowStaysOnTopHint)
        self.viewer.setMinimumSize(QSize(480,360))

        videoWidget = QVideoWidget()
        self.viewer.setCentralWidget(videoWidget)
        self.player.setVideoOutput(videoWidget)

        self.playButton.pressed.connect(self.player.play)
        self.pauseButton.pressed.connect(self.player.pause)
        self.stopButton.pressed.connect(self.player.stop)
        self.volumeSlider.valueChanged.connect(self.player.setVolume)

        self.viewButton.toggled.connect(self.toggle_viewer)
        self.viewer.state.connect(self.viewButton.setChecked)

        self.previousButton.pressed.connect(self.playlist.previous)
        self.nextButton.pressed.connect(self.playlist.next)

        self.model = PlaylistModel(self.playlist)
        self.playlistView.setModel(self.model)
        self.playlist.currentIndexChanged.connect(self.playlist_position_changed)
        selection_model = self.playlistView.selectionModel()
        selection_model.selectionChanged.connect(self.playlist_selection_changed)

        self.player.durationChanged.connect(self.update_duration)
        self.player.positionChanged.connect(self.update_position)
        self.timeSlider.valueChanged.connect(self.player.setPosition)

        self.open_file_action.triggered.connect(self.open_file)
        self.exit_m.triggered.connect(self.close)

        self.setAcceptDrops(True)
        self.volup_m.triggered.connect(self.volup_f)
        self.voldown_m.triggered.connect(self.voldown_f)

        self.show()
    def contextMenuEvent(self,event):
        global amenu
        menu_r = QMenu(self)
        black_m = QAction('Black',self)
        black_m.setShortcut('F1')
        black_m.triggered.connect(self.black)
        dev_m = QAction('Dev',self)
        dev_m.triggered.connect(self.dev)
        dev_m.setShortcut('F2')
        about_m = QAction('About',self)
        about_m.setShortcut('F3')
        about_m.triggered.connect(self.about)
        menu_r.addActions([black_m,dev_m,about_m])
        help_m = menu_r.addMenu('Help')
        help_mm = QAction('Help',self)
        help_mm.triggered.connect(self.help)
        help_mm.setShortcut('Ctrl+H')
        send_feedback_m = QAction('Send FeedBack',self)
        send_feedback_m.triggered.connect(self.feedback)
        send_feedback_m.setShortcut('Ctrl+F')
        help_m.addActions([help_mm,send_feedback_m])
        menu_r.addSeparator()
        exit_m = QAction('Exit',self)
        exit_m.setShortcut('Alt+F4')
        exit_m.triggered.connect(self.close)
        menu_r.addAction(exit_m)
        menu_r.addAction(exit_m)
        action = menu_r.exec_(self.mapToGlobal(event.pos()))    
        if action == black_m:
          self.black()
        elif action == dev_m:
            self.dev()
        elif action == about_m:
            self.about()
        elif action == send_feedback_m:
            self.feedback()
        elif action == help_mm:
            self.help()
        elif action == exit_m:
            self.close()  
    def dev(self):
        open_new_tab('https://mrprogrammer2938.github.io/mrprogrammer2938/')
    def black(self):
        open_new_tab('https://black-software-com.github.io/Black-Software/')
    def volup_f(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
                    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))

        currentVolumeDb = volume.GetMasterVolumeLevel()
        volume.SetMasterVolumeLevel(currentVolumeDb +    3.0, None)
    def voldown_f(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
                    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))

        currentVolumeDb = volume.GetMasterVolumeLevel()
        volume.SetMasterVolumeLevel(currentVolumeDb - 3.0, None)

    def about(self):
      global amenu,ammenu
      root = Tk()
      root.title('Black-Webbrowser/About')
      root.geometry("700x600+550+130")
      root.resizable(0,0)
      txt_a = '''
Black Player

Video Player

(Fast)
(Gui)
      '''
      photo = PhotoImage(file='./Scr/black-videoplayer-icon.png')
      root.iconphoto(False,photo)
      amenu = Menu(root,tearoff=0)
      filemenu = Menu(amenu,tearoff=0)
      filemenu.add_command(label='Help',accelerator='Ctrl+H',command=self.help)
      filemenu.add_separator()
      filemenu.add_command(label='Exit',accelerator='Alt+F4',command=root.destroy)
      amenu.add_cascade(label='Options',menu=filemenu)
      ammenu = Menu(root,tearoff=0)
      ammenu.add_cascade(label='Help',command=self.help)
      ammenu.add_separator()
      ammenu.add_cascade(label='Exit',command=root.destroy)
      root.config(menu=amenu)
      label_i = Label(root,text='Black Webbrowser',foreground='black',font=("None",28))
      label_i.place(bordermode=INSIDE,x=130,y=15)
      label_t = Label(root,text=txt_a,foreground='black',font=("None",10))
      label_t.place(bordermode=INSIDE,x=175,y=65)
      b = HTMLLabel(root,html='<a title="Black Software" href="https://black-software-com.github.io/Black-Software/" taregt="_blank"> Black </a>')
      b.place(bordermode=INSIDE,x=20,y=200)
      g = HTMLLabel(root,html='<a href="https://github.com/black-software-com" target="_blank"> Github </a>')
      g.place(bordermode=INSIDE,x=20,y=230)
      f = HTMLLabel(root,html='<a href="https://www.facebook.com/profile.php?id=100071465381949" target="_blank"> Facebook </a>')
      f.place(bordermode=INSIDE,x=20,y=260)
      i = HTMLLabel(root,html='<a href="https://instagram.com/black_software_company" target="_blank"> Instagram</a>')
      i.place(bordermode=INSIDE,x=20,y=290)
      t = HTMLLabel(root,html='<a href="https://twitter.com/blacksoftware3" target="_blank"> Twitter </a>')
      t.place(bordermode=INSIDE,x=20,y=320)
      tl = HTMLLabel(root,html='<a href="https://t.me/blacksoftware3" target="_blank"> Telegram </a>')
      tl.place(bordermode=INSIDE,x=20,y=350)
      z = HTMLLabel(root,html='<a href="https://zil.ink/blacksoftware" target="_blank"> ZLink </a>')
      z.place(bordermode=INSIDE,x=20,y=380)
      fl = Label(root,text='© Black Software')
      fl.place(bordermode=INSIDE,x=280,y=530)
      root.bind("<Control-h>",self.help)
      root.bind("<Button-3>",self.do_popupa)
      root.mainloop()
    def do_popupa(self,event):
        try:
            amenu.tk_popup(event.x_root,event.y_root)
        finally:
            amenu.grab_release()
    def feedback(self):
        open_new_tab('https://github.com/black-software-Com/Black-Player/issues')
    def help(self):
        open_new_tab('https://black-software-com.github.io/Black-Help/')
    
    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.acceptProposedAction()

    def dropEvent(self, e):
        for url in e.mimeData().urls():
            self.playlist.addMedia(
                QMediaContent(url)
            )

        self.model.layoutChanged.emit()

        if self.player.state() != QMediaPlayer.PlayingState:
            i = self.playlist.mediaCount() - len(e.mimeData().urls())
            self.playlist.setCurrentIndex(i)
            self.player.play()

    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "mp3 Audio (*.mp3);mp4 Video (*.mp4);Movie files (*.mov);All files (*.*)")

        if path:
            self.playlist.addMedia(
                QMediaContent(
                    QUrl.fromLocalFile(path)
                )
            )

        self.model.layoutChanged.emit()

    def update_duration(self, duration):
        print("!", duration)
        print("?", self.player.duration())
        
        self.timeSlider.setMaximum(duration)

        if duration >= 0:
            self.totalTimeLabel.setText(hhmmss(duration))

    def update_position(self, position):
        if position >= 0:
            self.currentTimeLabel.setText(hhmmss(position))

        self.timeSlider.blockSignals(True)
        self.timeSlider.setValue(position)
        self.timeSlider.blockSignals(False)

    def playlist_selection_changed(self, ix):
        # We receive a QItemSelection from selectionChanged.
        i = ix.indexes()[0].row()
        self.playlist.setCurrentIndex(i)

    def playlist_position_changed(self, i):
        if i > -1:
            ix = self.model.index(i)
            self.playlistView.setCurrentIndex(ix)

    def toggle_viewer(self, state):
        if state:
            self.viewer.show()
        else:
            self.viewer.hide()

    def erroralert(self, *args):
        print(args)

def main():
#     app = QApplication([])
#     app.setApplicationName("Black-Player")
#     app.setApplicationDisplayName("Black-Player")
#     app.setApplicationVersion("v1.0")
#     app.setStyle("Fusion")
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)

    window = MainWindow()

if __name__ == '__main__':
    txt_i = """
Black-Player (Welcome) :)

(Gui)
(Fast)
    """
    file_i = open("./Core/check_i","r").read()
    if file_i == "True" or file_i == "True\n":
        app = QApplication([])
        app.setApplicationName("Black-Player")
        app.setApplicationDisplayName("Black-Player")
        app.setApplicationVersion("v1.0")
        app.setStyle("Fusion")
        mess_i = QMessageBox()
        mess_i.setWindowTitle("Black-Player/Information")
        mess_i.setWindowIcon(QIcon('./Scr/black-videoplayer-icon.png'))
        mess_i.setIcon(QMessageBox.Information)
        mess_i.setText(txt_i)
        mess_i.exec_()
        with open("./Core/check_i","w") as file_i:
            file_i.write("False")
            file_i.close()
        # main()
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ToolTipBase, Qt.white)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, Qt.black)
    # app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

        window = MainWindow()
        # app.setPalette(palette)
        app.setPalette(palette)
        app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
        
        app.exec_()

    else:
        app = QApplication([])
        app.setApplicationName("Black-Player")
        app.setApplicationDisplayName("Black-Player")
        app.setApplicationVersion("v1.0")
        app.setStyle("Fusion")
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ToolTipBase, Qt.white)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, Qt.black)
        window = MainWindow()
        app.setPalette(palette)
        app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
        app.exec_()