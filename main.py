import csv 
import requests 
import xml.etree.ElementTree as ET 
from validations.status_code_20 import status_code_20
from validations.status_code_10 import status_code_10
from validations.status_code_01 import status_code_01
from validations.status_code_08 import status_code_08
from validations.status_code_11 import status_code_11
from validations.status_code_12 import status_code_12
from validations.status_code_13 import status_code_13
from validations.status_code_14 import status_code_14
from validations.status_code_21 import status_code_21
from validations.status_code_30 import status_code_30
from validations.status_code_32 import status_code_32
from validations.status_code_33 import status_code_33
from validations.status_code_40 import status_code_40
from validations.status_code_50 import status_code_50
from validations.status_code_51 import status_code_51
from validations.status_code_52 import status_code_52
from validations.status_code_53 import status_code_53
from validations.status_code_61 import status_code_61
from validations.status_code_70 import status_code_70
from validations.status_code_80 import status_code_80
from validations.status_code_81 import status_code_81
from validations.status_code_31 import status_code_31
from validations.status_code_60 import status_code_60
from validations.status_code_62 import status_code_62
  
def main():
    filepath = 'E:/Validation/Validation/files/shipment_status_wwa.14991480.20210302.073028.130.XML'
    errors = None
    warnings = None
    root, errors = read_file_xml(filepath)
    if not root:
        return  errors
    
    #Pending to validate status code from database ( gen_status = type L (status_code + type_of_move))
    status_code = get_status_code(root)
    if status_code:
        is_valid, errors ,warnings = run_validations(int(status_code), root)
    else:
        return 'Status code not found'
    return status_code, is_valid, errors, warnings



def run_validations(status_code, root):
    validations = {
        20 : status_code_20(root),
        10 : status_code_10(root),
        1 : status_code_01(root),
        8 : status_code_08(root),
        11 : status_code_11(root),
        12 : status_code_12(root),
        13 : status_code_13(root),
        14 : status_code_14(root),
        21 : status_code_21(root),
        30 : status_code_30(root),
        32 : status_code_32(root),
        33 : status_code_33(root),
        40 : status_code_40(root),
        50 : status_code_50(root),
        51 : status_code_51(root),
        52 : status_code_52(root),
        53 : status_code_53(root),
        61 : status_code_61(root),
        62 : status_code_62(root),
        70 : status_code_70(root),
        80 : status_code_80(root),
        81 : status_code_81(root),
        31 : status_code_31(root),
        60 : status_code_60(root)
    }
    return validations[status_code].run_all_validations()



def read_file_xml(path):
    try:
        tree = ET.parse(path)
        root = tree.getroot()
        return root, False
    except Exception as err:
        if type(err) == ET.ParseError:
            message = 'Malformed xml file'
        else:
            message = err
        return None, message



def get_status_code(root):
    for elem in root.iter('StatusCode'):
        status_code = elem.text
        return status_code
    return None


if __name__ == "__main__":
     
    print(main())