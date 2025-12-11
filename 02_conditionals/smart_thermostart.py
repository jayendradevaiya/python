device_status = "active"
temp = 3

if device_status == 'active':
   
    if temp > 35:
        print(f"high temperature and temp is :{temp}")
    else:
        print(f"normal temperature and temp is :{temp}")
else:
    print(f"your device is not active")