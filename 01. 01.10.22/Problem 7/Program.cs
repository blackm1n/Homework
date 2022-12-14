//Показать последнюю цифру трёхзначного числа
Console.Write("Введите трехзначное число: ");
int number = int.Parse(Console.ReadLine() ?? "0");

Console.WriteLine("Последнее число: " + number % 10);