//Найти третью цифру числа или сообщить, что её нет
Console.Write("Введите число: ");
string number = Console.ReadLine() ?? "0";

if (number.Length > 2) Console.WriteLine(number[2]);
else Console.WriteLine("Третье число не существует");