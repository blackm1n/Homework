//Задать массив, заполнить случайными положительными трёхзначными числами. Показать количество нечетных\четных чисел
void FillArray(int[] arr)
{
    for (int i = 0; i < arr.Length; i++)
    {
        var random = new Random();
        arr[i] = random.Next(100,1000);
    }
}

Console.Write("Введите длину массива: ");
int length = int.Parse(Console.ReadLine() ?? "0");
int[] array = new int[length];
FillArray(array);

int even = 0;
int odd = 0;

for (int i = 0; i < array.Length; i++)
{
    if (array[i] % 2 == 0)
    {
        even++;
    }
    else
    {
        odd++;
    }
}

Console.WriteLine($"Количество четных чисел: {even}");
Console.WriteLine($"Количество нечетных чисел: {odd}");
