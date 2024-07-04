import uuid

def session_id():
    return str(uuid.uuid4())[:8]