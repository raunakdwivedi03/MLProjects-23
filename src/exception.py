import sys
import logging

# Function to extract detailed error information
def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()  # Get exception traceback object
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get file name where error occurred
    error_message = "Error_occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)  # Format the error message
    )
    return error_message  # Return the detailed error message


# Custom exception class
class customException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)  # Call the base Exception constructor
        self.error_message = error_message_detail(error_message, error_detail)  # Store detailed error

    def __str__(self):
        return self.error_message  # When printed, return the detailed error message


