def custom_response(message,status,data):
    response={
        "message":message,
        "success":status,
        "data":data
    }
    return response