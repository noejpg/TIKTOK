import cv2
import os
from PIL import Image, ImageFont, ImageDraw
import numpy as np

def create_video(images_folder, video_path, story_steps, fps):
    """ Create a video from images in the given folder with text overlay using PIL. """

    # Get sorted list of images
    images = sorted([img for img in os.listdir(images_folder) if img.endswith(".jpg")], key=lambda x: int(x.split('_')[1]))

    # Read first image to get frame size
    frame = cv2.imread(os.path.join(images_folder, images[0]))
    height, width, _ = frame.shape

    # Define video codec and frame rate
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = fps

    # Load French font (replace with your desired path)
    font_path = "./fonts/TikTokDisplay-Medium.ttf"

    try:
        # Attempt to use getsize (newer PIL versions)
        font = ImageFont.truetype(font_path, size=36)  # Use "truetype" instead of "load_truetype"        text_width, text_height = font.getsize(step_text)  # Prefer this if available
    except AttributeError:
        # Fallback to textlength (older PIL versions)
        font = ImageFont.load_truetype(font_path, size=36)  # Adjust if necessary
    text_width = 10


    # Create video writer
    video = cv2.VideoWriter(video_path, fourcc, fps, (width, height))

    for i, image in enumerate(images):
        # Read image as PIL image
        pil_img = Image.open(os.path.join(images_folder, image))

        # Get text for the current step
        step_text = story_steps["steps"][i]["text"]

        # Create PIL drawing object
        draw = ImageDraw.Draw(pil_img)

        (text_width, baseline), (offset_x, offset_y) = font.font.getsize(story_steps["steps"][i]["text"])
        print(text_width)

        # Calculate text position
        text_x = (width - text_width) // 3  # Center text horizontally
        text_y = (height) - height // 3  # Slightly lower than the bottom

        # Draw text with black outline
        draw.text((text_x - 2, text_y - 2), step_text, font=font, fill=(0, 0, 0))  # Outline
        draw.text((text_x, text_y), step_text, font=font, fill=(255, 255, 255))  # Main text

        # Convert PIL image back to OpenCV format
        img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)  # Note: PIL uses RGB, OpenCV uses BGR

        # Write image with text overlay to the video
        video.write(img)

    # Release resources
    video.release()
