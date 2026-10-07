import sys
from networksecurity.logging.logger import logging

class NetworkSecurityException(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()

        self.line_no = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error occur in python script name {self.file_name} in line no {self.line_no} and the error message is {str(self.error_message)}"


if __name__ == "__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by zero execption occured")
        raise NetworkSecurityException(e,sys)