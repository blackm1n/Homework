//Выяснить является ли число чётным
Console.Write("Введите число: ");
int number = int.Parse(Console.ReadLine() ?? "0");

if (number % 2 == 0) Console.WriteLine("Число четное");
else Console.WriteLine("Число нечетное");