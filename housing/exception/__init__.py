import os
import sys

class HousingException(Exception):
    
    def __init__(self, error_message:Exception,error_detail:sys):
        super().__init__(error_message)
        self.error_message = HousingException.getDetailedErrorMessage(error_message =error_message,
                                                                       error_detail = error_detail)

    @staticmethod
    def getDetailedErrorMessage(error_message:Exception,error_detail:sys)->str:
        """
        Args:
            error_message (Exception): Exception object
            error_detail (sys): object of sys module

        Returns:
            str: error message
        """
        _,_,exec_tb = error_detail.exc_info()
        line_name = exec_tb.tb_frame.f_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename
        error_message = f"Error occured in script :[{file_name}] at line number:[{line_name}] and Error message is [{error_message}]"



        return error_message

    def __str__(self):
        return self.error_message   

    def __repr__(self) -> str:
        return HousingException,__name__.str() 


    


