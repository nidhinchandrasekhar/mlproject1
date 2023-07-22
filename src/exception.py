import sys

def error_message_detail(errir,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error mesage[{2}]".format()
    return error_message
    



    