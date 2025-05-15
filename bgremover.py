from rembg import remove 
from PIL import Image

input_path = 'madmax.jpg'
output_path = 'madmax.png'

try:
    inp = Image.open(input_path)
    output = remove(inp)
    output.save(output_path)
    Image.open(output_path).show()
except FileNotFoundError:
    print(f"File not found: {input_path}")
except Exception as e:
    print(f"An error occurred: {e}")