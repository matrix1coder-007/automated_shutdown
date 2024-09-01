import os
import csv
from datetime import datetime
from datetime import timedelta

"""
This should involve running the script when the VM starts and then counting the time from that time
"""

headers_in_log_file = ["vm_start_date", "vm_start_time", "vm_estimated_stop_date", "vm_estimated_stop_time", "vm_shut_down_date", "vm_shut_down_time"]

# current time when the script is run
vm_start_time = datetime.now()
print(vm_start_time)

vm_estimated_stop_time = vm_start_time + timedelta(minutes=1)
print(vm_estimated_stop_time)

i = 0

# runs the code infinitely
while 1 > 0:
    vm_shut_down_time = datetime.now()
    if vm_shut_down_time > vm_estimated_stop_time:
        print(vm_shut_down_time)
        i += 1
        vm_log_object = {
            "vm_start_date": vm_start_time.date(), 
            "vm_start_time": vm_start_time.time(), 
            "vm_estimated_stop_date": vm_estimated_stop_time.date(), 
            "vm_estimated_stop_time": vm_estimated_stop_time.time(), 
            "vm_shut_down_date": vm_shut_down_time.date(), 
            "vm_shut_down_time": vm_shut_down_time.time()
        }
        print(vm_log_object)

        if i == 1:
            with open("vm_log_sheet.csv", "a+", newline="") as log_file:
                csv_dict_writer = csv.DictWriter(log_file, fieldnames=headers_in_log_file)

                csv_dict_writer.writeheader()
                csv_dict_writer.writerow(vm_log_object)

            log_file.close()

            # shutting the system down here
            os.system("shutdown /s /t 1")
