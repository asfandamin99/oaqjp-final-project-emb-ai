import requests
import json

def emotion_detector(text_to_analyze):

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    myobj = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    try:
        response = requests.post(url, json=myobj, headers=headers)

        # Handle blank input / bad request
        if response.status_code == 400:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None
            }

        # Handle successful response
        if response.status_code == 200:

            # Convert response text into dictionary
            formatted_response = json.loads(response.text)

            # Extract emotions
            emotions = formatted_response["emotionPredictions"][0]["emotion"]

            anger = emotions["anger"]
            disgust = emotions["disgust"]
            fear = emotions["fear"]
            joy = emotions["joy"]
            sadness = emotions["sadness"]

            # Determine dominant emotion
            emotion_scores = {
                "anger": anger,
                "disgust": disgust,
                "fear": fear,
                "joy": joy,
                "sadness": sadness
            }

            dominant_emotion = max(emotion_scores, key=emotion_scores.get)

            # Return required dictionary
            return {
                "anger": anger,
                "disgust": disgust,
                "fear": fear,
                "joy": joy,
                "sadness": sadness,
                "dominant_emotion": dominant_emotion
            }

        # Handle all other unexpected responses
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    except Exception:
        # Handle network/API exceptions
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }