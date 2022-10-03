//Удалить вторую цифру трёхзначного числа
Console.Write("Введите трехзначное число: ");
int number = int.Parse(Console.ReadLine() ?? "0");

int newnumber = (number / 100) * 10 + number % 10;

Console.WriteLine("Ваше число: " + newnumber);