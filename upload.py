#import os
#ins = "pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib"
#os.system(ins)

from __future__ import print_function
import pickle
import os.path
from googleapiclient import errors
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']

def get_service():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)
    return service

    '''
    # Call the Drive v3 API
    file_metadata = {'name': 'data_new'}
    media = MediaFileUpload('data_new.csv',
                            mimetype='text/csv')
    file = service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    print('File ID: %s' % file.get('id'))

    file_metadata1 = {'name': 'data_old'}

    media1 = MediaFileUpload('data_old.csv',
                            mimetype='text/csv')
    file1 = service.files().create(body=file_metadata1,
                                  media_body=media1,
                                  fields='id').execute()
    print('File ID: %s' % file1.get('id'))
    '''
def update_file(service, file_id, new_filename):
  """Update an existing file's metadata and content.

  Args:
    service: Drive API service instance.
    file_id: ID of the file to update.
    new_filename: Filename of the new content to upload.

  Returns:
    Updated file metadata if successful, None otherwise.
  """
  try:
    # First retrieve the file from the API.
    #file = service.files().get(fileId=file_id).execute()
    #print(file)
    # File's new metadata.
    #file['title'] = new_title
    #file['description'] = str("last_update = " + datetime.strftime(datetime.now(),'%d-%m-%Y %H:%M'))
    #file['mimeType'] = new_mime_type
    file = {
        'name' :'cobagdrive'
    }

    # File's new content.
    media_body = MediaFileUpload(
        new_filename, mimetype='text/csv', resumable=True)

    # Send the request to the API.
    updated_file = service.files().update(
        fileId=file_id,
        body=file,

        media_body=media_body).execute()
    return updated_file
  except errors.HttpError as error:
    print ('An error occurred: %s' % error)
    return None
service = get_service()
update_file(service,"1SvlPWahahlj0fArcpfad4Fjn0ggs_NF-",'corona.csv')
update_file(service,"1Ui1LwT_exEje5BnRZC2fMHMBZH9T0eXL",'ekonomi.csv')



