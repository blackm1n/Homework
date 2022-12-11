//Задать номер четверти, показать диапазоны для возможных координат
Console.Write("Введите номер четверти: ");
int number = int.Parse(Console.ReadLine() ?? "0");

if (number == 1) Console.WriteLine("X = (0, +Inf); Y = (0, +Inf)");
else if (number == 2) Console.WriteLine("X = (-Inf, 0); Y = (0, +Inf)");
else if (number == 3) Console.WriteLine("X = (-Inf, 0); Y = (-Inf, 0)");
else if (number == 4) Console.WriteLine("X = (0, +Inf); Y = (-Inf, 0)");
else Console.WriteLine("Не является номером четверти");