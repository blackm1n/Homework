//Дано число из отрезка [10, 99]. Показать наибольшую цифру числа
Console.Write("Введите двухзначное число: ");
int number = int.Parse(Console.ReadLine() ?? "0");

if (number / 10 > number % 10) Console.WriteLine("Наибольшая цифра числа: " + number / 10);
else Console.WriteLine("Наибольшая цифра числа: " + number % 10);