def dec_bin(dec): "Преобразование  десятичного числа в двоичную систему счисления"
 if dec == 0:
  return "0"
 elif dec > 0:
  return dec_bin(dec // 2) + str(dec % 2)
 else:
  return "-" + dec_bin(-dec)

def dec_oct(dec): "Преобразование  десятичного числа в восьмеричную систему счисления"
 if dec == 0:
  return "0"
 elif dec > 0:
  return dec_oct(dec // 8) + str(dec % 8)
 else:
  return "-" + dec_oct(-dec)

def dec_input(): "Ввод числа пользователем"
 try:
  dec_number = float(input("Введите десятичное число: "))
  if dec_number != int(dec_number):
   print("Введенное число - вещественное, оно преобразовано в целое.")
  return int(dec_number)
 except ValueError:
      print("Ошибка! Введите целое число.")
      return dec_input()

dec_number = dec_input()
bin_number = dec_bin(dec_number)
oct_number = dec_oct(dec_number)

print(f"Двоичное представление:", bin_number)
print(f"Восьмеричное представление:", oct_number)
