//Написать программу копирования массива
void PrintArray(int[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        Console.Write($"{array[i]} ");
    }
    Console.WriteLine();
}

void FillArray(int[] array)
{
    var random = new Random();
    for (int i = 0; i < array.Length; i++)
    {
        array[i] = random.Next(-9, 9);
    }
}

int[] CopyArray(int[] array)
{
    int[] arraycopy = new int[array.Length];
    for (int i = 0; i < array.Length; i++)
    {
        arraycopy[i] = array[i];
    }
    return arraycopy;
}

Console.Write("Введите размер массива: ");
int m = int.Parse(Console.ReadLine() ?? "0");

int[] array = new int[m];

FillArray(array);
Console.Write("Ориг. - ");
PrintArray(array);
int[] array2 = CopyArray(array);
Console.Write("Копия - ");
PrintArray(array2);