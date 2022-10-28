//Написать программу, которая в двумерном массиве заменяет строки на столбцы или сообщить, что это невозможно (в случае, если матрица не квадратная).
void PrintArray(int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            Console.Write($"{array[i, j]} ");
        }
        Console.WriteLine();
    }
}

void FillArray(int[,] array)
{
    var random = new Random();
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            array[i, j] = random.Next(-20, 21);
        }
    }
}

int[,]? RowsToCollumns(int[,] array)
{
    if (array.GetLength(0) != array.GetLength(1))
        return null;
    int[,] result = new int[array.GetLength(0), array.GetLength(1)];
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            result[i, j] = array[j, i];
            result[j, i] = array[i, j];
        }
    }
    return result;
}

Console.Write("Введите m: ");
int m = int.Parse(Console.ReadLine() ?? "0");
Console.Write("Введите n: ");
int n = int.Parse(Console.ReadLine() ?? "0");

int[,] array = new int[m, n];

FillArray(array);

int[,]? result = RowsToCollumns(array);
if (result != null)
{
    Console.WriteLine("До");
    PrintArray(array);
    Console.WriteLine("После");
    PrintArray(result);
}
else
    Console.WriteLine("Матрица не квадратная");