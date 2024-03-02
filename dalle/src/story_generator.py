# story_generator.py
import json

def generate_story_steps(openai_client, prompt, num_images,role):
    messages = [
        {"role": "system", "content": role},
        {"role": "user", "content": prompt},
    ]

    # Generate story steps using GPT-3
    story_response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1000  # Adjust max_tokens accordingly
    )
    print(story_response.choices[0].message.content)
   # Assuming story_steps contains the JSON-like string
    story_steps_json = story_response.choices[0].message.content

    # Convert JSON-like string to Python dictionary
    story_steps = json.loads(story_steps_json)

    # Convert dictionary to list of dictionaries
    # story_steps = [value for _, value in story_steps_dict.items()]

    

    return story_steps # Return only the specified number of steps