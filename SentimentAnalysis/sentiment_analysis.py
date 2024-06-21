"""
Executing this function will return the sentiment analisis for a given text
"""
import json
import requests

def sentiment_analyzer(text_to_analyse):
    """
    A function that returns if a text has a Positive, Negative o Neutral sentiment
    """
    url = """https://sn-watson-sentiment-bert.labs.skills.network/v1
          /watson.runtime.nlp.v1/NlpService/SentimentPredict"""
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url, json = myobj, headers=header, timeout=10)
    if response.status_code == 500:
        return {"label" : None, "score" : None}

    json_response = json.loads(response.text)
    label = json_response['documentSentiment']['label']
    score = json_response['documentSentiment']['score']
    return {"label": label, "score": score}
