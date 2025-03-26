"""
Flask-based Emotion Detection API.

This module provides an API endpoint to analyze emotions from text input
using the `emotion_detector` function from the `EmotionDetection` package.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Analyze the user-provided text for emotions and return the result.

    Returns:
        str: A formatted string with emotion scores and the dominant emotion,
             or an error message if the text is invalid.
    """
    text_to_detect = request.args.get('textToAnalyze')
    if not text_to_detect:
        return "Invalid text! Please provide a valid input."

    formated_response = emotion_detector(text_to_detect)
    if formated_response['dominant_emotion'] is None:
        return "Invalid text! Please try again."
    return (
        f"For the given statement, the system response is 'anger': {formated_response['anger']} "
        f"'disgust': {formated_response['disgust']}, 'fear': {formated_response['fear']}, "
        f"'joy': {formated_response['joy']} and 'sadness': {formated_response['sadness']}. "
        f"The dominant emotion is {formated_response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Render the index.html page.

    Returns:
        Response: The rendered HTML page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
