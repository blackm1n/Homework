//По двум заданным числам проверять является ли первое квадратом второго
Console.Write("Введите первое число: ");
double a = double.Parse(Console.ReadLine()?? "0");
Console.Write("Введите второе число: ");
double b = double.Parse(Console.ReadLine()?? "0");
if (Math.Pow(a, 2) == b) Console.Write(a+"^2 = "+b);
else Console.Write(a+"^2 != "+b);