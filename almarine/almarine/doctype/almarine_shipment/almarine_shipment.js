// Copyright (c) 2024, Mosalam Company and contributors
// For license information, please see license.txt

frappe.ui.form.on("Almarine Shipment", {
        refresh(frm) {
            frm.get_field("accept_shipment").$wrapper.on("click", function() {
                console.log();
                frm.call("accept_shipment").then(r => {
                    if (r.message) {
                        frappe.show_alert(r.message);
                        frm.refresh(); 
                    }
                });
            });
            // Make all fields read-only except the button for truck owners
            if (frappe.user_roles.includes("Almarine Truck Owner")) {
                frm.fields.forEach(field => {
                    if (field.df.fieldname !== "accept_shipment") { 
                        frm.set_df_property(field.df.fieldname, "read_only", 1);
                        if (field.df.fieldtype === "Link" || field.df.fieldtype === "Dynamic Link") {
                            field.$wrapper.find('.control-value a').removeAttr('href');
                        }
                    }
                });
            }
        }
});
