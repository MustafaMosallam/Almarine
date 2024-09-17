// Copyright (c) 2024, Mosalam Company and contributors
// For license information, please see license.txt

frappe.ui.form.on("Almarine Shipment Request", {
	refresh(frm) {

	},
    onload: function(frm) {
        // Check user role and set field properties accordingly
        if (frappe.user.has_role("Almarine Customer")) {
            console.log(frappe.user);
            // Make specific fields read-only for customers
            frm.set_df_property("customer_link", "read_only", 1); 
            frm.set_df_property("shipment_request_status", "read_only", 1);
            // ... add other fields as needed
        }
    }
});


