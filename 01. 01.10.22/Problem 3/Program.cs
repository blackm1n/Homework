// Найти максимальное из трех чисел
double Max(double a, double b, double c)
{
    double max = 0;
    if (a > max) max = a;
    if (b > max) max = b;
    if (c > max) max = c;
    return max;
}

Console.Write("Введите первое число: ");
double a = double.Parse(Console.ReadLine() ?? "0");
Console.Write("Введите второе число: ");
double b = double.Parse(Console.ReadLine() ?? "0");
Console.Write("Введите третье число: ");
double c = double.Parse(Console.ReadLine() ?? "0");

Console.WriteLine("Максимальное: " + Max(a, b, c));