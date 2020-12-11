#LOCALFILE = 'prime.csv'
#CLOUDFILE = '/primes.csv'

#!/usr/bin/env python3

import dropbox
from dropbox import DropboxOAuth2FlowNoRedirect

class data_transfer:
    def __init__(self,oauth_result):
        self.oauth_result = oauth_result
    def upload(self,LOCALFILE,CLOUDFILE):
        dxb = dropbox.Dropbox(oauth2_access_token=self.oauth_result)
        dxb.users_get_current_account()
        with open(LOCALFILE, 'rb') as f:
            dxb.files_upload(f.read(), CLOUDFILE)

#dat = data_transfer(oauth_result)

#dat.upload(LOCALFILE,CLOUDFILE)
