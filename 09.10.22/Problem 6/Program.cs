//Найти произведение пар чисел в одномерном массиве. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
void FillArray(int[] arr, int min, int max)
{
    for (int i = 0; i < arr.Length; i++)
    {
        var random = new Random();
        arr[i] = random.Next(min,max);
    }
}

void PrintArray(int[] arr)
{
    for (int i = 0; i < arr.Length; i++)
    {
        Console.Write($"{arr[i]} ");
    }
}


Console.Write("Введите длину массива: ");
int length = int.Parse(Console.ReadLine() ?? "0");
int[] array = new int[length];
Console.Write("Введите минимальное число: ");
int min = int.Parse(Console.ReadLine() ?? "0");
Console.Write("Введите максималоное число: ");
int max = int.Parse(Console.ReadLine() ?? "0");
FillArray(array, min, max);
PrintArray(array);
Console.WriteLine();

int pair = 0;

for (int i = 0; i < array.Length/2; i++)
{
    pair = array[i] * array[array.Length-i-1];
    Console.WriteLine($"{array[i]} * {array[array.Length-i-1]} = {pair}");
}