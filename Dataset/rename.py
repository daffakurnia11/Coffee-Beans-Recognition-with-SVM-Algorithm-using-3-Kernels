import os

count = 1
dir_path = "C:/Users/LnData User/Documents/SEMESTER 7/FP SIFON/Coffee Beans Classification/Dataset/Tidak Cacad/"
files = os.listdir(dir_path)

for i in range(len(files)):
    os.rename(dir_path + files[i], f"{dir_path}Tidak Cacad{i+1}.jpg")
