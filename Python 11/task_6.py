print("Введите расположение коня: ")
knight_x = float(input())
knight_y = float(input())
print("Введите место на доске: ")
board_x = float(input())
board_y = float(input())

knight_cell_x = int(knight_x * 10)
knight_cell_y = int(knight_y * 10)
board_cell_x =  int(board_x * 10) 
board_cell_y  = int(board_y * 10)

can_move = abs(knight_cell_x - board_cell_x) == 2 and abs(knight_cell_y - board_cell_y) == 1 or \
           abs(knight_cell_x - board_cell_x) == 1 and abs(knight_cell_y - board_cell_y) == 2

if can_move:
    print("Конь в клетке:",knight_cell_x,",",knight_cell_y,"\nТочка в клетке:",board_cell_x,",",board_cell_y, "\nДа, конь может ходить в эту точку.")
else:
    print("Нет, конь не может ходить в эту точку.")
