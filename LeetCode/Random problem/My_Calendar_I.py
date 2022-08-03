# https://leetcode.com/problems/my-calendar-i/

class MyCalendar:
    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        for booked in self.calendar:
            if booked[0] <= start < booked[1] or booked[0] < end <= booked[1]:
                return False
            elif start < booked[0] and booked[1] < end:
                return False
        self.calendar.append([start, end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
