//В Указанном массиве вещественных чисел найдите разницу между максимальным и минимальным элементом
void FillArray(double[] arr)
{
    for (int i = 0; i < arr.Length; i++)
    {
        var random = new Random();
        arr[i] = Math.Sqrt(random.Next(1,26));
    }
}

void PrintArray(double[] arr)
{
    for (int i = 0; i < arr.Length; i++)
    {
        Console.Write($"{arr[i]} ");
    }
}

double DiffMinMax(double[] arr)
{
    double min = arr[0];
    double max = arr[0];
    for (int i = 0; i < arr.Length; i++)
    {
        if (arr[i] > max) max = arr[i];
        if (arr[i] < min) min = arr[i];
    }
    double result = max - min;
    return result;
}

Console.Write("Введите длину массива: ");
int length = int.Parse(Console.ReadLine() ?? "0");
double[] array = new double[length];
FillArray(array);
PrintArray(array);
Console.WriteLine();

double result = DiffMinMax(array);

Console.WriteLine($"Разница между максимальным и минимальным значением массива: {result}");