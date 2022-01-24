import datetime, pytz
from .validation_service import all_validations

class status_code_10:

    def __init__(self, root):
        self.errors = []
        self.warnings = []
        self.ETSPortOfLoading = None
        self.validations = all_validations(root)
    
    def run_all_validations(self):
        if not self.validations.ReceivingWarehouse():
            self.errors.append('ReceivingWarehouse')

        if not self.validations.CutoffReceivingWarehouse():
            self.errors.append('CutoffReceivingWarehouse')
        
        if not self.validations.ContentType():
            self.errors.append('ContentType')
        
        #pending to validate WWAReference against database
        if not self.validations.BookingNumber():
            self.errors.append('BookingNumber')
        
        #Pending to validate with UN code
        if not self.validations.StatusLocationCode():
            self.errors.append('StatusLocationCode')
        
        #Pending to validate from UN provided location codes/gen_location_table
        if not self.validations.PlaceOfReceiptOrPortOfLoading():
            self.errors.append('PlaceOfReceipt Or PortOfLoading')
        
        if not self.validations.ETSPlaceOfReceiptOrETSPortOfLoading():
            self.errors.append('ETSPlaceOfReceipt Or ETSPortOfLoading')
        
        #Pending to validate from UN provided location codes/gen_location_table
        if not self.validations.PortOfDischargeAndPlaceOfDelivery():
            self.errors.append('PortOfDischarge or PlaceOfDelivery')
        
        if not self.validations.ETAPortOfDischargeAndETAPlaceOfDelivery():
            self.errors.append('ETAPortOfDischarge and ETAPlaceOfDelivery')
        
        if not self.validations.StatusDateTimeDetails():
            self.errors.append('StatusDateTimeDetails')
        
        #pending to validate from gen_Customer_Alias table from database
        if not self.validations.CustomerAlias():
            self.errors.append('CustomerAlias')
        
        #pending to validate WWAReference against database
        if not self.validations.WWAShipmentReference():
            self.warnings.append('WWAShipmentReference has spaces')
        
        if not self.validations.imageLinkOrImage():
            self.errors.append('imageLink and image')
        
        if not self.validations.ShipperReference():
            self.warnings.append('ShipperReference')
        
        if not self.validations.ForwarderReference():
            self.warnings.append('ForwarderReference')
        
        if not self.validations.ConsigneeReference():
            self.warnings.append('ConsigneeReference')
        
        if not self.validations.CommunicationReference():
            self.warnings.append('CommunicationReference')
        
        if not self.validations.PickupReference():
            self.warnings.append('PickupReference')
        
        if not self.validations.LotNo():
            self.errors.append('LotNo')
        
        if not self.validations.HouseBillOfLadingNumber():
            self.errors.append('HouseBillOfLadingNumber')
        
        if not self.validations.ContainerNumber():
            self.errors.append('ContainerNumber')
        
        if len(self.errors) > 0:
            return False, self.errors, self.warnings

        return True, self.errors, self.warnings


        
    # def ReceivingWarehouse(self):
    #     for elem in self.root.iter('ReceivingWarehouse'):
    #         if elem.text:
    #             return True
    #     return False

    # def CutoffReceivingWarehouse(self):
    #     for elem in self.root.iter('CutoffReceivingWarehouse'):
    #         try:
    #             datetime.datetime.strptime(elem.text, "%Y-%m-%d")
    #         except:
    #             return False
    #         return True
    #     return False
    
    # def ContentType(self):
    #     valid_content_types = ('PDF', 'JPEG', 'HTML', 'PNG', 'GIF')
    #     for elem in self.root.iter('ContentType'):
    #         if elem.text and elem.text.split('/')[1].upper() in  valid_content_types:
    #             return True
    #     return False
    
    # def BookingNumber(self):
    #     for elem in self.root.iter('BookingNumber'):
    #         if elem.text and len(elem.text) <= 20:
    #             return True
    #     return False
    
    # def StatusLocationCode(self):
    #     for elem in self.root.iter('StatusLocationCode'):
    #         if elem.text and len(elem.text) == 5:
    #             return True
    #     return False
    
    # def PlaceOfReceiptOrPortOfLoading(self):
    #     PlaceOfReceipt = False
    #     PortOfLoading = False
    #     for elem in self.root.iter('PlaceOfReceipt'):
    #         if elem.text and len(elem.text) == 5:
    #             PlaceOfReceipt = True
        
    #     for elem in self.root.iter('PortOfLoading'):
    #         if elem.text and len(elem.text) == 5:
    #             PortOfLoading = True
        
    #     if PlaceOfReceipt or PortOfLoading:
    #         return True
    #     return False
    
    # def ETSPlaceOfReceiptOrETSPortOfLoading(self):
    #     ETSPlaceOfReceipt = False
    #     ETSPortOfLoading = False
    #     for elem in self.root.iter('ETSPlaceOfReceipt'):
    #         try:
    #             datetime.datetime.strptime(elem.text, "%Y-%m-%d")
    #             ETSPlaceOfReceipt = True
    #             break
    #         except:
    #             ETSPlaceOfReceipt = False
        
    #     for elem in self.root.iter('ETSPortOfLoading'):
    #         try:
    #             self.ETSPortOfLoading = datetime.datetime.strptime(elem.text, "%Y-%m-%d")
    #             ETSPortOfLoading = True
    #             break
    #         except:
    #             ETSPortOfLoading = False
        
    #     if ETSPlaceOfReceipt or ETSPortOfLoading:
    #         return True
    #     return False
    
    # def PortOfDischargeAndPlaceOfDelivery(self):
    #     PortOfDischarge = False
    #     PlaceOfDelivery = False
    #     for elem in self.root.iter('PortOfDischarge'):
    #         if elem.text and len(elem.text) == 5:
    #             PortOfDischarge = True
        
    #     for elem in self.root.iter('PlaceOfDelivery'):
    #         if elem.text and len(elem.text) == 5:
    #             PlaceOfDelivery = True
        
    #     if PortOfDischarge or PlaceOfDelivery:
    #         return True
    #     return False
    
    # def ETAPortOfDischargeAndETAPlaceOfDelivery(self):
    #     ETAPortOfDischarge = False
    #     ETAPlaceOfDelivery = False
    #     for elem in self.root.iter('ETAPortOfDischarge'):
    #         try:
    #             ETAPortOfDischarge = datetime.datetime.strptime(elem.text, "%Y-%m-%d")
    #             break
    #         except:
    #             return False
        
    #     for elem in self.root.iter('ETAPlaceOfDelivery'):
    #         try:
    #             ETAPlaceOfDelivery = datetime.datetime.strptime(elem.text, "%Y-%m-%d")
    #             break
    #         except:
    #             return False
    #     if ETAPortOfDischarge and ETAPlaceOfDelivery and self.ETSPortOfLoading:
    #         date_diff = (ETAPlaceOfDelivery.date() - datetime.datetime.today().date()).days
    #         if date_diff > 180 or date_diff < -120:
    #             return False
    #         if ETAPlaceOfDelivery.date() < ETAPortOfDischarge.date():
    #             return False
    #         if self.ETSPortOfLoading.date() > ETAPortOfDischarge.date():
    #             return False
    #         return True
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
    
    # def WWAShipmentReference(self):
    #     for elem in self.root.iter('WWAShipmentReference'):
    #         if elem.text and not elem.text.__contains__(' '):
    #             return True
    #     return False
    
    # def imageLinkOrImage(self):
    #     image_link_present = False
    #     image_present = False
    #     for elem in self.root.iter('ImageLink'):
    #         if elem.text:
    #             image_link_present = True
    #     for elem in self.root.iter('Image'):
    #         if elem.text:
    #             image_present = True
    #     if image_link_present or image_present:
    #         return True
    #     return False

    # def ShipperReference(self):
    #     for elem in self.root.iter('ShipperReference'):
    #         if elem.text:
    #             if len(elem.text) > 30:
    #                 return False
    #     return True
    
    # def ForwarderReference(self):
    #     for elem in self.root.iter('ForwarderReference'):
    #         if elem.text:
    #             if len(elem.text) > 30:
    #                 return False
    #     return True
    
    # def ConsigneeReference(self):
    #     for elem in self.root.iter('ConsigneeReference'):
    #         if elem.text:
    #             if len(elem.text) > 30:
    #                 return False
    #     return True
    
    # def CommunicationReference(self):
    #     for elem in self.root.iter('CommunicationReference'):
    #         if elem.text:
    #             if len(elem.text) > 30:
    #                 return False
    #     return True
    
    # def PickupReference(self):
    #     for elem in self.root.iter('PickupReference'):
    #         if elem.text:
    #             if len(elem.text) > 30:
    #                 return False
    #     return True
    
    # def LotNo(self):
    #     for elem in self.root.iter('LotNo'):
    #         if elem.text:
    #             if len(elem.text) > 20:
    #                 return False
    #     return True
    
    # def HouseBillOfLadingNumber(self):
    #     for elem in self.root.iter('HouseBillOfLadingNumber'):
    #         if elem.text:
    #             if len(elem.text) > 30:
    #                 return False
    #     return True
    
    # def ContainerNumber(self):
    #     for elem in self.root.iter('ContainerNumber'):
    #         if elem.text:
    #             if len(elem.text) > 12:
    #                 return False
    #     return True