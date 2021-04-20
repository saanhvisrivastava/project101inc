import dropbox
import os

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        #os.walk('top')
        #os.path.relpath('path')
       # os.path.join('path')
        f=open(file_from,'rb')
        dbx.files_upload(f.overwrite(),file_to)

def main():
    access_token='sl.AvQcejyspLuyn_yMItuwYr3TixaTOEMxSyTj7hDYcDU7cLbRcFaqByG45BpdxUKMiE25_600pU5jYUih0zYsgWlFvltWMqiDkT69xAzTt5ZI4yEOE0qFC2ShAuYdGyUQu12qHLo'
    transferData=TransferData(access_token)
    file_from=input("Enter the file path to transfer: ")
    file_to=input("Enter the full path to upload to dropbox: ")
    transferData.upload_file(file_from,file_to)
    print("File has been moved")


main()