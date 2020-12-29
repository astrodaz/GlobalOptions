import wx
from module1.window1 import Window1
from module_2.window2 import Window2
from options.class_options import AppOptions


class MyFrame(wx.Frame):

    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title)

        self.InitUI()
        self.Center()
        self.ThisProcess()

    def InitUI(self):
        # The  main panel
        panel = wx.Panel(self)

        # The main sizer for the window
        mainBox = wx.BoxSizer(wx.VERTICAL)

        """
            Execute and Exit Buttons
        """
        box_buttons = wx.StaticBox(panel)
        box_buttons_sizer = wx.StaticBoxSizer(box_buttons, wx.HORIZONTAL)

        btn_first = wx.Button(panel, label='Button 1')
        btn_first.Bind(wx.EVT_BUTTON, self.button1_click)
        btn_second = wx.Button(panel, label='Button 2')
        btn_second.Bind(wx.EVT_BUTTON, self.button2_click)

        box_buttons_sizer.Add(btn_first, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        box_buttons_sizer.Add(btn_second, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        mainBox.Add(box_buttons_sizer, wx.ALL | wx.EXPAND, 50)

        # Resize the panel to fit the controls, and then resize the main window
        panel.SetSizer(mainBox)
        mainBox.Fit(self)
        panel.Fit()

    def ThisProcess(self):
        options = AppOptions()
        print(options.option1)
        print(options.option2)
        print(options.option3)

    def button1_click(self, e):
        w1 = Window1(self, 'Window 1')
        w1.ShowModal()
        self.ThisProcess()

    def button2_click(self, e):
        w2 = Window2(self, 'Window 2')
        w2.ShowModal()
        self.ThisProcess()
