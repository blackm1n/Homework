﻿//Найти третью цифру числа или сообщить, что её нет
Console.Write("Введите число: ");
int number = int.Parse(Console.ReadLine() ?? "0");

if (number > 100) 
{
    while (number > 1000) number = number / 10;
    Console.WriteLine("Третье число: " + number % 10);
}
else Console.WriteLine("Третье число не существует");