//Задать массив из 12 элементов, заполненных числами из [0,9]. Найти сумму положительных/отрицательных элементов массива
//Из-за условия задачи, отрицательных чисел в массиве не будут присутствовать, но код может с ними работать.
void FillArray(int[] arr)
{
    for (int i = 0; i < arr.Length; i++)
    {
        arr[i] = new Random().Next(0,10);
    }
}

int[] array = new int[12];
FillArray(array);

int possum = 0;
int negsum = 0;

for (int i = 0; i < array.Length; i++)
{
    if (array[i] > 0)
    {
        possum = possum + array[i];
    }
    else
    {
        negsum = negsum + array[i];
    }
}

Console.WriteLine($"Сумма положительных: {possum}");
Console.WriteLine($"Сумма отрицательных: {negsum}");