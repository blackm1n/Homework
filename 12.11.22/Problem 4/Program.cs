//Написать программу показывающие первые N чисел, для которых каждое следующее равно сумме двух предыдущих. Первые два элемента последовательности задаются пользователем
void CustomFibonacci(int N, int a, int b)
{
    Console.Write($"{a} ");
    if (N > 1)
        CustomFibonacci(N - 1, b, a+b);
}

Console.Write("Введите N: ");
int N = int.Parse(Console.ReadLine() ?? "0");
Console.Write("Введите a: ");
int a = int.Parse(Console.ReadLine() ?? "0");
Console.Write("Введите b: ");
int b = int.Parse(Console.ReadLine() ?? "0");

CustomFibonacci(N, a, b);