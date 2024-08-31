# In your_app/doctype/almarine_shipment_request/almarine_shipment_request.py

import frappe
from frappe import _
from frappe.model.document import Document

class AlmarineShipmentRequest(Document):
     def on_update(self):
        if self.shipment_request_status == "مقبولة":  # Or any other status that triggers shipment creation
            self.create_shipment()
     def create_shipment(self):
        shipment = frappe.new_doc("Almarine Shipment")
        # Populate shipment fields from the shipment request
        shipment.update({
            "customer_name": self.name,
            "shpper_name": self.shipper_name,
            "رقم_هاتف_الشاحن": self.shipper_phone,
            "اسم_المستلم": self.revicer_name,
            "رقم_هاتف_المستلم": self.reciver_phone,
            "pickup_time": self.shipment_pickup_time,
            "pickup_country": self.pickup_country,
            "pickup_city": self.pickup_city,
            "shipment_type": self.shipment_type,
            "دولة_التوصيل": self.deliver_country,
            "مدينة_التوصيل": self.delivery_city,
            "payload_type": self.type_of_shipment,
            "payload_name": self.name_of_shipment,
            "payload_state": self.state_of_shipment,
            "payload_weight": self.weight_of_shipment,
            "packing_type": self.packing_type,
            "payload_image": self.image_of_shipment,
            "offered_price": self.offered_price,
            "currency_type": self.type_of_currency,
            "tax": self.tax,
            "full_price": self.full_price,
            "way_of_payment": self.way_of_payment,
            "shipment_status": "جاري التوصيل"  # Set initial shipment status
        })
        shipment.insert()

        # Trigger driver assignment logic here (if applicable)
        # ...

        frappe.msgprint(_("Shipment created successfully!"))
