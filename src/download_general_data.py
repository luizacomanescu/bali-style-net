from bing_image_downloader import downloader

# Download 100 images for each category
downloader.download("casual outfit street style", limit=100, output_dir='dataset/general/', adult_filter_off=True, force_replace=False, timeout=60)
downloader.download("fashion blogger chic outfit", limit=100, output_dir='dataset/general/', adult_filter_off=True, force_replace=False, timeout=60)
downloader.download("athleisure fashion", limit=100, output_dir='dataset/general/', adult_filter_off=True, force_replace=False, timeout=60)