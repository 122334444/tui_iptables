import subprocess
import time
import threading
import npyscreen

class DelRuleForm(npyscreen.FormBaseNew):
    def create(self):
        self.number = self.add(npyscreen.TitleText, name="Number rule: ")
        self.buttonDel = self.add(DelRuleButton, name='Delete rule')
        self.buttonBack = self.add(MainButton, name='Back menu (^B)')

        self.add_handlers({"^W": self.watch_menu})
        self.add_handlers({"^N": self.addrule_menu})
        self.add_handlers({"^B": self.back_menu})
        self.add_handlers({"^Q": self.exit_menu})

    def watch_menu(self, code_of_key_pressed):
        self.parentApp.getForm('WATCH').watch_thread = 1
        self.parentApp.switchForm('WATCH')

    def addrule_menu(self, code_of_key_pressed):
        self.parentApp.switchForm('ADDRULE')

    def back_menu(self, code_of_key_pressed):
        self.parentApp.switchForm('MAIN')

    def exit_menu(self, code_of_key_pressed):
        if npyscreen.notify_ok_cancel(message='Exit?', title='', form_color='CONTROL'):
            self.parentApp.switchForm(None)

    def check_data(self):
        try:
            if int(self.number.value) < 0:
                return False
            return True
        except:
            npyscreen.notify_confirm(message='Eroor field "{0}". Please input number delete iptables rule'.format(self.number.name), title='Error input feld', wrap=True, form_color='DANGER')
        return False

    def del_rule(self):
        if self.check_data():
            if npyscreen.notify_ok_cancel(message='Delete {0} rule in iptables?'.format(self.number.value), title='Warning!', form_color='WARNING'):
                subprocess.check_output(['bash', 'sh_script/del_iptables.sh', self.number.value]).decode("utf-8")
                # subprocess.check_output(['python', 'time_now.py']).decode("utf-8")
                self.parentApp.switchForm('MAIN')


class MainButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.parent.parentApp.switchForm('MAIN')

class DelRuleButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.parent.parentApp.getForm('DELRULE').del_rule()
