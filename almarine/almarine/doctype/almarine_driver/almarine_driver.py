# Copyright (c) 2024, Mosalam Company and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document
import frappe.utils
import frappe.utils.password


class AlmarineDriver(Document):
	def after_insert(self):
		user = frappe.new_doc("User")
		user.first_name = self.driver_fullname
		user.email = self.driver_email # Assuming email is used as the username
        # Set other User fields as needed (e.g., password)
		user.password = frappe.utils.password.encrypt("123")
        # Assign the "Almarine Driver" role
		user.append("roles", {
            "doctype": "Has Role",
            "role": "Almarine Driver"  # Make sure this role exists in your system
        })
		user.insert()
        # Link the Almarine Driver to the newly created User
		self.user = user.name
		self.save()
		#linking the truck
		for truck in self.driver_trucks: 
			truck.truck_driver = self.name
		self.save()
        # ... (rest of the after_insert method)
	def create_trucks_on_submit(doc, vehicles):
		for vehicle_data in vehicles:
			if not vehicle_data.truck_license_plate:  # Basic validation, adjust as needed
				frappe.throw(_("License Plate Number is required for all trucks."))

			truck = frappe.new_doc("Almarine Vehicle") 
			truck.truck_type = vehicle_data.truck_type
			truck.truck_license_plate = vehicle_data.truck_license_plate
			truck.truck_trailer_number = vehicle_data.truck_trailer_number
			# Set other truck fields as needed based on your child table structure

			truck.truck_driver = doc.name  # Link the truck to the driver
			truck.insert()

		return {"message": "Driver profile and trucks created successfully!"}
