"""
This module handles the rendering of the index page and emotion detection 
functionality using Flask. It defines routes to render the index page and 
analyze text for emotions, utilizing an external emotion detection API.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index():
    """
    Renders the index page.

    Returns:
        Response: The rendered template for the index page.
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detectoring() -> str:
    """
    Analyzes the provided text for emotions and returns a response string.
    
    Returns:
        str: A string describing the emotions detected and the dominant emotion.
    """
    text_to_analyze = request.args.get("textToAnalyze", "")

    result = emotion_detector(text_to_analyze) # Call the emotion detection API

    # extract relevant emotions to dictionary of {emotion: score}
    emotions = {k: result[k] for k in ("anger", "disgust", "fear", "joy", "sadness")}

    try:
        dominant_emotion = max(emotions, key=emotions.get) # get the emotion with the highest score
    except ValueError:
        return "Invalid text!\nPlease try again!."

    resp_text = f'''For the given statement, the system response is
                    {', '.join(f'{k}: {v}' for k, v in emotions.items())}.
                    The dominant emotion is <b>{dominant_emotion}</b>.
                '''

    return resp_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
