//Показать числа от -N до N
Console.Write("Введите число: ");
int number = int.Parse(Console.ReadLine()?? "0");
int i = -number;

while (i <= number)
{
    Console.Write(i + " ");
    i++;
}