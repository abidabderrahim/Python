from PIL import Image

path = input("Enter the name of image: ")
image = Image.open(path)
print(f"current size of image : {image.size}")
x = int(input("Enter X : "))
y = int(input("Enter Y : "))
extentation = str(input("Enter extantion (png,svg...): "))
resize_image = image.resize((x,y))
resize_image.save(f'new_size_img.{extentation}')
