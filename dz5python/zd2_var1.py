import os
import datetime

date = str(datetime.date.today())
os.mkdir(date)
file = os.path.join(date, "text.txt")
open(file, 'a+').close()
vl_dir = os.path.join(date, "vl_dir")
os.mkdir(vl_dir)
newfile = os.path.join(vl_dir, os.path.basename(file))
os.rename(file, newfile)
