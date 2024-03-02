from gradio_client import Client

client = Client("AP123/SDXL-Lightning")
result = client.predict(
		"Hello!!",	# str  in 'Enter you image prompt:' Textbox component
		"1-Step",	# Literal['1-Step', '2-Step', '4-Step', '8-Step']  in 'Select inference steps' Dropdown component
		api_name="/generate_image_1"
)
print(result)