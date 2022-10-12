//В одномерном массиве из 123 чисел найти количество элементов из отрезка [10,99]
void FillArray(int[] arr, int min, int max)
{
    for (int i = 0; i < arr.Length; i++)
    {
        var random = new Random();
        arr[i] = random.Next(min,max);
    }
}

int CountArray(int[] arr)
{
    int count = 0;
    for (int i = 0; i < arr.Length; i++)
    {
        if (arr[i] >= 10 && arr[i] <= 99)
        {
            count++;
        }
    }
    return count;
}

int[] array = new int[123];
Console.Write("Введите минимальное число: ");
int min = int.Parse(Console.ReadLine() ?? "0");
Console.Write("Введите максималоное число: ");
int max = int.Parse(Console.ReadLine() ?? "0");
FillArray(array, min, max);

int count = CountArray(array);

Console.WriteLine($"Количество элементов в отрезке [10,99]: {count}");

