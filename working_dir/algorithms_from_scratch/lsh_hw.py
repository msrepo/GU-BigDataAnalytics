import os
import csv
import sys
import numpy as np
from PIL import Image

# Paths
input_csv = "datasets/cs246/hw1-bundle/q4/data/patches.csv"
output_dir = "datasets/cs246/hw1-bundle/q4/data/image_patches"
html_file = "image_gallery.html"

# Plots images at the specified rows and saves them each to files.
def plot(A, row_nums, base_filename):
    for row_num in row_nums:
        patch = np.reshape(A[row_num, :], [20, 20])
        im = Image.fromarray(patch)
        if im.mode != 'RGB':
            im = im.convert('RGB')
        im.save(base_filename + "-" + str(row_num) + ".png")

# Loads the data into a np array, where each row corresponds to
# an image patch -- this step is sort of slow.
# Each row in the data is an image, and there are 400 columns.
def load_data(filename):
    return np.genfromtxt(filename, delimiter=',')

        
# Create output directory for images
os.makedirs(output_dir, exist_ok=True)

img_patches_np = load_data(input_csv)  # Load the data from the CSV file
plot(img_patches_np, range(0, len(img_patches_np)), os.path.join(output_dir, "patch"))  # Plot the first 10 patches

print(f"Images saved in '{output_dir}'.")

# Generate the HTML gallery
print("Generating HTML gallery...")
images = sorted(os.listdir(output_dir))  # List of image files
images_per_page = 50  # 10 columns x 5 rows
num_pages = (len(images) + images_per_page - 1) // images_per_page

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Gallery</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; }
        .gallery { display: flex; flex-wrap: wrap; justify-content: center; margin: 20px; }
        .gallery img { margin: 5px; width: 50px; height: 50px; object-fit: cover; }
        .pagination { text-align: center; margin: 20px; }
        .pagination a { margin: 0 5px; text-decoration: none; color: blue; }
        .pagination a.active { font-weight: bold; color: black; }
    </style>
</head>
<body>
"""

# Generate pages
for page in range(num_pages):
    html_content += f'<div class="gallery" id="page-{page + 1}" style="display: {"block" if page == 0 else "none"};">\n'
    start_index = page * images_per_page
    end_index = start_index + images_per_page
    for image in images[start_index:end_index]:
        html_content += f'    <img src="{output_dir}/{image}" alt="{image}">\n'
    html_content += "</div>\n"

# Add pagination
html_content += """
<div class="pagination">
"""
for page in range(num_pages):
    html_content += f'<a href="javascript:void(0);" class="{"active" if page == 0 else ""}" onclick="showPage({page + 1})">{page + 1}</a>\n'
html_content += """
</div>
<script>
    function showPage(page) {
        const pages = document.querySelectorAll('.gallery');
        const links = document.querySelectorAll('.pagination a');
        pages.forEach((p, index) => {
            p.style.display = (index === page - 1) ? 'block' : 'none';
        });
        links.forEach((link, index) => {
            link.className = (index === page - 1) ? 'active' : '';
        });
    }
</script>
</body>
</html>
"""

# Save the HTML file
with open(html_file, "w") as file:
    file.write(html_content)

print(f"HTML gallery saved as '{html_file}'.")