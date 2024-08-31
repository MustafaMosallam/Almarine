# Copyright (c) 2024, Mosalam Company and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document


class AlmarineCustomer(Document):
    def after_insert(self):
        # ... (any other post-registration actions you might have)

        # Create a new User record
        user = frappe.new_doc("User")
        user.email = self.customer_email 
        user.first_name = self.customer_firstname + ' ' + self.customer_lastname
        # Set other User fields as needed (e.g., password)
        user.password = frappe.utils.password.encrypt('your_default_password') 

        # Assign the "Almarine Customer" role
        user.append("roles", {
            "doctype": "Has Role",
            "role": "Almarine Customer" 
        })

        user.insert()

        # Link the Almarine Customer to the newly created User
        self.user = user.name
        self.save()

        # ... (rest of the after_insert method)
    def get_customer_for_user(self):
        if frappe.session and frappe.session.user:
            customer = frappe.db.get_value("Almarine Customer", {"user": frappe.session.user}, "name")
            if customer:
                return customer
        return None
   