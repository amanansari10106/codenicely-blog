import re
from blog import messages
def test_password(password, rePassword):
    # Regex pattern for password validation
    if password != rePassword:
        return {
            "success":False,
            "message":"Password Doesn't Match"            
        }
    
    
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    
    if re.match(pattern, password):
        return {
            "success":True        
        }
    else:
        return {
            "success":False,
            "message":messages.password_guidelines            
        }
    
    
def cresponse(sucess,message="", data={} ):
    return {
        "success":sucess,
        "message":message,
        "data":data
    }

def validateEmail(email):
    # pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    pattern = r'/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/'
    
    if re.match(pattern, email):
        return {
            "success":True,         
        }
    else:
        return {
            "success":False,
            "message":messages.emailUnvalid           
        }