# Importing the necessary libraries
import torch
import requests
from PIL import Image
from torchvision import transforms
import gradio as gr

# Load the pre-trained model
model = torch.hub.load('pytorch/vision:v0.6.0', 'resnet18', pretrained=True).eval()

# Download human-readable labels for ImageNet.
response = requests.get("https://git.io/JJkYN")
labels = response.text.split("\n")

# Define the predict function
def predict(inp):
    # Convert the input image to a tensor
    inp = transforms.ToTensor()(inp).unsqueeze(0)
    # Make a prediction
    with torch.no_grad():
        prediction = torch.nn.functional.softmax(model(inp)[0], dim=0)
        confidences = {labels[i]: float(prediction[i]) for i in range(1000)}
    return confidences

# Define the interface
demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(num_top_classes=5),
    title="Image Classification",
    description="An image classification demo using ResNet-18 model.",
)

# Launch the interface
demo.launch()