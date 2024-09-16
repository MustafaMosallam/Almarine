import frappe
from frappe.model.document import Document
from frappe.utils import random_string

class AlmarineTruck(Document):
    # ... other methods
	# def validate(self):
    # ... (your existing truck validation logic)
		# if frappe.session and frappe.session.user:
      	# 	# Check if the current user already owns a truck
		# 	existing_truck = frappe.db.exists("Almarine Truck", {"user": frappe.session.user})
		# 	if existing_truck:
		# 		frappe.throw(_("You can only own one truck."))

		# 	# ... (rest of your validation logic, including driver creation/linking)

	def after_insert(self):
        # Create a new User for the truck owner
		user = frappe.new_doc("User")
		user.email = self.truck_owner_email  # Use truck plate number as username
		user.first_name = self.truck_plate_number 

        # Generate a random password & send a welcome email
        # password = random_string(10)
        # user.password = frappe.utils.password.encrypt(password)
        # user.send_welcome_email = 1

        # Assign the "Truck Owner" role
		user.append("roles", {
            "doctype": "Has Role",
            "role": "Almarine Truck Owner" 
        })

		user.insert()

        # Link the truck to the newly created User
		self.user = user.name
		self.save()

        # Send the welcome email
        # You'll need to decide where to send this email. 
        # You could add a field in the Almarine Truck doctype to capture an email address
        # For now, let's assume there's a 'contact_email' field
        # frappe.sendmail(
        #     recipients=[self.contact_email], 
        #     subject="Welcome to Almarine!",
        #     message=f"Your Almarine account has been created.\nYour username is your truck's license plate: {self.truck_palte_number}.\nYour temporary password is: {password}.\nPlease change it after logging in.",
        # )