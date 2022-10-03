//Программа проверяет пятизначное число на палиндромом.
Console.Write("Введите пятизначное число: ");
int number = int.Parse(Console.ReadLine() ?? "0");

int fhalf = number / 1000;
int shalf = number % 100;

if (fhalf / 10 == shalf % 10 && fhalf % 10 == shalf / 10) Console.WriteLine("Число является палиндромом");
else Console.WriteLine("Число не является палиндромом");