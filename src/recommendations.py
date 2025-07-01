import os
import random

def get_recommendation_images(style_key, base_dir="/Users/luizacomanescu/git/bali-style-net/dataset/bali/", n=3):
    style_name = style_key.split("/")[-1]  # e.g., from "bali/relaxed" get "relaxed"
    style_dir = os.path.join(base_dir, style_name)

    if not os.path.exists(style_dir):
        return []

    images = [img for img in os.listdir(style_dir) if img.endswith((".jpg", ".jpeg", ".png"))]
    selected = random.sample(images, min(n, len(images)))
    return [os.path.join(style_dir, img) for img in selected]