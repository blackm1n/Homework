//Найти произведение двух матриц
//Я не знаю точно, что вы имеете ввиду под "произведением двух матриц". 
//Как по мне это звучит что надо каждый элемент одной матрицы, 
//умножить на соответсующий элемент другой матрицы.
//Надеюсь, что это то, что вы имели ввиду.
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

int[,] MultiplicationOfMatrixes(int[,] array, int[,] array2)
{
    int[,] result = new int[array.GetLength(0), array.GetLength(1)];
    for (int i = 0; i < result.GetLength(0); i++)
    {
        for (int j = 0; j < result.GetLength(1); j++)
        {
            result[i, j] = array[i, j] * array2[i, j];
        }
    }
    return result;
}

Console.Write("Введите m: ");
int m = int.Parse(Console.ReadLine() ?? "0");
Console.Write("Введите n: ");
int n = int.Parse(Console.ReadLine() ?? "0");

int[,] array = new int[m, n];
int[,] array2 = new int[m, n];

FillArray(array);
FillArray(array2);
Console.WriteLine("Первая матрица:");
PrintArray(array);
Console.WriteLine("Вторая матрица:");
PrintArray(array2);

int[,] result = MultiplicationOfMatrixes(array, array2);
Console.WriteLine("Произведение матриц:");
PrintArray(result);