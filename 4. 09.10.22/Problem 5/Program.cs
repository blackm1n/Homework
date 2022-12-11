//Найти сумму чисел одномерного массива стоящих на нечетной позиции
void FillArray(int[] arr, int min, int max)
{
    for (int i = 0; i < arr.Length; i++)
    {
        var random = new Random();
        arr[i] = random.Next(min, max);
    }
}

void PrintArray(int[] arr)
{
    for (int i = 0; i < arr.Length; i++)
    {
        Console.Write($"{arr[i]} ");
    }
}

int OddSumArray(int[] arr)
{
    int sum = 0;
    for (int i = 0; i < arr.Length; i++)
    {
        if (i % 2 == 1)
        {
            sum = sum + arr[i];
        }
    }
    return sum;
}

Console.Write("Введите длину массива: ");
int length = int.Parse(Console.ReadLine() ?? "0");
int[] array = new int[length];

Console.Write("Введите минимальное число: ");
int min = int.Parse(Console.ReadLine() ?? "0");
Console.Write("Введите максималоное число: ");
int max = int.Parse(Console.ReadLine() ?? "0");
FillArray(array, min, max);
PrintArray(array);
Console.WriteLine();

int sum = OddSumArray(array);

Console.WriteLine($"Сумма элементов с нечетным индексом: {sum}");
