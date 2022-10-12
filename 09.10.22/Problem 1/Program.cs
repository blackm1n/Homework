//Задать массив из 8 элементов, заполненных нулями и единицами вывести их на экран
void FillArray(int[] arr)
{
    for (int i = 0; i < arr.Length; i++)
    {
        var random = new Random();
        arr[i] = random.Next(0,2);
    }
}

void PrintArray(int[] arr)
{
    for (int i = 0; i < arr.Length; i++)
    {
        Console.Write($"{arr[i]} ");
    }
}

int[] array = new int[8];
FillArray(array);
PrintArray(array);