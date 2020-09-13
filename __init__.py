from mycroft import MycroftSkill, intent_file_handler


class InsultsBack(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('back.insults.intent')
    def handle_back_insults(self, message):
        self.speak_dialog('back.insults')


def create_skill():
    return InsultsBack()

