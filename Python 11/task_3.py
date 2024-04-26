size = int(input("Введите размер игры: "))
speed = int(input("Введите скорость: "))
downloaded = 0
sec = 0
while downloaded < size:
    sec += 1
    downloaded += speed
    if downloaded > size:
        downloaded = size
    percent = (downloaded / size) * 100
    print("Прошло", sec, "сек.", "Скачано", downloaded, "из", size, "Мб", f"({int(percent)}%)")
