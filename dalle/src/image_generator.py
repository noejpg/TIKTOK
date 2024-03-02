# image_generator.py
import os
from urllib.request import urlretrieve

def generate_images(openai_client, story_steps, output_folder, num_images,globalinstruction = ""):

    print(story_steps)
    i = 0
    # Generate images based on the story steps using DALL-E
    for step in story_steps["steps"]:
        i+=1
        print(step)
        # Generate an image based on the story step using DALL-E
        image_response = openai_client.images.generate(
            model="dall-e-3",
            prompt=step['scene'] + globalinstruction,  # Accessing 'scene' from the current step dictionary
            size="1024x1024",
            quality="standard",
            n=1  # Generate one image per step
        )

        # Retrieve the image URL and save the image
        image_url = image_response.data[0].url
        filename = os.path.join(output_folder, f"step_{i}_image.jpg")
        urlretrieve(image_url, filename)
        print(f"Step {i} image saved as {filename}")