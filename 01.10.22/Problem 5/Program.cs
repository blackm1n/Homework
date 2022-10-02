//Показать числа от -N до N
int number = int.Parse(Console.ReadLine()?? "0");
int i = -number;
while (i <= number)
{
    Console.Write(i + " ");
    i++;
}