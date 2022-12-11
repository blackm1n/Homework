// Найти расстояние между точками в пространстве 2D/3D
double twoD(double xa, double xb, double ya, double yb)
{
    double x = Math.Abs(xa - xb);
    double y = Math.Abs(ya - yb);
    double result = Math.Sqrt(Math.Pow(x, 2) + Math.Pow(y, 2));
    return result;
}

double threeD(double xa, double xb, double ya, double yb, double za, double zb)
{
    double x = Math.Abs(xa - xb);
    double y = Math.Abs(ya - yb);
    double z = Math.Abs(za - zb);
    double result = Math.Sqrt(Math.Pow(x, 2) + Math.Pow(y, 2) + Math.Pow(z, 2));
    return result;
}

Console.Write("Введите измерение: ");
int dimension = int.Parse(Console.ReadLine() ?? "0");
if (dimension == 2)
{
    Console.Write("Введите X координату точки A: ");
    double xa = double.Parse(Console.ReadLine() ?? "0");
    Console.Write("Введите Y координату точки A: ");
    double ya = double.Parse(Console.ReadLine() ?? "0");
    Console.Write("Введите X координату точки B: ");
    double xb = double.Parse(Console.ReadLine() ?? "0");
    Console.Write("Введите Y координату точки B: ");
    double yb = double.Parse(Console.ReadLine() ?? "0");
    
    Console.WriteLine("Дистанция между точками A и B: " + twoD(xa, xb, ya, yb));
}
else if (dimension == 3)
{
    Console.Write("Введите X координату точки A: ");
    double xa = double.Parse(Console.ReadLine() ?? "0");
    Console.Write("Введите Y координату точки A: ");
    double ya = double.Parse(Console.ReadLine() ?? "0");
    Console.Write("Введите Z координату точки A: ");
    double za = double.Parse(Console.ReadLine() ?? "0");
    Console.Write("Введите X координату точки B: ");
    double xb = double.Parse(Console.ReadLine() ?? "0");
    Console.Write("Введите Y координату точки B: ");
    double yb = double.Parse(Console.ReadLine() ?? "0");
    Console.Write("Введите Z координату точки B: ");
    double zb = double.Parse(Console.ReadLine() ?? "0");
    
    Console.WriteLine("Дистанция между точками A и B: " + threeD(xa, xb, ya, yb, za, zb));
}
else Console.WriteLine("Неправильное измерение");