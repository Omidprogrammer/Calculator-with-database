def get_number(prompt):
    while True:
        num_str = input(prompt).strip()
        try:
            num = float(num_str)
            return num
        except ValueError:
            print("❌ خطا: لطفاً یک عدد معتبر وارد کنید.")

def get_operator():
    valid_operators = ['+', '-', '*', '/']
    while True:
        op = input("عملگر مورد نظر خود را وارد کنید (+, -, *, /): ").strip()
        if op in valid_operators:
            return op
        print("❌ خطا: لطفاً یکی از عملگرهای معتبر را وارد کنید.")
