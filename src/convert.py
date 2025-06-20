from PIL import Image
import os

def convert_all_to_jpg(root_folder):
    for root, _, files in os.walk(root_folder):
        for file in files:
            file_lower = file.lower()
            file_path = os.path.join(root, file)

            if file_lower.endswith('.png') or file_lower.endswith('.webp') or file_lower.endswith('.jpeg'):
                jpg_path = os.path.splitext(file_path)[0] + '.jpg'
                try:
                    img = Image.open(file_path).convert('RGB')
                    img.save(jpg_path, 'JPEG')
                    os.remove(file_path)
                    print(f'Converted {file_path} → {jpg_path}')
                except Exception as e:
                    print(f'Error converting {file_path}: {e}')

if __name__ == '__main__':
    dataset_folder = '/Users/luizacomanescu/git/bali-style-net/dataset'
    convert_all_to_jpg(dataset_folder)