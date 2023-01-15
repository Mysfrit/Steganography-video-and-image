import random
from PIL import Image



# Prekonvertovanie dat do binárnej podoby podla ASCII tabulky
def covertDataFromString(data):
    newdata = []
    for i in data:
        newdata.append(format(ord(i), '08b'))
    return newdata


# Zmena pixelov v obrázku
def modifyPixels(imgdata, data, xxx):
    datalist = covertDataFromString(data)
    OrigX, OrigY = imgdata.size
    x = 0
    y = 0
    XXXindexion = 0

    for i in range(len(datalist)):

        pixelFragment = []
        for pixelBite in range(3):
            x += xxx[XXXindexion]

            if x >= OrigX:
                x = x % OrigX
                y += 1
            XXXindexion += 1
            print(f"{x},{y}")

            pixelFragment.append(imgdata.getpixel((x, y)))

        pixels = [a for b in pixelFragment for a in b]
        print(pixels)

        for j in range(0, 8):
            if (datalist[i][j] == '0') and (pixels[j] % 2 != 0):
                if (pixels[j] % 2 != 0):
                    pixels[j] -= 1

            elif (datalist[i][j] == '1') and (pixels[j] % 2 == 0):
                if (pixels[j] == 0):
                    pixels[j] += 1
                else:
                    pixels[j] -= 1

        # 0-pokracovant 1-skoncit
        if (i == len(datalist) - 1):
            if (pixels[-1] % 2 == 0):
                pixels[-1] -= 1
        else:
            if (pixels[-1] % 2 != 0):
                if(pixels[-1] == 0):
                    pixels[-1] += 1
                else:
                    pixels[-1] -= 1
        pixels = tuple(pixels)
        yield pixels[0:3]
        yield pixels[3:6]
        yield pixels[6:9]


# Samotné vkladanie jednotlivých zmenených pixelov do obrázku
def encodeToImage(newimg, data, password):
    random.seed(password)
    (x, y) = (0, 0)
    randIntList = list()
    OrigX, OrigY = newimg.size

    for i in range(int((OrigX * OrigY)/5)):
        randIntList.append(random.randint(1, 30))
    i = 0
    for pixel in modifyPixels(newimg.getdata(), data, randIntList):
        x += randIntList[i]
        if x >= OrigX:
            x = x % OrigX
            y += 1
        print(f"{x},{y}")
        print(pixel)
        newimg.putpixel((x, y), pixel)
        i += 1


# Dešifrovanie
def decodeFromImage(inputpath, password):
    image = Image.open(inputpath, 'r')
    random.seed(password)

    # Zhashovanie hesla

    data = ''
    imagedata = iter(image.getdata())

    xxx = list()
    sizeX, sizeY = image.getdata().size
    for interation in range(int((sizeX * sizeY) /5)):
        xxx.append(random.randint(1, 30))

    XXXindexion = 0
    OrigX, OrigY = image.size
    x = 0
    y = 0
    # Vybranie trojice pixelov, následné cítanie z nich
    while True:
        # for kkk in range(xxx[XXXindexion]):
        #    pixels = [value for value in imagedata.__next__()[:3] + imagedata.__next__()[:3] + imagedata.__next__()[:3]]

        # 4, 12, 21

        pixels123 = []

        for z in range(3):
            x += xxx[XXXindexion]

            if x >= OrigX:
                x = x % OrigX
                y += 1
            XXXindexion += 1
            print(f"{x},{y}")
            image.getpixel((x, y))
            pixels123.append(image.getpixel((x, y)))

        pixels = [a for b in pixels123 for a in b]

        # pixels = [value for value in imagedata.__next__()[:3] + imagedata.__next__()[:3] + imagedata.__next__()[:3]]

        # string na binárny string
        binarray = ''

        for i in pixels[:8]:
            if (i % 2 == 0):
                binarray += '0'
            else:
                binarray += '1'

        data += chr(int(binarray, 2))

        print(data)
        if (pixels[-1] % 2 != 0):
            return data


# Zašifrovanie
def encode(inputPath, outputPath, data, password):
    image = Image.open(inputPath, 'r')
    image = image.convert('RGB')

    newimg = image.copy()
    encodeToImage(newimg, data, password)
    newimg.save(outputPath)


# Formát obrázku
def imageFormatInfo(path):
    image = Image.open(path, 'r')
    if image.format == "JPEG":
        return True
    else:
        return False


# Presiahnutie množstva práva
def maxMessageLen(path, message):
    image = Image.open(path, 'r')
    if len(message) > ((image.height * image.width)/30):
        return False
    else:
        return True


# Maximálna dlžka správy
def imageMaxCharInfo(path):
    if path != "":
        image = Image.open(path, 'r')
        return str(int(((image.height * image.width)/30)))
