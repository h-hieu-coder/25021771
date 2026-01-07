class Date : 
    def __init__(self, day, month, year):
        self.day = day
        self.month = month 
        self.year = year 
    
    def check(self): 
        res = True 
        if (self.year % 4 == 0 and self.year % 100 != 0) or self.year % 400 == 0 : 
            if self.month in [1, 3, 5, 7, 8, 10, 12] : 
                if not (self.day >= 1 and self.day <= 31) : 
                    res = False 
            elif self.month in [4, 6, 9, 11] : 
                if not (self.day >=1 and self.day <= 30) : 
                    res = False 
            elif self.month == 2 : 
                if not (self.day >=1 and self.day <= 29) :
                    res = False 
            else : 
                res = False
            
        else : 
            if self.month in [1, 3, 5, 7, 8, 10, 12] : 
                if not (self.day >= 1 and self.day <= 31) : 
                    res = False 
            elif self.month in [4, 6, 9, 11] : 
                if not (self.day >=1 and self.day <= 30) : 
                    res = False 
            elif self.month == 2 : 
                if not (self.day >=1 and self.day <= 28) :
                    res = False 
            else : res = False
        return res  
    

    def next_day(self) : 
        if (self.year % 4 == 0 and self.year % 100 != 0) or self.year % 400 == 0 : 
            if self.month in [1, 3, 5, 7, 8, 10] : 
                if (self.day >= 1 and self.day <= 30) : 
                    self.day += 1
                elif self.day == 31 : 
                    self.day = 1
                    self.month += 1 
            elif self.month == 12 : 
                if (self.day >= 1 and self.day <= 30) : 
                    self.day += 1
                elif self.day == 31 : 
                    self.day = 1
                    self.month = 1
                    self.year += 1
            elif self.month in [4, 6, 9, 11] : 
                if (self.day >=1 and self.day <= 29) : 
                    self.day += 1
                elif self.day == 30 : 
                    self.day = 1
                    self.month += 1
            else : 
                if (self.day >=1 and self.day <= 28) :
                    self.day += 1
                elif self.day == 29 : 
                    self.day = 1
                    self.month += 1

        else :
            if self.month in [1, 3, 5, 7, 8, 10] : 
                if (self.day >= 1 and self.day <= 30) : 
                    self.day += 1
                elif self.day == 31 : 
                    self.day = 1
                    self.month += 1 
            elif self.month == 12 : 
                if (self.day >= 1 and self.day <= 30) : 
                    self.day += 1
                elif self.day == 31 : 
                    self.day = 1
                    self.month = 1
                    self.year += 1
            elif self.month in [4, 6, 9, 11] : 
                if (self.day >=1 and self.day <= 29) : 
                    self.day += 1
                elif self.day == 30 : 
                    self.day = 1
                    self.month += 1
            else : 
                if (self.day >=1 and self.day <= 27) :
                    self.day += 1
                elif self.day == 28 : 
                    self.day = 1
                    self.month += 1
        
        return (self.day, self.month, self.year)

    
day,month,year = map(int, input().split("/"))
date = Date(day,month,year)
if not date.check() : 
    print("INVALID")
else : 
    n_day, n_month, n_year = date.next_day()
    print(str(n_day).rjust(2,'0'),str(n_month).rjust(2,'0'),str(n_year).rjust(4,'0'),sep = "/")

# hàm word.rjust(k,'x') : nếu word chua du k phan tu thi them vao truoc word mot so phan tu cho du k  