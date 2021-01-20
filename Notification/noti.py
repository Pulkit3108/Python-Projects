from pynotifier import Notification
t=input('Enter Title : ')
d=input('Enter Description : ')
n=int(input('Enter Duration : '))
Notification(title=t, description=d,duration=n).send()
