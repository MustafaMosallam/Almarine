import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils.password import update_password 

class AlmarineCustomer(Document):
    def after_insert(self):
        """Handles user creation and password setting after customer registration."""
        try:
            # Check if a user with this email already exists
            existing_user = frappe.get_doc("User", {"email": self.customer_email})
            if existing_user:
                frappe.throw(_("A user with this email address already exists. Please use a different email or log in."))

            # Create the user (since no existing user was found)
            user = frappe.new_doc("User")
            user.email = self.customer_email
            user.first_name = self.customer_firstname 
            user.last_name = self.customer_lastname
            # ... (set other User fields as needed)
            user.add_roles("Almarine Customer")
            user.insert()

            # Set the password if provided 
            if self.new_password:
                update_password(user=user.name, pwd=self.new_password)  
                self.db_set("new_password", "")  

            # Link the Almarine Customer to the User
            self.user = user.name
            self.save()

            frappe.msgprint(_("Customer and user created successfully!"))
        except Exception as e:
            frappe.throw(_("Error during customer registration: {}").format(e))

    def get_customer_for_user(self):
        if frappe.session and frappe.session.user:
            customer = frappe.db.get_value("Almarine Customer", {"user": frappe.session.user}, "name")
            if customer:
                return customer
        return None