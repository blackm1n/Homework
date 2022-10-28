//В двумерном массиве целых чисел. Удалить строку и столбец, на пересечении которых расположен наименьший элемент.
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

int[,] RemoveRowAndCollumnWithSmallestElement(int[,] array)
{
    int minelement = array[0, 0];
    int[] minposition = {0, 0};
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            if (array[i, j] < minelement)
            {
                minelement = array[i, j];
                minposition[0] = i;
                minposition[1] = j;
            }
        }
    }
    int[,] result = new int[array.GetLength(0)-1, array.GetLength(1)-1];
    for (int i = 0; i < result.GetLength(0); i++)
    {
        for (int j = 0; j < result.GetLength(1); j++)
        {
            if (i >= minposition[0] && j >= minposition[1])
                result[i, j] = array[i + 1, j + 1];
            else if (i >= minposition[0])
                result[i, j] = array[i + 1, j];
            else if (j >= minposition[1])
                result[i, j] = array[i, j + 1];
            else
                result[i, j] = array[i, j];
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

Console.WriteLine("До:");
PrintArray(array);

int[,] result = RemoveRowAndCollumnWithSmallestElement(array);

Console.WriteLine("После:");
PrintArray(result);