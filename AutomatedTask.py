import dropbox
import os
import time

start_time = time.time()

class TransferData:  
    def __init__(self,accessToken):
        self.accessToken = accessToken
    
    def upload_data(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.accessToken)

        for root,dirs,files in os.walk(file_from):
            for name in files:
                local_path = os.path.join(root,name)
                print(local_path)
                
                relative_path = os.path.relpath(local_path,file_from)
                dropbox_path = os.path.join(file_to,relative_path)
                print(relative_path)
                print(dropbox_path)
        
                with open(local_path,'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path)

def main():
    accessToken = "sl.A_4ePAc8iGctrzvzY2tR5S7ztYTgLy4-H4af82NNJexoYiRZo5KXq5-1CvlwkHILxFajMxpoTT8YYOGVAS39YencQ0Ao30n9DAd9Wdj0gwQ5HBvrjmNSGJSrMmBLRa7vmfLXtl0c_fW6"
    transferData = TransferData(accessToken)
    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to upload to dropbox: ")
    
    while(True):
        if((time.time()-start_time)>=300):
            transferData.upload_data(file_from,file_to)

if __name__ == '__main__':
    main()
            
    
            

    



