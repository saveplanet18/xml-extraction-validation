import datetime, pytz
from .validation_service import all_validations

class status_code_11:

    def __init__(self, root):
        self.errors = []
        self.warnings = []
        self.validations = all_validations(root)
    
    def run_all_validations(self):
        #pending to validate WWAReference against database
        if not self.validations.BookingNumber():
            self.errors.append('BookingNumber')
        
        if not self.validations.ContentType():
            self.errors.append('ContentType')
        
        if not self.validations.StatusLocationCode():
            self.errors.append('StatusLocationCode')
        
        if not self.validations.StatusDateTimeDetails():
            self.errors.append('StatusDateTimeDetails')
        
        if not self.validations.CustomerAlias():
            self.errors.append('CustomerAlias')
        
        if len(self.errors) > 0:
            return False, self.errors, self.warnings

        return True, self.errors, self.warnings
        
    
    # def BookingNumber(self):
    #     for elem in self.root.iter('BookingNumber'):
    #         if elem.text and len(elem.text) <= 20:
    #             return True
    #     return False
    
    # def ContentType(self):
    #     valid_content_types = ('PDF', 'JPEG', 'HTML', 'PNG', 'GIF')
    #     for elem in self.root.iter('ContentType'):
    #         if elem.text and elem.text.split('/')[1].upper() in  valid_content_types:
    #             return True
    #     return False
    
    # def StatusDateTimeDetails(self):
    #     for elem in self.root.iter('StatusDateTimeDetails'):
    #         if elem.__len__() == 3 and elem[0].text and elem[1].text and elem[2].text:
    #             try:
    #                 status_date = datetime.datetime.strptime(elem[0].text+elem[1].text, "%Y-%m-%d%H:%M:%S")
    #                 #Set timezone
    #                 timezone = pytz.timezone(elem[2].text)
    #                 status_date = timezone.localize(status_date)
    #             except:
    #                 return False
    #             return True
    #     return False
    
    # def CustomerAlias(self):
    #     for elem in self.root.iter('CustomerAlias'):
    #         if elem.text:
    #             return True
    #     return False
    
    # def StatusLocationCode(self):
    #     for elem in self.root.iter('StatusLocationCode'):
    #         if elem.text and len(elem.text) == 5:
    #             return True
    #     return False