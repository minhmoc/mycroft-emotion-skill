from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG

__author__ = 'minhmoc'

LOGGER = getLogger(__name__)

class EmotionSkill(MycroftSkill):

    def __init__(self):
        super(EmotionSkill, self).__init__(name="EmotionSkill")
        
        self.count = 0

    @intent_handler(IntentBuilder("").require("Extremely").require("Happy"))
    def handle_extremely_happy_intent(self, message):
        self.speak_dialog("extremely.happy")

    @intent_handler(IntentBuilder("").require("Happy"))
    def handle_happy_intent(self, message):
        self.speak_dialog("happy")

    @intent_handler(IntentBuilder("").require("Sad"))
    def handle_sad_intent(self, message):
        self.speak_dialog("sad")

def create_skill():
    return EmotionSkill()

