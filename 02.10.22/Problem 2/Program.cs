//По двум заданным числам проверять является ли одно квадратом другог
Console.Write("Введите первое число: ");
int a = int.Parse(Console.ReadLine() ?? "0");
Console.Write("Введите второе число: ");
int b = int.Parse(Console.ReadLine() ?? "0");

int min = a;
int max = b;

if (a > b)
{
    min = b;
    max = a;
} 

if (Math.Pow(min, 2) == max) Console.WriteLine(min + "^2 = " + max);
else Console.WriteLine(min + "^2 != " + max);
