#! /usr/bin/env python3

from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import io
from apiclient.http import MediaIoBaseDownload

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

CREDENTIAL_DIR = './config/google/download'
CREDENTIAL_FILENAME = 'drive-python-download.json'

CLIENT_SECRET_FILE = './config/google/google_drive_secret_key.json'
APPLICATION_NAME = 'Google Drive File Download'

SCOPES = 'https://www.googleapis.com/auth/drive.readonly'

EXCEL = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'


def __get_credentials():
    credential_dir = CREDENTIAL_DIR
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, CREDENTIAL_FILENAME)

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def down(file_id, exported_file_name):
    credentials = __get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)

    request = service.files().export_media(fileId=file_id, mimeType=EXCEL)
    fh = io.FileIO(exported_file_name, 'wb')
    downloader = MediaIoBaseDownload(fh, request)

    done = False

    while done is False:
        status, done = downloader.next_chunk()
        print('Download %d%%.' % int(status.progress() * 100))