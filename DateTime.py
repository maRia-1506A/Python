import datetime

a = datetime.datetime.now()
print("Current time:", a)
print("Day:", a.strftime("%A"))
print("Date:", a.strftime("%d"))
print("Month as number:", a.strftime("%m"))
print("Month full version:", a.strftime("%B"))
