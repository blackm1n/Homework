//Найти сумму элементов от M до N, N и M заданы
int SumNumbers(int M, int N)
{
    int sum = N;
    if (N > M)
        sum += SumNumbers(M, N - 1);
    return sum;
}

Console.Write("Введите M: ");
int M = int.Parse(Console.ReadLine() ?? "0");
Console.Write("Введите N: ");
int N = int.Parse(Console.ReadLine() ?? "0");

Console.WriteLine(SumNumbers(M, N));