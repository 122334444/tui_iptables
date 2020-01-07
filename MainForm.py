import npyscreen

class MainForm(npyscreen.FormBaseNew):
    def create(self):
        self.buttonWatch = self.add(WatchButton, name='Watch iptables\t(^W)')
        self.buttonAddRule = self.add(AddRuleButton, name='Add rule iptables\t(^S)')
        self.buttonDelRule = self.add(DelRuleButton, name='Del rule iptables\t(^D)')
        self.buttonExit = self.add(ExitButton, name='Exit application\t(^Q)')

        self.add_handlers({"^W": self.watch_menu})
        self.add_handlers({"^S": self.addrule_menu})
        self.add_handlers({"^D": self.delrule_menu})
        self.add_handlers({"^Q": self.exit_app})

    def watch_menu(self, code_of_key_pressed):
        self.parentApp.getForm('WATCH').watch_thread = 1
        self.parentApp.switchForm('WATCH')

    def addrule_menu(self, code_of_key_pressed):
        self.parentApp.switchForm('ADDRULE')

    def delrule_menu(self, code_of_key_pressed):
        self.parentApp.switchForm('DELRULE')

    def exit_app(self, code_of_key_pressed):
        if npyscreen.notify_ok_cancel(message='Exit?', title='', form_color='CONTROL'):
            self.parentApp.switchForm(None)

class WatchButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.parent.parentApp.getForm('WATCH').watch_thread = 1
        self.parent.parentApp.switchForm('WATCH')

class AddRuleButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.parent.parentApp.switchForm('ADDRULE')

class DelRuleButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.parent.parentApp.switchForm('DELRULE')

class ExitButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.parent.parentApp.switchForm(None)