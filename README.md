
# JPGCompress

A simple Python tool to compress JPG images using the Pillow library.

## Description

JPGCompress allows you to easily reduce the file size of JPG images by adjusting the compression quality and optionally resizing the image. This can help save storage space and speed up image uploads or transfers.

## Features

- Compress JPG images by lowering JPEG quality.
- Optional resizing to limit image dimensions while maintaining aspect ratio.
- Easy to use with minimal dependencies.

## Requirements

- Python 3.x
- Pillow library

## Installation

Install the Pillow library via pip:

```
pip install Pillow
```

## Usage

Example usage in Python:

```
from jpg_compress import compress_jpg

input_file = "input.jpg"
output_file = "compressed.jpg"

# Compress with quality 30 and max width 800 pixels
compress_jpg(input_file, output_file, quality=30, max_width=800)
```

## Function Signature

```
def compress_jpg(input_path, output_path, quality=30, max_width=None, max_height=None):
    """
    Compress JPG image by reducing quality and optionally resizing.

    Args:
        input_path (str): Path to the original JPG image.
        output_path (str): Path to save the compressed JPG image.
        quality (int): JPEG quality (1-95), lower means more compression.
        max_width (int or None): Max width to resize image (preserving aspect ratio).
        max_height (int or None): Max height to resize image (preserving aspect ratio).
    """
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

