import frappe
from frappe import _  # Import the translation function
from frappe.model.document import Document

class AlmarineShipment(Document):
    # ... (your existing code)

    @frappe.whitelist()
    def accept_shipment(self):
        """Handles a truck owner accepting a shipment."""

        truck_owner = frappe.session.user

        # Check if the user has the 'Almarine Truck Owner' role
        if not frappe.db.exists(
            "Has Role", {"parent": truck_owner, "role": "Almarine Truck Owner"}
        ):
            frappe.throw(_("Only truck owners can accept shipments."))

        # Check if the shipment is already accepted
        if self.truck:
            frappe.throw(_("This shipment has already been accepted."))

        # Assign the truck owned by the user to the shipment
        truck = self.get_truck_for_owner(truck_owner)
        if not truck:
            frappe.throw(_("You don't own any trucks. Please register a truck first."))
        self.truck = truck

        # Update the shipment status (optional)
        # self.shipment_status = "Accepted" 

        self.save()

        # Send notification to the customer 
        # self.notify_customer(truck_owner)

        return {"message": _("Shipment accepted successfully!")}
    @frappe.whitelist()
    def get_truck_for_owner(self, truck_owner):
        """Gets the truck owned by the given user."""
        # Assuming there's a one-to-one relationship between user and truck
        truck = frappe.get_list("Almarine Truck", filters={"user": truck_owner}, limit=1)
        return truck[0].name if truck else None
     
    

    # ... (your existing notify_customer method)