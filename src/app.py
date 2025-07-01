import streamlit as st
from PIL import Image
import torch
from torchvision import transforms
from recommendations import get_recommendation_images
import timm

# Define class names
class_names = ['general/casual', 'general/chic', 'general/sporty', 'bali/relaxed', 'bali/elegant', 'bali/adventurous']

# Load model
@st.cache_resource
def load_model():
    model = timm.create_model('swin_base_patch4_window7_224', pretrained=False, num_classes=6)
    model.load_state_dict(torch.load('/Users/luizacomanescu/git/bali-style-net/src/swin_model.pth', map_location=torch.device('cpu')))
    model.eval()
    return model

model = load_model()

# Image transforms
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])
])

# Prediction
def predict(img):
    image = transform(img).unsqueeze(0)
    with torch.no_grad():
        outputs = model(image)
        _, pred = torch.max(outputs, 1)
    return class_names[pred.item()]

# Streamlit UI
st.title("Bali Style Net ✨🌴")
st.write("Upload your outfit and see its Bali-style match!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("Classifying...")
    label = predict(image)
    st.success(f"Predicted Style: **{label}**")

    # Show Bali outfit recommendations
    st.subheader("Your Bali Style Inspiration ✨")
    recs = get_recommendation_images(label)
    if recs:
        cols = st.columns(len(recs))
        for col, img_path in zip(cols, recs):
            col.image(img_path, use_column_width=True)
    else:
        st.info("No recommendations available for this style.")