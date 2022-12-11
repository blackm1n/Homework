//Показать натуральные числа от M до N, N и M заданы
void ShowNumbers(int M, int N)
{
    if (N > M)
        ShowNumbers(M, N - 1);
    Console.Write($"{N} ");
}

Console.Write("Введите M: ");
int M = int.Parse(Console.ReadLine() ?? "0");
Console.Write("Введите N: ");
int N = int.Parse(Console.ReadLine() ?? "0");

ShowNumbers(M, N);