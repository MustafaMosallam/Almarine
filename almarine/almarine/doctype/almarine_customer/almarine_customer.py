import time
import frappe
from frappe.model.document import Document
from frappe.utils import random_string

class AlmarineCustomer(Document):
    # ... (other methods)

    def after_insert(self):
        # Create a new User record
        user = frappe.new_doc("User")
        user.email = self.customer_email
        user.first_name = self.customer_firstname 
        user.last_name = self.customer_lastname
        user.append('roles',{
					"doctype": "Has Role",
					"role":"Almarine Customer"
					})
        user.insert(ignore_permissions=True)
        # Link the Almarine Customer to the newly created User
        self.user = user.name
        self.save()
    @frappe.whitelist(allow_guest=True)
    def get_customer_for_user(self):
            if frappe.session and frappe.session.user:
                customer = frappe.db.get_value("Almarine Customer", {"user": frappe.session.user}, "name")
                if customer:
                    return customer
            return None