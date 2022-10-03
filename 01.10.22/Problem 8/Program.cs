//Показать вторую цифру трёхзначного числа
Console.Write("Введите трехзначное число: ");
int number = int.Parse(Console.ReadLine() ?? "0");

Console.WriteLine("Второе число: " + (number / 10) % 10);