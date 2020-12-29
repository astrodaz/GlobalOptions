import wx
from options.class_options import AppOptions


class Window1(wx.Dialog):
    def __init__(self, parent, title):
        super(Window1, self).__init__(parent, title=title)

        self.config = AppOptions()

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
        btn_first.Bind(wx.EVT_BUTTON, self._save_options)

        box_buttons_sizer.Add(btn_first, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        mainBox.Add(box_buttons_sizer, wx.ALL | wx.EXPAND, 50)

        # Resize the panel to fit the controls, and then resize the main window
        panel.SetSizer(mainBox)
        mainBox.Fit(self)
        panel.Fit()
        self.Center()

    def _save_options(self, e):
        self.config.option2 = 'pickle'
        self.config.option1 = 'ham'
        self.Close()
