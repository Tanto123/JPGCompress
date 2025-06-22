from PIL import Image
import os

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
    # Open the original image
    with Image.open(input_path) as img:
        # Resize if max width or height is specified
        if max_width or max_height:
            # Calculate new size preserving aspect ratio
            width, height = img.size
            aspect_ratio = width / height

            if max_width and width > max_width:
                width = max_width
                height = int(width / aspect_ratio)

            if max_height and height > max_height:
                height = max_height
                width = int(height * aspect_ratio)

            img = img.resize((width, height), Image.ANTIALIAS)

        # Save compressed image with specified quality
        img.save(output_path, "JPEG", optimize=True, quality=quality)

    # Print file size before and after compression
    original_size = os.path.getsize(input_path) / 1024
    compressed_size = os.path.getsize(output_path) / 1024
    print(f"Original size: {original_size:.2f} KB")
    print(f"Compressed size: {compressed_size:.2f} KB")

if __name__ == "__main__":
    # Example usage
    input_file = "input.jpg"      # Replace with your input JPG path
    output_file = "compressed.jpg" # Output compressed JPG path

    # Compress with quality=30 (lower quality = smaller file), resize max width=800 px
    compress_jpg(input_file, output_file, quality=30, max_width=800)
