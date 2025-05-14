import requests, json 

def emotion_detector(text_to_analyse: str) -> dict[str, any]:
    ''' This function executes the emotion detection over the text
        provided by the user. It returns a dictionary with the label
        and its confidence score.
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    response = requests.post(url, json=myobj, headers=header)
    if response.status_code != 200: # Error handling for black user entry
        return {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, "dominant_emotion": None}
    
    emotions = response.json()['emotionPredictions'][0].get("emotion")
    # Select the emotion with the highest value (confidence score)
    # by using the max function with a key argument.
    # The key argument is a function that takes a dictionary entry
    # and returns a value that will be used for comparison.
    # In this case, the value is the confidence score of the emotion.
    max_emotion = max(emotions, key=lambda x: emotions[x])
    emotions["dominant_emotion"] = max_emotion
    
    return emotions
