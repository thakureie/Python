import os, datetime
todaystr = datetime.date.today().isoformat()
if not os.path.exists(os.path.join('/home/build/test/sandboxes/', todaystr)):  
    os.mkdir(os.path.join('/home/build/test/sandboxes/', todaystr))
