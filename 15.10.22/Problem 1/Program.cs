//Найти точку пересечения двух прямых заданных уравнением y = k1 * x + b1, y = k2 * x + b2, b1 k1 и b2 и k2 заданы
Console.Write("Введите k1: ");
double k1 = int.Parse(Console.ReadLine() ?? "0");
Console.Write("Введите b1: ");
double b1 = int.Parse(Console.ReadLine() ?? "0");
Console.Write("Введите k2: ");
double k2 = int.Parse(Console.ReadLine() ?? "0");
Console.Write("Введите b2: ");
double b2 = int.Parse(Console.ReadLine() ?? "0");

double x = (b2 - b1)/(k1 - k2);

double y = k1 * x + b1;

Console.WriteLine($"({x}, {y})");