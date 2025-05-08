from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_remote_menu):

    MIN_VOLUME = 0
    MAX_VOLUME = 10

    MIN_CHANNEL = 1
    MAX_CHANNEL = 9

    def __init__(self) -> None:
        """
        Method to initialize variables for the class and connects the channel buttons to their respective
        pictures at the top of the webpage
        """
        super().__init__()
        self.setupUi(self)

        self.label_power.setPixmap(QtGui.QPixmap("Pictures/black.png"))
        self.vol_slider.setEnabled(False)

        self.power.clicked.connect(lambda: self.tv_power())
        self.mute.clicked.connect(lambda: self.mute_tv())
        self.num_1.clicked.connect(lambda: self.channel_1())
        self.num_2.clicked.connect(lambda: self.channel_2())
        self.num_3.clicked.connect(lambda: self.channel_3())
        self.num_4.clicked.connect(lambda: self.channel_4())
        self.num_5.clicked.connect(lambda: self.channel_5())
        self.num_6.clicked.connect(lambda: self.channel_6())
        self.num_7.clicked.connect(lambda: self.channel_7())
        self.num_8.clicked.connect(lambda: self.channel_8())
        self.num_9.clicked.connect(lambda: self.channel_9())
        self.ch_up.clicked.connect(lambda: self.channel_up())
        self.ch_down.clicked.connect(lambda: self.channel_down())
        self.vol_up.clicked.connect(lambda: self.volume_up())
        self.vol_down.clicked.connect(lambda: self.volume_down())
        self.vol_slider.valueChanged.connect(lambda: self.slider())

        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Logic.MIN_VOLUME
        self.__channel: int = Logic.MIN_CHANNEL

    def tv_power(self) -> None:
        """
        Method to turn the tv power on and off
        """
        if self.__status == False:
            self.__status = True
            self.check_channel()
            self.vol_slider.setEnabled(True)
        else:
            self.label_power.setPixmap(QtGui.QPixmap("Pictures/black.png"))
            self.__status = False
            self.vol_slider.setEnabled(False)

    def mute_tv(self) -> None:
        """
        Method to mute or unmute the tv
        """
        if self.__status:
            if self.__muted == False:
                self.__muted = True
                self.vol_slider.setEnabled(False)
            else:
                self.__muted = False
                self.vol_slider.setEnabled(True)

    def channel_1(self) -> None:
        """
        changes to channel 1
        """
        if self.__status:
            self.label_power.setPixmap(QtGui.QPixmap("Pictures/nbc.png"))
            self.__channel = 1

    def channel_2(self) -> None:
        """
        changes to channel 2
        """
        if self.__status:
            self.label_power.setPixmap(QtGui.QPixmap("Pictures/cn.png"))
            self.__channel = 2

    def channel_3(self) -> None:
        """
        changes to channel 3
        """
        if self.__status:
            self.label_power.setPixmap(QtGui.QPixmap("Pictures/abc.png"))
            self.__channel = 3

    def channel_4(self) -> None:
        """
        changes to channel 4
        """
        if self.__status:
            self.label_power.setPixmap(QtGui.QPixmap("Pictures/fox_news.png"))
            self.__channel = 4

    def channel_5(self) -> None:
        """
        changes to channel 5
        """
        if self.__status:
            self.label_power.setPixmap(QtGui.QPixmap("Pictures/food_network.png"))
            self.__channel = 5

    def channel_6(self) -> None:
        """
        changes to channel 6
        """
        if self.__status:
            self.label_power.setPixmap(QtGui.QPixmap("Pictures/hgtv.png"))
            self.__channel = 6

    def channel_7(self) -> None:
        """
        changes to channel 7
        """
        if self.__status:
            self.label_power.setPixmap(QtGui.QPixmap("Pictures/hallmark.png"))
            self.__channel = 7

    def channel_8(self) -> None:
        """
        changes to channel 8
        """
        if self.__status:
            self.label_power.setPixmap(QtGui.QPixmap("Pictures/history.png"))
            self.__channel = 8

    def channel_9(self) -> None:
        """
        changes to channel 9
        """
        if self.__status:
            self.label_power.setPixmap(QtGui.QPixmap("Pictures/espn.png"))
            self.__channel = 9

    def channel_up(self) -> None:
        """
        Method to increase the channel number
        """
        if self.__status:
            if self.__channel < Logic.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Logic.MIN_CHANNEL
            self.check_channel()

    def channel_down(self) -> None:
        """
        Method to decrease the channel number
        """
        if self.__status:
            if self.__channel > Logic.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Logic.MAX_CHANNEL
            self.check_channel()

    def check_channel(self) -> None:
        """
        Changes the channel depending on the channel number
        """
        if self.__channel == 1:
            self.channel_1()
        elif self.__channel == 2:
            self.channel_2()
        elif self.__channel == 3:
            self.channel_3()
        elif self.__channel == 4:
            self.channel_4()
        elif self.__channel == 5:
            self.channel_5()
        elif self.__channel == 6:
            self.channel_6()
        elif self.__channel == 7:
            self.channel_7()
        elif self.__channel == 8:
            self.channel_8()
        elif self.__channel == 9:
            self.channel_9()

    def slider(self) -> None:
        """
        Changes the volume variable to represent location along the slider
        """
        self.__volume = self.vol_slider.value()


    def volume_up(self) -> None:
        """
        Method to increase the volume
        """
        if self.__status:
            self.__muted = False
            self.vol_slider.setEnabled(True)
            if self.__volume < Logic.MAX_VOLUME:
                self.__volume += 1
            self.vol_slider.setValue(self.__volume)

    def volume_down(self) -> None:
        """
        Method to decrease the volume
        """
        if self.__status:
            self.__muted = False
            self.vol_slider.setEnabled(True)
            if self.__volume > Logic.MIN_VOLUME:
                self.__volume -= 1
            self.vol_slider.setValue(self.__volume)
