from torchvision.datasets import ImageFolder
from torchvision.datasets.folder import default_loader
import os

class NestedImageFolder(ImageFolder):
    def find_classes(self, directory):
        # Walk through subdirectories and ignore images directly in top-level folders
        classes = set()

        for root, dirs, _ in os.walk(directory):
            rel_path = os.path.relpath(root, directory)

            if rel_path == ".":
                continue  # Skip root

            if os.path.dirname(rel_path) == "":
                continue  # Skip top-level folders like 'bali/', 'general/'

            classes.add(rel_path.replace("\\", "/"))

        classes = sorted(classes)
        class_to_idx = {cls_name: i for i, cls_name in enumerate(classes)}
        return classes, class_to_idx

    def make_dataset(self, directory, class_to_idx, extensions=None, is_valid_file=None):
        instances = []
        directory = os.path.expanduser(directory)
        if extensions is None and is_valid_file is None:
            raise ValueError("Both extensions and is_valid_file cannot be None")

        def is_valid(path):
            if extensions is not None:
                return path.lower().endswith(extensions)
            return is_valid_file(path)

        for class_name in sorted(class_to_idx.keys()):
            class_index = class_to_idx[class_name]
            target_dir = os.path.join(directory, class_name)
            if not os.path.isdir(target_dir):
                continue

            for root, _, fnames in sorted(os.walk(target_dir)):
                for fname in sorted(fnames):
                    path = os.path.join(root, fname)
                    if is_valid(path):
                        item = (path, class_index)
                        instances.append(item)

        return instances