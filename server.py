from flask import Flask, make_response, render_template, request
from EmotionDetector.emotion_detection import emotion_detector

app=Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def emotionDetector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominantEmotion = response['dominant_emotion']
    return "For the given statement, the system response is {}. The dominant emotion is {}".format(response, dominantEmotion)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)