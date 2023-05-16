import os
def handle_uploaded_file(file ,type_ ):
    if type_ == 'xlsx':
        with open("api/services/data.xlsx", "wb+") as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        try:
            os.remove("api/services/data.csv")
        except OSError:
            print(f"Error handling {OSError.__name__}")
    else:
        with open("api/services/data.csv", "wb+") as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        try:
            os.remove("api/services/data.xlsx")
        except OSError:
            print(f"Error handling {OSError.__name__}")
    return f'{type_} file uploaded Successfully'