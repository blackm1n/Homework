//Найти произведение двух матриц
//Я не знаю точно, что вы имеете ввиду под "произведением двух матриц". 
//Сам я понимаю как произведение каждого элемента первой матрицы на произведение соответсующего элемента другой матрицы.
//Но в интернете совершенно другое понимание, которое я оставлю как главное решение, а свое как побочное. Оно будет закоментировано.
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
            array[i, j] = random.Next(1, 10);
        }
    }
}

//Главное решение задачи.
int[,]? MultiplicationOfMatrixes(int[,] array, int[,] array2)
{
    if (array.GetLength(1) != array2.GetLength(0))
    {
        return null;
    }
    int[,] result = new int[array.GetLength(0), array2.GetLength(1)];
    for (int i = 0; i < result.GetLength(0); i++)
    {
        for (int j = 0; j < result.GetLength(1); j++)
        {
            for (int k = 0; k < array.GetLength(0); k++)
            {
                result[i, j] += array[i, k] * array2[k, j];
            }
        }
    }
    return result;
}

//Мое понимание задания до просмотра интернета.
/*int[,]? MultiplicationOfMatrixes(int[,] array, int[,] array2)
{
    if (array.GetLength(0) != array2.GetLength(0) || array.GetLength(1) != array2.GetLength(1))
    {
        return null;
    }
    int[,] result = new int[array.GetLength(0), array.GetLength(1)];
    for (int i = 0; i < result.GetLength(0); i++)
    {
        for (int j = 0; j < result.GetLength(1); j++)
        {
            result[i, j] = array[i, j] * array2[i, j];
        }
    }
    return result;
}*/

Console.Write("Введите m первой матрицы: ");
int m1 = int.Parse(Console.ReadLine() ?? "0");
Console.Write("Введите n первой матрицы: ");
int n1 = int.Parse(Console.ReadLine() ?? "0");

Console.Write("Введите m второй матрицы: ");
int m2 = int.Parse(Console.ReadLine() ?? "0");
Console.Write("Введите n второй матрицы: ");
int n2 = int.Parse(Console.ReadLine() ?? "0");

int[,] array = new int[m1, n1];
int[,] array2 = new int[m2, n2];

FillArray(array);
FillArray(array2);
Console.WriteLine("Первая матрица:");
PrintArray(array);
Console.WriteLine("Вторая матрица:");
PrintArray(array2);

int[,]? result = MultiplicationOfMatrixes(array, array2);
if (result != null)
{
    Console.WriteLine("Произведение матриц:");
    PrintArray(result);
}
else
    Console.WriteLine("Невозможно произвести произведение матриц");