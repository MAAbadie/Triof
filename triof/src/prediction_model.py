import requests


def identify_waste_type(user_path=None):
    """
    Identify whether a given waste is a bottle, a glass or cutlery
    """
    # TODO [security] put this in secret vault from Azure - retrieve environment variables
    # NOTE: we use the 'predict from url' version of the model 
    ENDPOINT_URL = "https://triofwastetypersecondhand-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/a24ef570-2981-47a0-8f37-4e0b3390d432/classify/iterations/Iteration1/url"
    prediction_key_url = "01da5e70b4b045fb9ff65d824d1663c6"
    content_type_url = "application/json"

    ENDPOINT_LOCAL_FILE = "https://triofwastetypersecondhand-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/a24ef570-2981-47a0-8f37-4e0b3390d432/classify/iterations/Iteration1/image"
    prediction_key_local_file = "01da5e70b4b045fb9ff65d824d1663c6"
    content_type_local_file = "application/octet-stream"
    
    # NOTE: test set for function
    # path = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.NMwKLGTZzgNhzJmjsSpRXQHaHa%26pid%3DApi&f=1&ipt=e14c9566bb9b6dbf919d26e240026f2917d0d5aa60d50228ea92e53c16e75dc3&ipo=images"
    # body_file = "camera/100-gobelets-transparent.jpg"

    # CHOOSE YOUR IMAGE
    body_url = {"Url": user_path}
    exception = ""
    predictions = {}

    # Get prediction from model
    try:
        response = requests.post(url=ENDPOINT_URL, 
                                headers={"Prediction-Key": prediction_key_url, "Content-Type": content_type_url},
                                json=body_url)
        print("NO EXCEPTION DURING MODEL CALL")
        print(response.status_code)
        json_response = response.json()
        print(json_response)
        results = json_response.get("predictions")
        print(results)
        predictions = {i.get("tagName"): i.get("probability") for i in results}
        print(predictions)
    except Exception as e:
        exception = e
    return predictions, exception