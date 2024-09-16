# In your_app/doctype/almarine_shipment_request/almarine_shipment_request.py

import frappe
from frappe import _
from frappe.model.document import Document

class AlmarineShipmentRequest(Document):
    def validate(self):
        # ... (your existing validation logic)

        def validate(self):
    # ... (your existing validation logic)

            if frappe.session and frappe.session.user:
                # Check if the current user has the 'Almarine Customer' role
                has_customer_role = frappe.db.exists(
                    "Has Role", {"parent": frappe.session.user, "role": "Almarine Customer"}
                )

                if has_customer_role:
                    # Fetch the Almarine Customer document associated with the current user
                    customer = frappe.db.get_value("Almarine Customer", {"user": frappe.session.user}, "name")

                    if customer:
                        # Only set customer_link if it's not already set (for new requests)
                        if not self.customer_link:
                            self.customer_link = customer
                    else:
                        frappe.throw(_("No customer profile found for the current user."))

                # No restrictions for admin or dispatcher
            
    def on_update(self):
        if self.shipment_request_status == "مقبولة":  # Or any other status that triggers shipment creation
            self.create_shipment()
    def create_shipment(self):
        shipment = frappe.new_doc("Almarine Shipment")
        # Populate shipment fields from the shipment request
        shipment.update({
        "customer_name": self.name,  # ربط بطلب الشحن
        "truck_type": self.truck_type,  # استخدام الحقل من "Almarine Shipment" وليس الحقل المجلوب
        "مدينة_التوصيل": self.delivery_city,
        "دولة_التوصيل": self.deliver_country,
        "موعد_الشحنة": self.shipment_pickup_time,
        "حالة_الطلب": self.shipment_request_status,
        # ... (اي حقول اخرى من طلب الشحن تحتاجها في الشحنة)
    })
        shipment.insert()

        # Trigger driver assignment logic here (if applicable)
        # ...

        frappe.msgprint(_("Shipment created successfully!"))
