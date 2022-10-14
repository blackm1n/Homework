//В Указанном массиве вещественных чисел найдите разницу между максимальным и минимальным элементом

//Чтобы сделать вещественные числа, я использовал рандомайзер, и находил квадратный корень от его результата. Квадратные корни все же являются вещественными числами.
//Если вас это не устраивает, в комментариях предложен вариант с заранее написанным массивом вещественных чисел.
void FillArray(double[] arr)
{
    for (int i = 0; i < arr.Length; i++)
    {
        var random = new Random();
        arr[i] = Math.Sqrt(random.Next(1, 26));
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

//double[] array = {4.8820466521384146, 1.8731613694833507, 1.4142135623730951, 2.7182818284590452, 0.6270626783375392, 4.3415178392441032, 3.1415926535897932};

Console.Write("Введите длину массива: ");
int length = int.Parse(Console.ReadLine() ?? "0");
double[] array = new double[length];

FillArray(array);
PrintArray(array);
Console.WriteLine();

double result = DiffMinMax(array);

Console.WriteLine($"Разница между максимальным и минимальным значением массива: {result}");