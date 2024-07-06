from PIL import Image

while True:
    characters = ["░","▒","▓"]
    imagePath = input("Image path: ")
    if __name__ == "__main__":
        pixelPer = 1
        image = Image.open(f'{imagePath}').resize((500,500)).convert("RGB")
        width = image.size[0]
        imagePaletted = list(image.getdata())
        i = 0
        while(i < len(imagePaletted)):
            brightness = imagePaletted[i][0] + imagePaletted[i][1] + imagePaletted[i][2]
            brightness = int(brightness * 3 / 768)
            print(characters[brightness], end="")
            if(i % width == 0):
                print("\n", end="")
                i += 5*width
            i += 5