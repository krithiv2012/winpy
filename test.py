import os

# Function to check which IPs are not working 
def notWorkingIP(IP,IMGRD_port):
    # Converting the 2 lists into dictionary
    master_dict=[{k:v} for k,v in zip(IP,IMGRD_port)]
    # print(master_dict)
    not_working_list=[]
    for i in range(len(master_dict)):
        for ip,port in master_dict[i].items():
            cmd="C:\\Users\\S0121529\\Desktop\\lmutil.exe"  # Always use double backward slash here to avoid unicode escape error
            arg1="lmstat"
            arg2="-a"
            arg3="-c"
            command= cmd + " " + arg1 + " " + arg2 + " " + arg3 + " " + "{0}@{1}".format(port,ip)  
            # print(command)
            if i!=0:
                print('*'*150,end="")
            print()
            output=os.system(command)
            print(output,end=" ")
            print()
            # If the output is not zero then update the IPs and Port
            if output!=0:
                to_update={ip:port}
                not_working_list.append(to_update)
               
    print()
    print("Non working IP, Ports:")
    return not_working_list

# Main code
IP=[
    "10.94.134.3","10.94.134.3","10.94.134.3","10.94.134.3","10.94.134.3",
    "10.94.134.3","10.94.134.3","10.94.134.3","10.94.134.3","10.94.134.3","10.94.134.3",
    "10.94.152.17", 
    "10.94.134.2", "10.94.134.2","10.94.134.2","10.94.134.2","10.94.134.2",
    "Cawess133.ta1.tas-can.com",
    "Cawess133.ta1.tas-can.com"
    ]  # 19 ip addresses
IMGRD_port=[
       "42612", "3570", "42601", "4608", "1717", 
       "1717", "27000","42606", "27010", "250001","84000",
       "7788",
       "5280", "27002", "7788", "27000", "27001",
       "27000",
       "27001"
       ] # 19 ports # ip_addresses and ports need to be mapped correctly.


print(notWorkingIP(IP,IMGRD_port))
