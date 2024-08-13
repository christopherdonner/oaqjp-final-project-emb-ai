import requests
import json

def emotion_detector(text_to_analyze):
    URL='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    inputJSON={ "raw_document": { "text": text_to_analyze } }
    header={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(URL, json=inputJSON, headers=header)
    result=json.loads(response.text)
    emotion_list=result['emotionPredictions']
    return result['emotionPredictions']