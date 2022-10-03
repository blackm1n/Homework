//По двум заданным числам проверять является ли первое квадратом второго
Console.Write("Введите первое число: ");
int a = int.Parse(Console.ReadLine() ?? "0");
Console.Write("Введите второе число: ");
int b = int.Parse(Console.ReadLine() ?? "0");

if (Math.Pow(b, 2) == a) Console.Write(b + "^2 = " + a);
else Console.Write(b + "^2 != " + a);