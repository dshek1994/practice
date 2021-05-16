#Creating a set

Days = set(["Mon","Tue","Wed","Thu","Fri","Sat"])
Months = {"Jan","Feb","Mar"}
Dates = {21,22,17}

Days.add("Sun")
Days.discard("Sun")
print(Days)