# main.py

import os
import datetime
from openai import OpenAI
from story_generator import generate_story_steps
from image_generator import generate_images
from video_creator import create_video

if __name__ == "__main__":
    # Initialize OpenAI client
    openai_client = OpenAI()


    # Specify the number of images to generate
    num_images = 15
    
    role = """You are a writer of prompt for image generation of an imaginative story. you have to imagine steps for this story, 
    for each steps you have to give 2 things :
    [ scene : the description of the scene (descriptive like you were describing a picture) , text : few words that tells the continous story to the viewer in french language !], 
    you have to do that in 150 characters maximum and give response in json format like this :
    {"steps":[{"scene": 'scene1 content',"text": 'text1 content'},{"scene":'scene2 content',"text":'text1 content'}]}
    """
    # Prompt for the story with instructions to separate steps by blank lines
    prompt = f"Write the story of skippy the dog obsessed by his wood stick to change that in {num_images} steps, give the same description of the guy in each scene so the pictures will be coherent, make sure to respect the content filters"
    globalinstruction = " this is a step of the story of a big fat  man that wear silly clothes marked by his rotund belly and thick limbs, photorealistic style"


    # # Generate story steps
    story_steps = generate_story_steps(openai_client, prompt, num_images,role)
    # print(story_steps)

    # Define the output folder for saving images with a timestamp
    # Obtenir la date et l'heure actuelles
    current_datetime = datetime.datetime.now()
    # Formatter la date et l'heure selon le format souhaité
    date_string = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
    # Utiliser la date formattée dans le nom du dossier de sortie
    output_folder = f"output/generated_images_{date_string}"

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Generate images based on the story steps and save them in the output folder
    generate_images(openai_client, story_steps, output_folder, num_images, globalinstruction)

    # Define the output video path
    video_path = os.path.join(output_folder, f"output_video.mp4")


    fps = 1/(55/num_images)  # You can adjust this value as needed
    # Create the video from the generated images
    create_video(output_folder, video_path, story_steps, fps)
