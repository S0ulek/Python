chattles = int(input("Сколько чаттлов? "))
cr_convert_coef = 1/2200
cr_out = chattles * cr_convert_coef
print("Это", cr_out, "CR" )
ship_price = 0.5
ships_can_buy = int(cr_out / ship_price)
print("Можно купить шаттлов:", ships_can_buy)