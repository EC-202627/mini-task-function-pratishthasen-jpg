def calculate_fine(book_title, days_overdue, daily_rate=5.0, max_fine=150.0):
    fine = days_overdue * daily_rate
    if fine > max_fine:
        fine = float(max_fine)
        print(f"Book: {book_title}")
        print(f"Days overdue: {days_overdue}")
        print(f"Fine: Rs. {fine}")
        print(f"You have accumulated the maximum fine of INR: {max_fine}")
    else:
        print(f"Book: {book_title}")
        print(f"Days overdue: {days_overdue}")
        print(f"Fine: Rs. {fine}")
book_title = input()
days_overdue = int(input())
daliy_rate = float(input())
calculate_fine(book_title, days_overdue, daily_rate)

