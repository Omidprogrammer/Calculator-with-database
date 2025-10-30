from input_module import get_number, get_operator
from menu import show_menu
import database

def calculate(num1, num2, operator):
    error = None
    result = None
    try:
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                error = "❌ خطا: تقسیم بر صفر امکان‌پذیر نیست."
            else:
                result = num1 / num2
        else:
            error = "❌ خطا: عملگر نامعتبر."
    except Exception as e:
        error = f"❌ خطای غیرمنتظره: {str(e)}"
    return result, error

def main():
    print("🔹 به ماشین‌حساب فارسی خوش آمدید!")
    database.create_table()  # ساخت جدول در صورت عدم وجود
    while True:
        choice = show_menu()
        if choice == '1':  # انجام محاسبه جدید
            num1 = get_number("عدد اول را وارد کنید: ")
            operator = get_operator()
            num2 = get_number("عدد دوم را وارد کنید: ")

            result, error = calculate(num1, num2, operator)
            database.add_record(num1, operator, num2, result, error)

            if error:
                print(error)
            else:
                print(f"نتیجه: {num1} {operator} {num2} = {result}")

        elif choice == '2':  # نمایش تاریخچه
            history = database.get_history()
            if not history:
                print("🛈 هیچ تاریخچه‌ای موجود نیست.")
            else:
                print("📜 تاریخچه:")
                for h in history:
                    num1, operator, num2, result, error = h
                    if error:
                        print(f"{num1} {operator} {num2} → خطا: {error}")
                    else:
                        print(f"{num1} {operator} {num2} = {result}")

        elif choice == '3':  # پاک کردن تاریخچه
            database.clear_history()
            print("🗑️ تاریخچه پاک شد.")

        elif choice == '4':  # خروج
            print("👋 خداحافظ!")
            break

if __name__ == "__main__":
    main()
