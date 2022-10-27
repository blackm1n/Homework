//Показать треугольник Паскаля *Сделать вывод в виде равнобедренного треугольника
int[,] PascalTriangle(int rows)
{
    int[,] pascal = new int[rows, rows*2+1];
    pascal[0, pascal.GetLength(1) / 2] = 1;
    for (int i = 0; i < pascal.GetLength(0)-1; i++)
    {
        int j = 0;
        while (pascal[i, j] == 0)
        {
            j++;
        }
        for (int k = 0; k < i + 2; k++)
        {
            pascal[i+1, j-1] = pascal[i, j-2] + pascal[i, j];
            j += 2;
        }
    }
    return pascal;
}

void PrintPascalTriangle(int[,] pascal)
{
    int max = 0;
    for (int i = 0; i < pascal.GetLength(0); i++)
    {
        for (int j = 0; j < pascal.GetLength(1); j++)
        {
            if(pascal[i, j] > max)
                max = pascal[i, j];
        }
    }
    string temp = max.ToString();
    int maxlength = temp.Length;
    int numberlength = 0;
    for (int i = 0; i < pascal.GetLength(0); i++)
    {
        for (int j = 0; j < pascal.GetLength(1); j++)
        {
            temp = pascal[i, j].ToString();
            numberlength = temp.Length;
            if(pascal[i, j] == 0)
                for (int k = 0; k < maxlength; k++)
                {
                    Console.Write(" ");
                }
            else
            {
                Console.Write($"{pascal[i, j]}");
                for (int k = 0; k < maxlength-numberlength; k++)
                {
                    Console.Write(" ");
                }
            }
        }
        Console.WriteLine();
    }
}

Console.Write("Введите строки: ");
int rows = int.Parse(Console.ReadLine() ?? "0");

int[,] pascal = PascalTriangle(rows);
PrintPascalTriangle(pascal);