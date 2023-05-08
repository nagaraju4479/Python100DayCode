from PIL import Image
import os

# Get the absolute paths to the images
image1_path = os.path.relpath("PythonProjects\image1.jpg")
image2_path = os.path.relpath("PythonProjects\image1.jpg")

# Open the two images
image1 = Image.open(image1_path)
image2 = Image.open(image2_path)

# Resize the images to have the same dimensions
image1 = image1.resize((400, 400))
image2 = image2.resize((400, 400))

# Create a new image with the same dimensions as the two input images
result = Image.new("RGB", (800, 400))

# Paste the two images into the new image, side by side
result.paste(image1, (0, 0))
result.paste(image2, (400, 0))

# Blend the two images with an alpha value of 0.5
blended = Image.blend(image1, image2, 0.5)

# Save the blended image to a file
blended.save("C:\Users\Nagaraju\Documents\Python100DaysPractise\PythonProjects\blended.jpg")
