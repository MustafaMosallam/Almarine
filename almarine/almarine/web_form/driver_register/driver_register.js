// In your webform_name.js file
frappe.ready(function() {

    frappe.web_form.validate = () => {
        let data = frappe.web_form.get_values();

        // Full Name Validation
        if (!data.driver_fullname || data.driver_fullname.trim() === "") {
            frappe.msgprint("Please enter your full name.");
            return false; // Prevent form submission
        }

        // Email Validation
        var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!data.driver_email || !emailRegex.test(data.driver_email)) {
            frappe.msgprint("Please enter a valid email address.");
            return false;
        }

        // Phone Number Validation (basic)
        var phoneRegex = /^\d{10,15}$/; // Adjust based on your phone number format
        if (!data.driver_phone || !phoneRegex.test(data.driver_phone)) {
            frappe.msgprint("Please enter a valid phone number.");
            return false;
        }

        // Country Validation (ensure a value is selected)
        if (!data.driver_country) {
            frappe.msgprint("Please select your country.");
            return false;
        }

        // Driver License and Passport Validation (check if files are attached)
        // Note: File attachment validation might require additional logic depending on your implementation
        if (!data.driver_license) {
            frappe.msgprint("Please attach your driver's license.");
            return false;
        }

        if (!data.driver_passport) {
            frappe.msgprint("Please attach your passport.");
            return false;
        }

        // Child Table (Almarine Trucks) Validation - Ensure at least one truck is added
        if (data.driver_trucks.length === 0) {
            frappe.msgprint("Please add at least one truck.");
            return false;
        } else {
            // You can add further validation for individual truck fields here if needed
        }
    }


    frappe.ui.form.on('Almarine Driver', { 
        after_save: function(frm) { 
            frappe.call({
                // Call the server-side Python function to process the truck data
                method: 'almarine.almarine.doctype.almarine_driver.almarine_driver.create_trucks_on_submit', 
                args: {
                    doc: frm.doc,
                    vehicles: frm.doc.driver_trucks 
                },
                callback: function(r) {
                    if (r.message) {
                        frappe.msgprint(r.message); 
                    } else {
                        frappe.msgprint("An error occurred while creating trucks."); 
                    }
                }
            });}
        
    
    });

    // Automatically link new trucks to the driver
    frappe.ui.form.on('Almarine Trucks', { 
        before_insert: function(frm, cdt, cdn) {
            var row = locals[cdt][cdn];
            row.truck_driver = frm.doc.name; 
        }
    });

});

