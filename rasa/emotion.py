from rasa.nlu.components import Component
from EmotionClassifier import CLF

class EmotionClassifier(Component):
    name = "emotion_classifier"
    provides = ["entities"]
    requires = []
    defaults = {}
    language_list = ["en"]
    clf = CLF()
    print("INITIALIZED CUSTOM EMOTION CLASSIFIER")

    def __init__(self, component_config=None):
        super(EmotionClassifier, self).__init__(component_config)

    def train(self, training_data, cfg, **kwargs):
        pass

    def convert_to_rasa(self, value, confidence):
        """Convert model output into the Rasa NLU compatible output format."""

        entity = {
            "value": value,
            "confidence": confidence,
            "entity": "emotion",
            "extractor": "EmotionClassifier"
        }

        return entity

    def process(self, message, **kwargs):
        intent = message.get("intent")
        if not intent == "need_advice":
            emotion, confidence = self.clf.predict(message.text)

            entity = self.convert_to_rasa(None, 1.0)
            if confidence is not None:
                if confidence > 0.2:
                    entity = self.convert_to_rasa(emotion, confidence)

            message.set(
                "entities",
                message.get("entities", []) + [entity],
                add_to_output=True
            )


    def persist(self, file_name, model_dir):
        pass
