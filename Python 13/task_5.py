
start_amplitude = float(input("Введите начальную амплитуду: "))
stop_amplitude = float(input("Введите амплитуду остановки: "))
   

swings = 0
while start_amplitude > stop_amplitude:
    start_amplitude *= 0.916
    swings += 1

print(f"Маятник считается остановившимся через {swings} колебаний.")
