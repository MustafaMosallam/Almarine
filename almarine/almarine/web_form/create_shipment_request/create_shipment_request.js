frappe.ready(function() {
    frappe.web_form.after_load = () => {
        // Automatically set the customer_link field based on the logged-in user
        if (frappe.session && frappe.session.user) {
            frappe.call({
                method: "almarine.almarine.doctype.almarine_customer.almarine_customer.get_customer_for_user",
                args: {},
                callback: function(r) {
                    if (r.message) {
                        frappe.web_form.set_value("customer_link", r.message);
                    } else {
                        frappe.msgprint("Error fetching customer information. Please log in again.");
                    }
                }
            });
        } else {
            frappe.msgprint("You need to be logged in to create a shipment request.");
            // Optionally, redirect to the login page.
        }
    };

    // Add your validation logic here using frappe.web_form.validate
    // ... 
});