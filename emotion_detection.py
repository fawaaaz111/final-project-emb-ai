import requests, json 

def emotion_detector(text_to_analyse: str) -> dict[str,any]:
    ''' This function executes the emotion detection over the text
        provided by the user. It returns a dictionary with the label
        and its confidence score.
    '''

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    response = requests.post(url, json = myobj, headers = header)  # Send a POST request to the API with the text and headers

    # Check if the response status code is not 200 (OK)
    if response.status_code != 200:
        return {'label': "None", 'score': "None"}  # Return a default response if the request failed
    
    formated = json.loads(response.text)

    label = formated.get("documentEmotion", {}).get("label", "N/A")  # Extract the emotion label from the response
    score = formated.get("documentEmotion", {}).get("score", "N/A")  # Extract the emotion score from the response


    return {'label': f"{label}", 'score': f"{score}"}  # Return the response text from the API