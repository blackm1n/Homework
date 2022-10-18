//В двумерном массиве заменить элементы, у которых оба индекса чётные на их квадраты
void PrintArray(double[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            Console.Write($"{array[i, j]} ");
        }
        Console.WriteLine();
    }
    Console.WriteLine();
}

void FillArray(double[,] array)
{
    var random = new Random();
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            array[i, j] = random.Next(-9, 10);
        }
    }
}

void EvenIndexToSquare(double[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            if (i % 2 == 0 && j % 2 == 0)
            {
                array[i, j] = Math.Pow(array[i, j], 2);
            }
        }
    }
}

Console.Write("Введите m: ");
int m = int.Parse(Console.ReadLine() ?? "0");
Console.Write("Введите n: ");
int n = int.Parse(Console.ReadLine() ?? "0");

double[,] array = new double[m, n];

FillArray(array);
PrintArray(array);
EvenIndexToSquare(array);
PrintArray(array);