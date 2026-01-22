#I am aware this is a bit messy, but it does work! :)

import re
import matplotlib.pyplot as plt

fname = "mbox.txt"
with open(fname, 'r') as file:
    fhand = file.read()

dayList = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
monthList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
monthNum = []
dayNum = []
j = 0

emailNum = re.findall('Date: 200[0-9]-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2} -[0-9]{4} \([a-zA-Z]{3}, [0-9]{2} [a-zA-Z]{3} [0-9]{4}\)', str(fhand)) #looking at 50 emails, Date: 200(?)- appears once every email

for i in monthList:
    monthList[j] = re.findall(monthList[j], str(emailNum))
    if monthList[j] != []:
        monthNum.append(monthList[j])
    j += 1
j=0
for i in dayList:
    dayList[j] = re.findall(dayList[j], str(emailNum))
    if dayList[j] != []:
        dayNum.append(dayList[j])
    j += 1
    
plt.hist(dayNum, bins=1, histtype='bar', edgecolor='black', label=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
plt.xlabel('Years in Article')
plt.title('Amount Of Emails Each Day In 2007-2008')
plt.legend()
plt.grid(axis='y')
plt.savefig('DayHistogram.png', dpi=200)
plt.show()

plt.hist(monthNum, bins=1, histtype='bar', edgecolor='black', label=['Jan 2008', 'Oct 2007', 'Nov 2007', 'Dec 2007'])
plt.xlabel('Months')
plt.title('Amount Of Emails Sent In 2007-2008')
plt.legend()
plt.grid(axis='y')
plt.savefig('MonthHistogram.png', dpi=200)
plt.show()

    

