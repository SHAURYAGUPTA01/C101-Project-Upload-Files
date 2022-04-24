import os
import dropbox

class TransferData:
    
    def __init__(self,access_token):
       self.access_token=access_token
       
    def uploadFile(self,fileFrom,fileto):
        dx=dropbox.Dropbox(self.access_token)
        
        for root,dirs,files in os.walk(fileFrom):
            relative_path=os.path.relpath(localpath,fileFrom)
            dropbox_path= os.path.join(fileto,relative_path)
            
            with open(localpath,'rb') as f:
                dropbox.files_upload(f.read(),dropbox_path,mode = WriteMode('overwrite'))
                
def main():
    access_token = "sl.BF2umM3B2XVFJzrzavDDyi4I3Q4vuRa84IoY30zFU3ReUS-5BY9tTAmcW8wauHkAWCprqSLUEyr4kA0RmMiIqiYhSohLtZ5FOlgsGEGBWNp0CdRfTGDcVFpYFxrSFFVoGPFl3ZChhYI"
    td = TransferData(access_token)
    fileFrom = input("enter folder transfer : ")
    fileTo = input("enter folder path : ")
    td.uploadFile(file_from,file_to)
    print("files have been moved successfully")

main()