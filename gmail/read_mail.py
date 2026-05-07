def get_latest_email(service):

    results = service.users().messages().list(
        userId='me',
        maxResults=1
    ).execute()

    messages = results.get('messages', [])

    if not messages:
        return None

    return messages[0]['id']