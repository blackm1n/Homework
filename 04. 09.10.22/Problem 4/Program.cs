//В одномерном массиве из 123 чисел найти количество элементов из отрезка [10,99]

//В условии не понятно, что именно подразумевается под "Количество элементов из отрезка [10,99]". Значения этих элементов или же индексы. 
//Мне показалось, что именно значения этих элементов, так как последнее, просто не имеет смысла, но оно присутсвует в комментариях.
void FillArray(int[] arr, int min, int max)
{
    for (int i = 0; i < arr.Length; i++)
    {
        var random = new Random();
        arr[i] = random.Next(min, max);
    }
}

/*int CountArray(int[] arr)
{
    int count = 0;
    for (int i = 0; i < arr.Length; i++)
    {
        if (i >= 10 && i <= 99)
        {
            count++;
        }
    }
    return count;
}*/

int CountArray(int[] arr)
{
    int count = 0;
    for (int i = 0; i < arr.Length; i++)
    {
        if (arr[i] >= 10 && arr[i] <= 99)
        {
            count++;
        }
    }
    return count;
}

int[] array = new int[123];

Console.Write("Введите минимальное число: ");
int min = int.Parse(Console.ReadLine() ?? "0");
Console.Write("Введите максималоное число: ");
int max = int.Parse(Console.ReadLine() ?? "0");
FillArray(array, min, max);

int count = CountArray(array);

Console.WriteLine($"Количество элементов в отрезке [10,99]: {count}");

