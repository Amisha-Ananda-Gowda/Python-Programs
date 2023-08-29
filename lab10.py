from IPython.core.application import SYSTEM_CONFIG_DIRS
#Lab 10
#Write a pythn program to demonstrate init, str and add methods
class Time:
  def __init__(self,hour=0,minute=0, second=0):
    self.hour=hour
    self.minute=minute
    self.second=second
  def __str__(self):
    return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
  def __add__(self,other):
    h=self.hour+other.hour
    m=self.minute+other.minute
    s=self.second+other.second
    h=(h+m // 60)% 24
    m=(m+s // 60)% 60
    return Time(h,m,s % 60)
    print('----------------')
time1=Time()
print(time1)

print('----------------')
time2=Time(10,20,35)
print(time2)
print('----------------')
time3= Time(10,55, 40)

print('----------------')
time1=time2+time3
print(time1)