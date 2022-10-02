Console.Write("Введите первое число: ");
int a = int.Parse(Console.ReadLine()?? "0");
Console.Write("Введите второе число: ");
int b = int.Parse(Console.ReadLine()?? "0");
if (Math.Pow(a, 2) == b) Console.Write(a+"^2 = "+b);
else Console.Write(a+"^2 != "+b);