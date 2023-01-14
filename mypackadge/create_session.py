import pandas as pd
import os
import csv


class SessionCreate:
    def __init__(self, data=""):
        self.data = data
        # ["ip","username","password"]
        self.all_server = {}
        self.default_user = "pi"
        self.default_pass = "pi1"

        self.ip = []
        self.user_name = []
        self.password = []


    def save_sassion(self, file_path="servers.csv"):
        try:
            for ser in  self.data:
                cred = ser.split(",")
                ip = cred[0].split(".")
                if len(ip) >= 4:
                    if len(cred) < 2:
                        self.ip.append(cred[0])
                        self.user_name.append(self.default_user)
                        self.password.append(self.default_pass)

                    elif len(cred) < 3:
                        self.ip.append(cred[0])
                        self.user_name.append(cred[1])
                        self.password.append(self.default_pass)
                    
                    else:
                        self.ip.append(cred[0])
                        self.user_name.append(cred[1])
                        self.password.append(cred[2])
            
            # ["ip","username","password"]
            self.all_server["ip"] = self.ip
            self.all_server["username"] = self.user_name
            self.all_server["password"] = self.password

            df = pd.DataFrame(self.all_server)
            df.to_csv(file_path, columns=["ip","username","password"], index=False)
            return True
            
        except Exception as e:
            print("Error: ", e)
            return False
        
    def create_folders(self, root_folder):
        rt = f"logs/{root_folder}"
        for files in list(set(self.ip)):
            os.mkdir(f"{rt}/{files}")
            os.mkdir(f"{rt}/{files}/pre")
            os.mkdir(f"{rt}/{files}/post")
            os.mkdir(f"{rt}/{files}/res")


if __name__ == "__name__":
    ip_list = ['169.18.1.390,admini', '169.13.1.39,admini,root@123', 
        '169.15.1.39,admini,root@123', '169.171.39,pi1,root@123', '169.19.1.39,admini,root@12345', 
        '169.13.1.39,admini,root@123', '169.12.1.39,admini,root@123', '169.11.1.39,pi1,root@123', 
        '169.19.1.39,admini,root@12345', '169.15.1.39,admini,root@123', '169.14.1.39,admini,root@123', 
        '', '']

    a = SessionCreate(ip_list)
    a.save_sassion()




