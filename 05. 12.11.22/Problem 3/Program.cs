//Написать программу вычисления функции Аккермана
int Akkerman(int m, int n)
{
    if (m > 0 && n == 0)
        return Akkerman(m - 1, 1);
    else if (m > 0 && n > 0)
        return Akkerman(m - 1, Akkerman(m, n - 1));
    else
        return n + 1;
}

Console.Write("Введите m: ");
int m = int.Parse(Console.ReadLine() ?? "0");
Console.Write("Введите n: ");
int n = int.Parse(Console.ReadLine() ?? "0");

Console.WriteLine(Akkerman(m, n));