import subprocess
import time
import threading
import npyscreen

class WatchForm(npyscreen.FormBaseNew):
    def create(self):
        self.buttonBack = self.add(MainButton, name='Back menu (^B)')
        self.watch = self.add(npyscreen.MultiLineEdit, name='')
        self.watch.editable = False
        self.watch.wrap = True
        self.watch_thread = 0

        self.thread_time = threading.Thread(target=self.update_time, args=())
        self.thread_time.daemon = True
        self.thread_time.start()

        self.add_handlers({"^N": self.addrule_menu})
        self.add_handlers({"^D": self.delrule_menu})
        self.add_handlers({"^B": self.back_menu})
        self.add_handlers({"^Q": self.exit_menu})

    def off_thread(self):
        self.parentApp.getForm('WATCH').watch_thread = 0
        self.parentApp.getForm('WATCH').thread_time = None
        self.parentApp.getForm('WATCH').watch.value = ''


    def addrule_menu(self, code_of_key_pressed):
        self.off_thread()
        self.parentApp.switchForm('ADDRULE')

    def delrule_menu(self, code_of_key_pressed):
        self.off_thread()
        self.parentApp.switchForm('DELRULE')

    def back_menu(self, code_of_key_pressed):
        self.off_thread()
        self.parentApp.switchForm('MAIN')

    def exit_menu(self, code_of_key_pressed):
        if npyscreen.notify_ok_cancel(message='Exit?', title='', form_color='CONTROL'):
            self.off_thread()
            self.parentApp.switchForm(None)

    def update_time(self):
        while True:
            if self.watch_thread == 1:
                self.watch.value = str(subprocess.check_output(['bash', 'sh_script/ls_iptables.sh']).decode("utf-8"))
                # self.watch.value = str(subprocess.check_output(['python', 'time_now.py']).decode("utf-8"))
                self.watch.display()
            time.sleep(1)

class MainButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.parent.parentApp.getForm('WATCH').watch_thread = 0
        self.parent.parentApp.getForm('WATCH').thread_time = None
        self.parent.parentApp.getForm('WATCH').watch.value = ''
        self.parent.parentApp.switchForm('MAIN')
