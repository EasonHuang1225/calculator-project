import math


class Calculator:
    def add(self, a, b):
        """加法運算"""
        return a + b
    
    def subtract(self, a, b):
        """減法運算"""
        return a - b
    
    def multiply(self, a, b):
        """乘法運算"""
        return a * b
    
    def divide(self, a, b):
        """除法運算"""
        if b == 0:
            raise ValueError("除數不能為零")
        return a / b
    
    def square_root(self, a):
        """平方根運算"""
        if a < 0:
            raise ValueError("無法計算負數的平方根")
        return math.sqrt(a)

def main():
    calc = Calculator()
    
    print("簡易計算機")
    print("===========")
    print("操作選項:")
    print("1: 加法")
    print("2: 減法")
    print("3: 乘法")
    print("4: 除法")
    print("5: 平方根")  # 新增選項
    print("q: 退出")
    
    while True:
        choice = input("\n請選擇操作 (1/2/3/4/5/q): ")
        
        if choice == 'q':
            print("感謝使用，再見！")
            break
        
        if choice not in ['1', '2', '3', '4', '5']:
            print("無效的選擇，請重試")
            continue
        
        try:
            if choice == '5':
                num = float(input("請輸入一個數字: "))
                try:
                    result = calc.square_root(num)
                    print(f"結果: √{num} = {result}")
                except ValueError as e:
                    print(f"錯誤: {e}")
            else:
                num1 = float(input("請輸入第一個數字: "))
                num2 = float(input("請輸入第二個數字: "))

            if choice == '1':
                result = calc.add(num1, num2)
                print(f"結果: {num1} + {num2} = {result}")
            elif choice == '2':
                result = calc.subtract(num1, num2)
                print(f"結果: {num1} - {num2} = {result}")
            elif choice == '3':
                result = calc.multiply(num1, num2)
                print(f"結果: {num1} * {num2} = {result}")
            elif choice == '4':
                try:
                    result = calc.divide(num1, num2)
                    print(f"結果: {num1} / {num2} = {result}")
                except ValueError as e:
                    print(f"錯誤: {e}")
        except ValueError:
            print("請輸入有效的數字")

if __name__ == "__main__":
    main()