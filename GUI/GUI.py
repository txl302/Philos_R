import time
import sys
 
from PyQt4 import QtGui, QtCore
from PyQt4.phonon import Phonon
 
class PollTimeThread(QtCore.QThread):
    """
    This thread works as a timer.
    """
    update = QtCore.pyqtSignal()
 
    def __init__(self, parent):
        super(PollTimeThread, self).__init__(parent)
 
    def run(self):
        while True:
            time.sleep(1)
            if self.isRunning():
                # emit signal
                self.update.emit()
            else:
                return
 
class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
 
        # media
        self.media = Phonon.MediaObject(self)
        self.media.stateChanged.connect(self.handleStateChanged)
        self.video = Phonon.VideoWidget(self)
        self.video.setMinimumSize(200, 200)
        self.audio = Phonon.AudioOutput(Phonon.VideoCategory, self)
        Phonon.createPath(self.media, self.audio)
        Phonon.createPath(self.media, self.video)
 
        # control button
        self.button_hello = QtGui.QPushButton('Hello', self)
        self.button_hello.clicked.connect(self.handleButton)

        self.button_hug = QtGui.QPushButton('Hug', self)
        self.button_hug.clicked.connect(self.handleButton)

        self.button_left_n = QtGui.QPushButton('left near', self)
        self.button_left_n.clicked.connect(self.handleButton)

        self.button_left_m = QtGui.QPushButton('left middle', self)
        self.button_left_m.clicked.connect(self.handleButton)

        self.button_left_f = QtGui.QPushButton('left far', self)
        self.button_left_f.clicked.connect(self.handleButton)

        self.button_right_n = QtGui.QPushButton('right near', self)
        self.button_right_n.clicked.connect(self.handleButton)

        self.button_right_m = QtGui.QPushButton('right middle', self)
        self.button_right_m.clicked.connect(self.handleButton)

        self.button_right_f = QtGui.QPushButton('right far', self)
        self.button_right_f.clicked.connect(self.handleButton)

        self.button_auto = QtGui.QPushButton('Auto', self)
        self.button_auto.clicked.connect(self.handleButton)

        self.button_manual = QtGui.QPushButton('Manual', self)
        self.button_manual.clicked.connect(self.handleButton)
 
 
 
        # for display of time lapse
        self.info = QtGui.QLabel(self)
 
        # layout
        layout = QtGui.QGridLayout(self)
        layout.addWidget(self.video, 1, 3, 7, 1)
        layout.addWidget(self.info, 4, 3, 1, 1)

        layout.addWidget(self.button_hello, 1, 1, 1, 1)
        layout.addWidget(self.button_hug, 1, 2, 1, 1)

        layout.addWidget(self.button_left_n, 2, 1, 1, 1)
        layout.addWidget(self.button_left_m, 3, 1, 1, 1)
        layout.addWidget(self.button_left_f, 4, 1, 1, 1)

        layout.addWidget(self.button_right_n, 2, 2, 1, 1)
        layout.addWidget(self.button_right_m, 3, 2, 1, 1)
        layout.addWidget(self.button_right_f, 4, 2, 1, 1)

        layout.addWidget(self.button_auto, 6, 1, 1, 1)
        layout.addWidget(self.button_manual, 6, 2, 1, 1)
 
 
        # signal-slot, for time lapse
        self.thread = PollTimeThread(self)
        self.thread.update.connect(self.update)
 
    def update(self):
        # slot
        lapse = self.media.currentTime()/1000.0
        self.info.setText("%4.2f s" % lapse)
 
    def startPlay(self):
        if self.path:
            self.media.setCurrentSource(Phonon.MediaSource(self.path))
 
            # use a thread as a timer
            self.thread = PollTimeThread(self)
            self.thread.update.connect(self.update)
            self.thread.start()
            self.media.play()
 
    def handleButton(self):
        if self.media.state() == Phonon.PlayingState:
            self.media.stop()
            self.thread.terminate()
        else:
            self.path = QtGui.QFileDialog.getOpenFileName(self, self.button.text())
            self.startPlay()
 
    def handleStateChanged(self, newstate, oldstate):
        if newstate == Phonon.PlayingState:
            self.button.setText('stop')
        elif (newstate != Phonon.LoadingState and
              newstate != Phonon.BufferingState):
            self.button.setText('file select')
            if newstate == Phonon.ErrorState:
                source = self.media.currentSource().fileName()
                print ('Error: cannot play:', source.toLocal8Bit().data())
                print ('  %s' % self.media.errorString().toLocal8Bit().data())
 
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('video play')
    window = Window()
    window.show()
    sys.exit(app.exec_())

