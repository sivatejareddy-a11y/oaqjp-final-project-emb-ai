from flask import Flask, render_template, request 
from EmotionDetection.emotion_detection import emotion_detector
import json

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    formatted_responseresponse = (
    f"For the given statement, the system response is "
    f"'anger': {data['anger']}, 'disgust': {data['disgust']}, 'fear': {data['fear']}, "
    f"'joy': {data['joy']} and 'sadness': {data['sadness']}. "
    f"The dominant emotion is {data['dominant_emotion']}."
    )
    return formatted_response

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    #TODO
    return render_template('index.html')
    

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5000)

