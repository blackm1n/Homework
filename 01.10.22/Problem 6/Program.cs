// Показать четные числа от 1 до N
Console.Write("Введите число: ");
int number = int.Parse(Console.ReadLine()?? "0");
int i = 1;

while (i < number)
{
    if (i % 2 == 0) Console.Write(i + " ");
    i++;
}