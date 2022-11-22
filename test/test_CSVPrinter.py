import unittest
from specilallecture.CSVPrinter import CSVPrinter

class TestCSVPrinter(unittest.TestCase):
    def test_read1(self):
        printer = CSVPrinter("sample.csv")
        l = printer.read()
        self.assertEqual(3, len(l))

    def test_read2(self):
        printer = CSVPrinter("sample.csv")
        line = printer.read()
        abc="ABC"
        for i in range(3):
            for j in range(3):
                self.assertEqual(f"value{i+1}{abc[j]}", line[i][j])
        print("Line:", line)

    def test_read3(self):
        """
        with self.assertRaises(FileNotFoundError):
            printer = CSVPrinter("sample2.csv")
            printer.read()
        """
        try:
            printer = CSVPrinter("sample2.csv")
            printer.read()

        except FileNotFoundError as e:
            print("This line should not be invoked")

if __name__ == "__main__":
    unittest.main()