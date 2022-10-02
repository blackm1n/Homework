//По двум заданным числам проверять является ли первое квадратом второго
Console.Write("Введите первое число: ");
double a = double.Parse(Console.ReadLine()?? "0");
Console.Write("Введите второе число: ");
double b = double.Parse(Console.ReadLine()?? "0");
if (Math.Pow(b, 2) == a) Console.Write(b+"^2 = "+a);
else Console.Write(b+"^2 != "+a);