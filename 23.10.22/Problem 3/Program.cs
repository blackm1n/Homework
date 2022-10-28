//Сформировать трехмерный массив не повторяющимися двузначными числами показать его построчно на экран выводя индексы соответствующего элемента
//Задание можно было сделать просто прибавляв один к каждому проследующему элементу... Но я решил сделать через рандом...
//Дополнительное решение в комментариях.
void PrintArrayWithIndexes(int[,,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            for (int k = 0; k < array.GetLength(2); k++)
            {
                Console.WriteLine($"{array[i, j, k]} - {i}, {j}, {k}");
            }
        }
    }
}

/*void FillArrayWithoutRepeat(int[,,] array)
{
    int n = 10;
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            for (int k = 0; k < array.GetLength(2); k++)
            {
                array[i, j, k] = n;
                n++;
            }
        }
    }
}*/

void FillArrayWithoutRepeat(int[,,] array)
{
    var random = new Random();
    int randnumber = 0;
    bool check = true;
    int m = 0;
    int[] memory = new int[array.GetLength(0) * array.GetLength(1) * array.GetLength(2)];
    for (int i = 0; i < memory.Length; i++)
    {
        memory[i] = 0;
    }
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            for (int k = 0; k < array.GetLength(2); k++)
            {
                check = true;
                while (check)
                {
                    check = false;
                    randnumber = random.Next(10, 100);
                    for (int l = 0; l < memory.Length; l++)
                    {
                        if (randnumber == memory[l])
                        {
                            check = true;
                            break;
                        }
                    }
                }
                array[i, j, k] = randnumber;
                memory[m] = randnumber;
                m++;
            }
        }
    }
}

Console.Write("Введите m: ");
int m = int.Parse(Console.ReadLine() ?? "0");
Console.Write("Введите n: ");
int n = int.Parse(Console.ReadLine() ?? "0");
Console.Write("Введите o: ");
int o = int.Parse(Console.ReadLine() ?? "0");

int[,,] array = new int[m, n, o];

if (m * n * o > 90)
    Console.WriteLine("Невозможно без повторений");
else
{
    FillArrayWithoutRepeat(array);
    PrintArrayWithIndexes(array);
}
