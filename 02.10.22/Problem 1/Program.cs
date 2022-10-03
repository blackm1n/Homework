//Дано число обозначающее день недели. Выяснить является номер дня недели выходным
Console.Write("Введите номер дня: ");
int day = int.Parse(Console.ReadLine() ?? "0");

if (day == 6 | day == 7) Console.WriteLine("Выходной! Можно отдыхать!");
else if (day > 0 && day < 6) Console.WriteLine("Пора на работу :(");
else Console.WriteLine("Не является номером дня");