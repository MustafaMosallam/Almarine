frappe.ready(function() {
    // ... your other web form logic

    frappe.web_form.after_load = () => {
        // Check if a user is logged in
        if (frappe.session && frappe.session.user) {
            // Fetch the customer linked to the user
            frappe.call({
                method: "almarine.almarine.doctype.almarine_customer.almarine_customer.get_customer_for_user",
                args: {}, // No arguments needed in this case
                callback: function(r) {
                    if (r.message) {
                        // Set the customer_link field to the fetched customer name
                        frappe.web_form.set_value("customer_link", r.message);
                    } else {
                        frappe.msgprint("Error fetching customer information. Please log in again.");
                    }
                }
            });
        } else {
            frappe.msgprint("You need to be logged in to create a shipment request.");
            // Optionally, you can redirect the user to the login page here.
        }
    };

    // ... your validation logic
});