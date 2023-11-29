from datetime import datetime,time,date
import calendar
import pytest

class dateNtime : 
    Date=0
    Time=0
    year=0;month=0;day=0
    hours=0;minutes=0;seconds=0
    
    def _init_(self,*args):
        if len(args)==0:
            Date=datetime.utcnow().date()
            Time=datetime.utcnow().time()
        elif len(args)==1:
            Date=self.StringtoDate(args[0])
            Time=self.StringtoTime("0:0:0")
        elif len(args)==2:
            Date=self.StringtoDate(args[0])
            Time=self.StringtoTime(args[1])
        else :
            Date=datetime(args[2],args[1],args[0]).date()
            Time=self.StringtoTime(args[3])
        self.day=Date.day;self.month=Date.month;self.year=Date.year
        self.hours=Time.hour;self.minutes=Time.minute;self.seconds=Time.second
        self.Date=Date;self.Time=Time

    #Method to convert String to Date
    def StringtoDate(self,date):
        date= datetime.strptime(date,'%Y-%m-%d').date()
        return date
    
    #Method to convert String to Time
    def StringtoTime(self,time):
        time=datetime.strptime(time,'%H:%M:%S').time()
        return time
    
    #Method to get date and time in ISO format
    def ISOformat(self):
        #Date=datetime.strptime(Date,'%Y-%m-%d').date()
        #Time=datetime.strptime(Time,'%H:%M:%S').time()
        print("Date and Time in ISO format : ")
        print((self.Date).isoformat(),end=" ")
        print((self.Time).isoformat())
        print()
        
    #Method to get date and time in human readable format
    def HumanReadable(self):
        print("Date and Time in Human Readable format : ")
        m=str(self.Date.strftime("%B"))
        d=str(self.Date.day)
        y=str(self.Date.year)
        print(m,d+",",y,self.Time)
        
    #Method to Validate the given date    
    def validatedate(self,day,month,year):
        try:
            datetime(year,month,day)
            print("The given date is VALID\n")
            return 1
        except ValueError:
            print("The given date is INVALID\n")
            return 0
            
    #Method to get difference between two different dates
    def difference(self,date1,date2):
        date1=self.StringtoDate(date1)
        date2=self.StringtoDate(date2)
        diff=abs(date2-date1)
        print("The difference",diff.days,"days")
        return diff.days
        
    #Static Method to find day of the week
    @staticmethod
    def findDay(date):
        date = datetime.strptime(date, '%Y-%m-%d').weekday()
        return (calendar.day_name[date]) 
        
    
        

def test_WeekDay1():
  date = dateNtime.findDay("2023-11-28")
  assert date == "Tuesday"

def test_WeekDay2():
  date = dateNtime.findDay("2023-11-29")
  assert date == "Sunday"

def test_DateDifference1():
  DnT=dateNtime()
  value=DnT.difference("2023-11-28","2022-12-10")
  assert value==353

def test_DateDifference2():
  DnT=dateNtime()
  value=DnT.difference("2023-02-05","2020-09-10")
  assert value==353

def test_DateValidation1():
    DnT=dateNtime()
    value = DnT.validatedate(12,10,2023)
    assert value==1
  
def test_DateValidation2():
  DnT=dateNtime()
  value = DnT.validatedate(10,7,2023)
  assert value==0

def test_ISODisplay1():
  dnt4=dateNtime(7,1,2020,"15:00:00")
  dnt4.ISOformat()

def test_ISODisplay2():
  dnt4=dateNtime("2021-04-35", "12:10:01")
  dnt4.ISOformat()

def test_HumanReadableDisplay1():
  dnt4=dateNtime("2020-07-10")
  dnt4.HumanReadable()

def test_HumanReadableDisplay2():
  dnt4=dateNtime(7,13,2020,"15:00:00")
  dnt4.HumanReadable()