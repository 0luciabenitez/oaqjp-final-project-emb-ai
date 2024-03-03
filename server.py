"""
This module serves as a Flask web server for an emotion detection service. It provides
routes for detecting emotions in a given text and for serving the application's index page.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detection():
    """Detect emotions from the provided text and return a formatted response."""
    text_to_analyze = request.args.get("textToAnalyze")
    try:
        response = emotion_detector(text_to_analyze)
        if response['dominant_emotion'] is None:
            return "Invalid text! Please try again!"
        
        # Splitting the return statement to avoid line too long issue
        return (
            f"For the given statement, the system response is "
            f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
            f"'fear': {response['fear']}, 'joy': {response['joy']} and "
            f"'sadness': {response['sadness']}. The dominant emotion is "
            f"{response['dominant_emotion']}."
        )
    except ValueError as e:  # Replace with specific exceptions as needed
        return str(e)

@app.route("/")
def render_index_page():
    """Render the index page of the web application."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
