 ```python
 def add(x, y):
     """2つの数値を加算する"""
     return x + y

 def subtract(x, y):
     """2つの数値を減算する"""
     return x - y

 if __name__ == "__main__":
     num1 = float(input("1つ目の数値を入力してください: "))
     num2 = float(input("2つ目の数値を入力してください: "))

     print("加算結果:", add(num1, num2))
     print("減算結果:", subtract(num1, num2))
 ```
