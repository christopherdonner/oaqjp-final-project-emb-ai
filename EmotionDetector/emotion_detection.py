import requests
import json

def emotion_detector(text_to_analyze):
    URL='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    inputJSON={ "raw_document": { "text": text_to_analyze } }
    header={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(URL, json=inputJSON, headers=header)
    result=json.loads(response.text)
    emotion_list=result['emotionPredictions']
    emotion=emotion_list[0]['emotion']
    sortedEmotions=sorted(emotion.items(), key=lambda x:x[1], reverse=True)
    print(sortedEmotions)
    emotion_aggregated={
        'anger': emotion['anger'],
        'disgust': emotion['disgust'],
        'fear': emotion['fear'],
        'joy': emotion['joy'],
        'sadness': emotion['sadness'],
    }
    print(emotion_aggregated)
    return emotion_aggregated