//В прямоугольной матрице найти строку с наименьшей суммой элементов.
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

int RowWithLowestSum(int[,] array)
{
    int index = 1;
    int minsum = 0;
    int sum = 0;
    for (int i = 0; i < array.GetLength(0); i++)
    {
        sum = 0;
        for (int j = 0; j < array.GetLength(1); j++)
        {
            sum += array[i, j];
        }
        if (i == 0)
            minsum = sum;
        else if (sum < minsum)
        {
            minsum = sum;
            index = i + 1;
        }
    }
    return index;
}

Console.Write("Введите m: ");
int m = int.Parse(Console.ReadLine() ?? "0");
Console.Write("Введите n: ");
int n = int.Parse(Console.ReadLine() ?? "0");

int[,] array = new int[m, n];

FillArray(array);
PrintArray(array);

int result = RowWithLowestSum(array);
Console.WriteLine($"{result} строка имеет наименьшую сумму элементов");