//Выяснить, кратно ли число заданному, если нет, вывести остаток.
Console.Write("Введите число: ");
int a = int.Parse(Console.ReadLine() ?? "0");
Console.Write("Введите заданное число: ");
int b = int.Parse(Console.ReadLine() ?? "0");

if (a % b == 0) Console.WriteLine("Число кратно");
else Console.WriteLine("Число не кратно. Остаток: " + a % b);