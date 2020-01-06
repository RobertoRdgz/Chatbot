from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher

from typing import Any, Text, Dict, List
from imgurpython import ImgurClient

import random

client_id = 'f7cb1f7fe249b1e'
client_secret = 'fa63213de4acad75186a7b5d5a50e669d9dd7709'
client = ImgurClient(client_id, client_secret)

class ActionTest(Action):
    def name(self) -> Text:
        return "action_test"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        topic = tracker.get_slot('topic')
        url = "https://dummyimage.com/600x400/000/fff&text={}".format(topic)

        dispatcher.utter_message(url)


class ActionRecommend(Action):
    def name(self) -> Text:
        return "action_recommend"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        topic = tracker.get_slot("topic")
        content_type = tracker.get_slot("content_type")

        if content_type in ["image", "picture", "photo"]:
            search = topic

            items = client.gallery_search(search)
            img = items[0].link

            dispatcher.utter_message("Here's an image for you!")
            dispatcher.utter_message(img)

        elif content_type in ["video"]:
            videos = [
                "https://www.youtube.com/watch?v=uoNXG2UZef0",
                "https://www.youtube.com/watch?v=S9B4gHJpo1M",
                "https://www.youtube.com/watch?v=yP6TqsdPIu4",
                "https://www.youtube.com/watch?v=Ksg6lbZrxpM",
                "https://www.youtube.com/watch?v=9dJm0UBikJI",
                "https://www.youtube.com/watch?v=YEzgaKNX5Es",
                "https://www.youtube.com/watch?v=yiw5j1XOaew",
            ]

            video = random.choice(videos)

            dispatcher.utter_message("Here's a video for you!")
            dispatcher.utter_message(video)

        else:
            dispatcher.utter_message("I can't give you a recommendation yet, let's keep talking and get to know each other a little better, what do you think?")

        return [UserUtteranceReverted()]
