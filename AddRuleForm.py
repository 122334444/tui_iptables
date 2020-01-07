import re
import subprocess
import time
import threading
import npyscreen

class AddRuleForm(npyscreen.FormBaseNew):
    def create(self):
        self.buttonBack = self.add(MainButton, name='Back menu (^B)')

        # self.watch.value = str(subprocess.check_output(['bash', '/WEB/utils/ls_iptables.sh']).decode("utf-8"))
        # self.watch.value = str(subprocess.check_output(['python', 'time_now.py']).decode("utf-8"))

        self.global_eth = self.add(npyscreen.TitleText, name="Global interface: ")
        self.global_port = self.add(npyscreen.TitleText, name="Global port: ")
        self.local_ip = self.add(npyscreen.TitleText, name="Local IP: ")
        self.local_port = self.add(npyscreen.TitleText, name="Local port: ")

        self.buttonAddNewRule = self.add(AddRuleButton, name='Add new rule iptables')

        self.add_handlers({"^W": self.watch_menu})
        self.add_handlers({"^D": self.delrule_menu})
        self.add_handlers({"^B": self.back_menu})
        self.add_handlers({"^Q": self.exit_menu})

    def watch_menu(self, code_of_key_pressed):
        self.parentApp.getForm('WATCH').watch_thread = 1
        self.parentApp.switchForm('WATCH')

    def delrule_menu(self, code_of_key_pressed):
        self.parentApp.switchForm('DELRULE')

    def back_menu(self, code_of_key_pressed):
        self.parentApp.switchForm('MAIN')

    def exit_menu(self, code_of_key_pressed):
        if npyscreen.notify_ok_cancel(message='Exit?', title='', form_color='CONTROL'):
            self.parentApp.switchForm(None)

    def check_data(self):
        ## Valid ip
        try:
            if bool(re.findall(r"^[^a-z]", self.global_eth.value)):
                raise ValueError
            if bool(re.findall(r"[^a-z0-9@]", self.global_eth.value)):
                raise ValueError
            if bool(re.findall(r"[^0-9l]+$", self.global_eth.value)):
                raise ValueError
        except:
            npyscreen.notify_confirm(message='Eroor field "{0}". Please input correct interface.'.format(self.global_eth.name), title='Error input feld', wrap=True, wide=True, form_color='DANGER')
            return False

        ## Valid port
        try:
            if int(self.global_port.value) < 0:
                raise ValueError
            if int(self.global_port.value) > 65535:
                raise ValueError
        except:
            npyscreen.notify_confirm(message='Eroor field "{0}". Please input correct port.'.format(self.global_port.name), title='Error input feld', wrap=True, wide=True, form_color='DANGER')
            return False

        ## Valid ip
        try:
            arr = str(self.local_ip.value).split('.')
            for elem in arr:
                if int(elem) < 0:
                    raise ValueError
                if int(elem) > 255:
                    raise ValueError
            if str(self.local_ip.value).split('.').__len__() == 4:
                pass
            else:
                raise ValueError
        except:
            npyscreen.notify_confirm(message='Eroor field "{0}". Please input correct ip'.format(self.local_ip.name), title='Error input feld', wrap=True, wide=True, form_color='DANGER')
            return False



        ## Valid port
        try:
            if int(self.local_port.value) < 0:
                raise ValueError
            if int(self.local_port.value) > 65535:
                raise ValueError
        except:
            npyscreen.notify_confirm(message='Eroor field "{0}". Please input correct port.'.format(self.local_port.name), title='Error input feld', wrap=True, wide=True, form_color='DANGER')
            return False

        return True

    def add_rule(self):
        if self.check_data():
            subprocess.check_output(['bash', 'sh_script/add_iptables.sh', self.global_eth.value, self.global_port.value, self.local_ip.value, self.local_port.value]).decode("utf-8")
            # subprocess.check_output(['python', 'time_now.py']).decode("utf-8")
            self.parentApp.switchForm('MAIN')


class MainButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.parent.parentApp.switchForm('MAIN')

class AddRuleButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.parent.parentApp.getForm('ADDRULE').add_rule()
