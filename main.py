#!/usr/bin/python
# encoding: utf-8
import curses
import time

import npyscreen
from MainForm import MainForm
from WatchForm import WatchForm
from AddRuleForm import AddRuleForm
from DelRuleForm import DelRuleForm

class ContainerIptablesApp(npyscreen.NPSAppManaged):
    def onStart(self):
        npyscreen.setTheme(npyscreen.Themes.ColorfulTheme)
        height, width = curses.initscr().getmaxyx()
        # self.addForm('MAIN', MainForm, name="container iptables", lines=20, columns=60, draw_line_at=16)
        # self.addForm('WATCH', WatchForm, name="watch iptables", lines=20, columns=60, draw_line_at=16)
        self.mainForm = MainForm(name='container iptables', lines=height, columns=width)
        self.addForm = AddRuleForm(name='add rule iptables', lines=height, columns=width)
        self.watchForm = WatchForm(name='watch iptables', lines=height, columns=width)
        self.delForm = DelRuleForm(name='del rule iptables', lines=height, columns=width)

        self.registerForm("MAIN", self.mainForm)
        self.registerForm("ADDRULE", self.addForm)
        self.registerForm("WATCH", self.watchForm)
        self.registerForm("DELRULE", self.delForm)

if __name__ == '__main__':
    app = ContainerIptablesApp()
    app.run()
