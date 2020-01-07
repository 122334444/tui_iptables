#!/usr/bin/python
# encoding: utf-8
import curses
import npyscreen
from MainForm import MainForm
from WatchForm import WatchForm
from AddRuleForm import AddRuleForm
from DelRuleForm import DelRuleForm

class ContainerIptablesApp(npyscreen.NPSAppManaged):
    def onStart(self):
        npyscreen.setTheme(npyscreen.Themes.ColorfulTheme)
        # self.addForm('MAIN', MainForm, name="container iptables", lines=20, columns=60, draw_line_at=16)
        # self.addForm('WATCH', WatchForm, name="watch iptables", lines=20, columns=60, draw_line_at=16)
        self.registerForm("MAIN", MainForm(name='container iptables', lines=40, columns=100))
        self.registerForm("ADDRULE", AddRuleForm(name='add rule iptables', lines=40, columns=100))
        self.registerForm("WATCH", WatchForm(name='watch iptables', lines=40, columns=100))
        self.registerForm("DELRULE", DelRuleForm(name='del rule iptables', lines=40, columns=100))

if __name__ == '__main__':
    app = ContainerIptablesApp()
    app.run()
