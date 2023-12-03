from test import main                           
import io                                       
import sys                                      
import json                                     
import os                                       
                                                
arg = os.environ.get('ARGS')                    
answer = os.environ.get('ANSWER')               
json_arg = json.loads(arg.replace("'","\""))    
                                                
captured_output = io.StringIO()                 
sys.stdout = captured_output                    
                                                
return_output = main(*json_arg)                 
                                                
sys.stdout = sys.__stdout__                     
print_output = captured_output.getvalue()       
                                                
correct = str(return_output)==answer            
                                                
data = {                                        
    "Print" : print_output,                     
    "Return" : str(return_output),              
    "Solution" : answer,                        
    "Win" : correct                             
}                                               
                                                
json_string = json.dumps(data)                  
                                                
print(json_string)                              