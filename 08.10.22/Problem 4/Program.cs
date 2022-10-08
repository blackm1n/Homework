//Показать кубы чисел, заканчивающихся на четную цифру
Console.Write("Введите число: ");
int number = int.Parse(Console.ReadLine() ?? "0");
int index = 1;
double cube = 0;
while (index <= number)
{
    cube = Math.Pow(index, 3);
    if (cube % 2 == 0) Console.WriteLine(index + "^3 = " + cube);
    index++;
}