//Написать программу масштабирования фигуры
void PrintArray(double[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        Console.Write($"({array[i, 0]}, {array[i, 1]}) ");
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

void ScaleShape(double[,] array, double k)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            array[i, j] = array[i, j] * k;
        }
    }
}

double[,] array = new double[4, 2];

FillArray(array);
PrintArray(array);

Console.Write("Введите k: ");
double k = double.Parse(Console.ReadLine() ?? "0");

ScaleShape(array, k);
PrintArray(array);
