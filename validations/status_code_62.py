import datetime, pytz
from .validation_service import all_validations

class status_code_62:

    def __init__(self, root):
        self.errors = []
        self.warnings = []
        self.ETSPortOfLoading = None
        self.validations = all_validations(root)
    
    def run_all_validations(self):

        if not self.validations.ArrivalNoticeNumber():
            self.errors.append('ArrivalNoticeNumber')
        
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