from class_main_window import MyFrame
import wx
import os
from options.class_options import AppOptions

config = AppOptions()


def main():
    thisapp = wx.App()
    app_windows = MyFrame(None, 'Options Test')
    app_windows.Show()
    thisapp.MainLoop()


if __name__ == '__main__':
    main()
