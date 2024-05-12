def danger_level(x):
    return x**3 - 3*x**2 - 12*x + 10

def find_safe_depth(max_deviation):
    depth_low = 0
    depth_high = 4
    depth_mid = (depth_low + depth_high) / 2

    while abs(danger_level(depth_mid)) > max_deviation:
        if danger_level(depth_low) * danger_level(depth_mid) < 0:
            depth_high = depth_mid
        else:
            depth_low = depth_mid
        depth_mid = (depth_low + depth_high) / 2
    
    return depth_mid

def main():    
        max_deviation = float(input("Введите максимально допустимый уровень опасности: "))
        safe_depth = find_safe_depth(max_deviation)
        print("Приблизительная глубина безопасной кладки:", safe_depth, "м")
   
main()
