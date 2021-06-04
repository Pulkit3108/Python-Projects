import time
from plyer import notification
if __name__=="__main__":
        print('----------------------------')
        print('DESKTOP REMINDER')
        print('----------------------------')
        t=input("Enter Title Of The Reminder : ")
        d=input("Enter Description Of The Reminder : ")
        m=int(input("Enter The Number Of Minutes (After Which You Want To Be Reminded) : "))
        time.sleep(m*60)
        notification.notify(
                title = t,
                message= d ,
                timeout=10,
                app_icon='noti.ico',
        )