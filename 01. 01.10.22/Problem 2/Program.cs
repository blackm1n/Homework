// По заданному номеру дня недели вывести его название
string[] day = { "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье" };

Console.Write("Введите номер дня: ");
int number = int.Parse(Console.ReadLine() ?? "0");

if (number > 0 && number < 8) Console.WriteLine(day[number - 1]);
else Console.WriteLine("Не является номером дня");