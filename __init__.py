from mycroft import MycroftSkill, intent_file_handler


class PausenErinnerung(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('erinnerung.pausen.intent')
    def handle_erinnerung_pausen(self, message):
        self.speak_dialog('erinnerung.pausen')


def create_skill():
    return PausenErinnerung()

