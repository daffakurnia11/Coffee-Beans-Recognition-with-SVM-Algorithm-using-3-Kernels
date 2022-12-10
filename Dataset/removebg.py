from rembg import remove
from PIL import Image
import cv2
import os

dir_path = "C:/Users/LnData User/Documents/SEMESTER 7/FP SIFON/Coffee Beans Classification/Dataset/Cacad/"
files = os.listdir(f"{dir_path}Image/")

for i in range(len(files)):
    print(files[i])
    input = Image.open(f"{dir_path}Image/{files[i]}")

    width, height = input.size

    left = width / 4
    top = height / 4
    right = 3 * width / 4
    bottom = 3 * height / 4

    output = input.crop((left, top, right, bottom))
    output = output.save(f"{dir_path}Cropped/Cacad_cropped{i+1}.jpg")

    input = cv2.imread(f"{dir_path}Cropped/Cacad_cropped{i+1}.jpg")
    output = remove(input)
    cv2.imwrite(f"{dir_path}/Transparent/Cacad_transparent{i+1}.png", output)
