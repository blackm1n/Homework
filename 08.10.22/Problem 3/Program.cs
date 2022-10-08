Console.Write("Введите число: ");
int number = int.Parse(Console.ReadLine() ?? "0");
int index = 1;
int result = 1;
while (index <= number)
{
    result = result * index;
    index++;
}
Console.WriteLine(number + "! = " + result);