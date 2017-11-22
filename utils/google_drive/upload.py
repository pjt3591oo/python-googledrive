from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import os


CLIENT_SECRET_FILE = './config/google/google_drive_secret_key.json'
CREDENTIAL_DIR = './config/google/upload'
CREDENTIAL_FILENAME = 'drive-python-upload.json'

SCOPES = 'https://www.googleapis.com/auth/drive.file'

def up(filename):
    try:
        import argparse
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    except ImportError:
        flags = None

    if not os.path.exists(CREDENTIAL_DIR):
        os.makedirs(CREDENTIAL_DIR)
    credential_path = os.path.join(CREDENTIAL_DIR, CREDENTIAL_FILENAME)


    store = file.Storage(credential_path)
    creds = store.get()

    if not creds or creds.invalid:
        print("make new storage data file ")
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        creds = tools.run_flow(flow, store, flags) \
                if flags else tools.run(flow, store)

    DRIVE = build('drive', 'v3', http=creds.authorize(Http()))

    FILES = (
        (filename),
    )

    for file_title in FILES:
        file_name = file_title
        metadata = {'name': file_name,
                    'mimeType': None
                    }

        res = DRIVE.files().create(body=metadata, media_body=file_name).execute()
        if res:
            print('Uploaded "%s" (%s)' % (file_name, res['mimeType']))
            print('Uploaded "%s" (%s)' % (file_name, res))
