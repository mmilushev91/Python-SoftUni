book_pages = int(input())
read_pages_per_hour = int(input())
days_to_read_book = int(input())

#1. calculate pages to read for a day
pages_per_day = book_pages / days_to_read_book

#2. calculate reading hours per day
reading_hours_per_day = int(pages_per_day / read_pages_per_hour)

#3. print reading hours per day
print(reading_hours_per_day)
