namespace MyTest
{
    class Program
    {
        static int userNumber = 0;
        static int[] a = new int[3];
        static void Main(string[] args)
        {
            Console.WriteLine("Enter Your Number:");

            for (int i = 0; i < a.Length; i++)
            {
                a[i] = int.Parse(Console.ReadLine());
            }
            prnPermut(a, 0, a.Length - 1);
            Console.ReadLine();
        }
        public static void swapTwoNumber(ref int a, ref int b)
        {
            int temp = a;
            a = b;
            b = temp;
        }

        public static void prnPermut(int[] list, int k, int m)
        {
            int i;
            if (k == m)
            {
                for (i = 0; i <= m; i++)
                {
                    Console.Write("{0}", list[i]);
                }
                Console.WriteLine();
            }
            else
            {
                for (i = k; i <= m; i++)
                {
                    swapTwoNumber(ref list[k], ref list[i]);
                    prnPermut(list, k + 1, m);
                    swapTwoNumber(ref list[k], ref list[i]);
                }
            }

        }
    }
}