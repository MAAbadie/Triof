from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials
import os, time, uuid


VISION_TRAINING_KEY = "6907931ff1da43d1b3b66bc8107485a5"
VISION_TRAINING_ENDPOINT = "https://triofwastetypersdkbuilt.cognitiveservices.azure.com/"
VISION_PREDICTION_KEY = "9c96bcd39fdf404eb79c7a32a2c7cdc0"
VISION_PREDICTION_ENDPOINT = "https://triofwastetypersdkbuilt-prediction.cognitiveservices.azure.com/"
VISION_PREDICTION_RESOURCE_ID = "/subscriptions/974386b8-dfe6-43cc-94af-17335974d64a/resourceGroups/triof_resources_Simplon_Bdx_MA/providers/Microsoft.CognitiveServices/accounts/triofwastetypersdkbuilt-Prediction"

credentials = ApiKeyCredentials(in_headers={"Training-key": VISION_TRAINING_KEY})
trainer = CustomVisionTrainingClient(VISION_TRAINING_ENDPOINT, credentials)
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": VISION_PREDICTION_KEY})
predictor = CustomVisionPredictionClient(VISION_PREDICTION_KEY, prediction_credentials)

publish_iteration_name = "classifyModelWasteTyper"

# Create a new project
print ("Creating project...")
project_name = uuid.uuid4()
project = trainer.create_project(project_name)
# Make two tags in the new project
hemlock_tag = trainer.create_tag(project.id, "Hemlock")
cherry_tag = trainer.create_tag(project.id, "Japanese Cherry")

#  * * ** * * * * * * * * * * * * * * * * * * * *  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 

# TODO PREDICTION
# # Now there is a trained endpoint that can be used to make a prediction
# prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key_local_file})
# predictor = CustomVisionPredictionClient(ENDPOINT_LOCAL_FILE, prediction_credentials)

# path = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.NMwKLGTZzgNhzJmjsSpRXQHaHa%26pid%3DApi&f=1&ipt=e14c9566bb9b6dbf919d26e240026f2917d0d5aa60d50228ea92e53c16e75dc3&ipo=images"
# # with open(os.path.join (base_image_location, "Test/test_image.jpg"), "rb") as image_contents:
# with open(os.path.join (path), "rb") as image_contents:
#     results = predictor.classify_image(
#         project.id, publish_iteration_name, image_contents.read())

#     # Display the results.
#     for prediction in results.predictions:
#         print("\t" + prediction.tag_name +
#               ": {0:.2f}%".format(prediction.probability * 100))