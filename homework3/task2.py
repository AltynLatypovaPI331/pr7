def dec_tri(dec): #Преобразование  десятичного числа в троичную систему счисления
 if dec == 0:
  return "0"
 elif dec > 0:
  return dec_tri(dec // 3) + str(dec % 3)
 else:
  return "-" + dec_tri(-dec)
def dec_input(): #Ввод числа пользователем
 try:
  dec_number = float(input("Введите десятичное число: "))
  if dec_number != int(dec_number):
   print("Введенное число - вещественное, оно преобразовано в целое.")
  return int(dec_number)
 except ValueError:
      print("Ошибка! Введите целое число.")
      return dec_input()

dec_number = dec_input()
tri_number = dec_tri(dec_number)
print(f"Троичное представление:", tri_number)
