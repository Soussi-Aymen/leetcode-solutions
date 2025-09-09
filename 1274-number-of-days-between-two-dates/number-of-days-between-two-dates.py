class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def is_leap(year: int) -> bool:
            return  (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
        
        def days_from_1971(y: int, m: int, d: int) -> int:
            days = 0
            for year in range(1971, y):
                days += 366 if is_leap(year) else 365
            for month in range(1,m):
                if month == 2 and is_leap(y): 
                    days += 29
                else:
                    days += days_of_month[month-1]

            return days + d
        
        y1, m1, d1 = map(int, date1.split("-"))
        y2, m2, d2 = map(int, date2.split("-"))

        return abs(days_from_1971(y1, m1, d1) - days_from_1971(y2, m2, d2))