import datetime, pytz
from .validation_service import all_validations

class status_code_51:

    def __init__(self, root):
        self.errors = []
        self.warnings = []
        self.ETSPortOfLoading = None
        self.validations = all_validations(root)
    
    def run_all_validations(self):

        if not self.validations.CutoffReceivingWarehouse():
            self.errors.append('CutoffReceivingWarehouse')
        
        if not self.validations.ShipperReference():
            self.warnings.append('ShipperReference')
        
        if not self.validations.ForwarderReference():
            self.warnings.append('ForwarderReference')
        
        if not self.validations.BookingNumber():
            self.errors.append('BookingNumber')
        
        if not self.validations.HouseBillOfLadingNumber():
            self.errors.append('HouseBillOfLadingNumber')
        
        if not self.validations.PlaceOfReceiptOrPortOfLoading():
            self.errors.append('PlaceOfReceipt Or PortOfLoading')
        
        if not self.validations.ETSPlaceOfReceiptOrETSPortOfLoading():
            self.errors.append('ETSPlaceOfReceipt Or ETSPortOfLoading')
        
        if not self.validations.PortOfDischargeAndPlaceOfDelivery():
            self.errors.append('PortOfDischarge or PlaceOfDelivery')
        
        if not self.validations.ETAPortOfDischargeAndETAPlaceOfDelivery():
            self.errors.append('ETAPortOfDischarge and ETAPlaceOfDelivery')
        
        if not self.validations.StatusDateTimeDetails():
            self.errors.append('StatusDateTimeDetails')

        if len(self.errors) > 0:
            return False, self.errors, self.warnings

        return True, self.errors, self.warnings