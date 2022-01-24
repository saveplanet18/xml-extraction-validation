import datetime, pytz

class all_validations:

    def __init__(self, root):
        self.root = root
        self.ETSPortOfLoading = None

    def ReceivingWarehouse(self):
        for elem in self.root.iter('ReceivingWarehouse'):
            if elem.text:
                return True
        return False
    
    def CutoffReceivingWarehouse(self):
        for elem in self.root.iter('CutoffReceivingWarehouse'):
            try:
                datetime.datetime.strptime(elem.text, "%Y-%m-%d")
            except:
                return False
            return True
        return False
    
    def ContentType(self):
        valid_content_types = ('PDF', 'JPEG', 'HTML', 'PNG', 'GIF')
        for elem in self.root.iter('ContentType'):
            if elem.text and elem.text.split('/')[1].upper() in  valid_content_types:
                return True
        return False
    
    def BookingNumber(self):
        for elem in self.root.iter('BookingNumber'):
            if elem.text and len(elem.text) <= 20:
                return True
        return False
    
    def ShipperReference(self):
        for elem in self.root.iter('ShipperReference'):
            if elem.text:
                if len(elem.text) > 30:
                    return False
        return True
    
    def ForwarderReference(self):
        for elem in self.root.iter('ForwarderReference'):
            if elem.text:
                if len(elem.text) > 30:
                    return False
        return True
    
    def StatusLocationCode(self):
        for elem in self.root.iter('StatusLocationCode'):
            if elem.text and len(elem.text) == 5:
                return True
        return False
    
    def PlaceOfReceiptOrPortOfLoading(self):
        PlaceOfReceipt = False
        PortOfLoading = False
        for elem in self.root.iter('PlaceOfReceipt'):
            if elem.text and len(elem.text) == 5:
                PlaceOfReceipt = True
        
        for elem in self.root.iter('PortOfLoading'):
            if elem.text and len(elem.text) == 5:
                PortOfLoading = True
        
        if PlaceOfReceipt or PortOfLoading:
            return True
        return False
    
    def ETSPlaceOfReceiptOrETSPortOfLoading(self):
        ETSPlaceOfReceipt = False
        ETSPortOfLoading = False
        for elem in self.root.iter('ETSPlaceOfReceipt'):
            try:
                datetime.datetime.strptime(elem.text, "%Y-%m-%d")
                ETSPlaceOfReceipt = True
                break
            except:
                ETSPlaceOfReceipt = False
        
        for elem in self.root.iter('ETSPortOfLoading'):
            try:
                self.ETSPortOfLoading = datetime.datetime.strptime(elem.text, "%Y-%m-%d")
                ETSPortOfLoading = True
                break
            except:
                ETSPortOfLoading = False
        
        if ETSPlaceOfReceipt or ETSPortOfLoading:
            return True
        return False
    
    def PortOfDischargeAndPlaceOfDelivery(self):
        PortOfDischarge = False
        PlaceOfDelivery = False
        for elem in self.root.iter('PortOfDischarge'):
            if elem.text and len(elem.text) == 5:
                PortOfDischarge = True
        
        for elem in self.root.iter('PlaceOfDelivery'):
            if elem.text and len(elem.text) == 5:
                PlaceOfDelivery = True
        
        if PortOfDischarge or PlaceOfDelivery:
            return True
        return False
    
    def ETAPortOfDischargeAndETAPlaceOfDelivery(self):
        ETAPortOfDischarge = False
        ETAPlaceOfDelivery = False
        for elem in self.root.iter('ETAPortOfDischarge'):
            try:
                ETAPortOfDischarge = datetime.datetime.strptime(elem.text, "%Y-%m-%d")
                break
            except:
                pass
        
        for elem in self.root.iter('ETAPlaceOfDelivery'):
            try:
                ETAPlaceOfDelivery = datetime.datetime.strptime(elem.text, "%Y-%m-%d")
                break
            except:
                pass
        if ETAPortOfDischarge and ETAPlaceOfDelivery and self.ETSPortOfLoading:
            date_diff = (ETAPlaceOfDelivery.date() - datetime.datetime.today().date()).days
            if date_diff > 180 or date_diff < -120:
                return False
            if ETAPlaceOfDelivery.date() < ETAPortOfDischarge.date():
                return False
            if self.ETSPortOfLoading.date() > ETAPortOfDischarge.date():
                return False
            return True
        elif ETAPortOfDischarge or ETAPlaceOfDelivery:
            return True
        return False
    
    def StatusDateTimeDetails(self):
        for elem in self.root.iter('StatusDateTimeDetails'):
            if elem.__len__() == 3 and elem[0].text and elem[1].text and elem[2].text:
                try:
                    status_date = datetime.datetime.strptime(elem[0].text+elem[1].text, "%Y-%m-%d%H:%M:%S")
                    date_diff = (status_date.date() - datetime.datetime.today().date()).days
                    #Set timezone
                    timezone = pytz.timezone(elem[2].text)
                    status_date = timezone.localize(status_date)
                except:
                    return False
                if date_diff > -90 and date_diff <= 3:
                    return True
                return True
        return False
    
    def WWAShipmentReference(self):
        for elem in self.root.iter('WWAShipmentReference'):
            if elem.text and not elem.text.__contains__(' '):
                return True
        return False
    
    def imageLinkOrImage(self):
        image_link_present = False
        image_present = False
        for elem in self.root.iter('ImageLink'):
            if elem.text:
                image_link_present = True
        for elem in self.root.iter('Image'):
            if elem.text:
                image_present = True
        if image_link_present or image_present:
            return True
        return False
    
    def ConsigneeReference(self):
        for elem in self.root.iter('ConsigneeReference'):
            if elem.text:
                if len(elem.text) > 30:
                    return False
        return True
    
    def CommunicationReference(self):
        for elem in self.root.iter('CommunicationReference'):
            if elem.text:
                if len(elem.text) > 30:
                    return False
        return True
    
    def PickupReference(self):
        for elem in self.root.iter('PickupReference'):
            if elem.text:
                if len(elem.text) > 30:
                    return False
        return True
    
    def LotNo(self):
        for elem in self.root.iter('LotNo'):
            if elem.text:
                if len(elem.text) > 20:
                    return False
        return True
    
    def HouseBillOfLadingNumber(self):
        for elem in self.root.iter('HouseBillOfLadingNumber'):
            if elem.text:
                if len(elem.text) > 30:
                    return False
        return True
    
    def ContainerNumber(self):
        for elem in self.root.iter('ContainerNumber'):
            if elem.text:
                if len(elem.text) <= 12 and elem.text[0:4].isupper():
                    try:
                        for char in elem.text[0:4]:
                            if char.isdigit():
                                return False
                        int(elem.text[4:len(elem.text)])
                        return True
                    except:
                        return False
        return False
    
    def CustomerAlias(self):
        for elem in self.root.iter('CustomerAlias'):
            if elem.text:
                return True
        return False
    
    def LotNumber(self):
        for elem in self.root.iter('LotNumber'):
            if elem.text:
                if elem.text and len(elem.text) <= 20:
                    return True
        return False
    
    def SealNumber(self):
        for elem in self.root.iter('SealNumber'):
            if elem.text:
                if len(elem.text) > 20:
                    return False
        return True
    
    def OceanVEssel(self):
        for elem in self.root.iter('OceanVEssel'):
            if elem.text:
                if len(elem.text) > 50:
                    return False
        return True
    
    def ExceptionID(self):
        for elem in self.root.iter('ExceptionID'):
            if elem.text.lower() == 'weight' or elem.text.lower() == 'volume' or elem.text.lower() == 'piece' or elem.text.lower() == 'destination':
                return True
        return False
    
    def UOM(self):
        for elem in self.root.iter('UOM'):
            if elem.text.lower() == 'e' or elem.text.lower() == 'm':
                return True
        return False
    
    def ValueReceived(self):
        for elem in self.root.iter('ValueReceived'):
            if elem.text:
                if len(elem.text) <= 15:
                    return True
        return False
    
    def ValueBooked(self):
        for elem in self.root.iter('ValueBooked'):
            if elem.text:
                if len(elem.text) <= 15:
                    return True
        return False
    
    def ReleaseType(self):
        for elem in self.root.iter('ReleaseType'):
            if elem.text:
                if len(elem.text) == 1:
                    return True
        return False
    
    def ArrivalNoticeNumber(self):
        for elem in self.root.iter('ArrivalNoticeNumber'):
            if elem.text:
                return True
        return False