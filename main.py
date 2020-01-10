#!/usr/bin/python
# encoding: utf-8
import npyscreen
from MainForm import MainForm
from WatchForm import WatchForm
from AddRuleForm import AddRuleForm
from DelRuleForm import DelRuleForm

class ContainerIptablesApp(npyscreen.NPSAppManaged):
    def onStart(self):
        npyscreen.setTheme(npyscreen.Themes.ColorfulTheme)

        self.registerForm("MAIN", MainForm(name='container iptables', minimum_columns=0, minimum_lines=0))
        self.registerForm("ADDRULE", AddRuleForm(name='add rule iptables', minimum_columns=0, minimum_lines=0))
        self.registerForm("WATCH", WatchForm(name='watch iptables', minimum_columns=0, minimum_lines=0))
        self.registerForm("DELRULE", DelRuleForm(name='del rule iptables', minimum_columns=0, minimum_lines=0))

if __name__ == '__main__':
    app = ContainerIptablesApp()
    app.run()
