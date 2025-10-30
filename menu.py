def show_menu():
    while True:
        print("\nمنو:")
        print("1. محاسبه جدید")
        print("2. مشاهده تاریخچه")
        print("3. پاک کردن تاریخچه")
        print("4. خروج")
        choice = input("گزینه مورد نظر خود را وارد کنید: ").strip()
        if choice in ['1', '2', '3', '4']:
            return choice
        print("❌ گزینه نامعتبر است. لطفاً 1 تا 4 را وارد کنید.")
