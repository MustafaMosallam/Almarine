frappe.ready(function() {
	frappe.web_form.validate = () => {
        let data = frappe.web_form.get_values();

        // First Name and Last Name Validation
        if (!data.customer_firstname || data.customer_firstname.trim() === "") {
            frappe.msgprint("Please enter your first name.");
            return false;
        }
        if (!data.customer_lastname || data.customer_lastname.trim() === "") {
            frappe.msgprint("Please enter your last name.");
            return false;
        }

        // Email Validation
        var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!data.customer_email || !emailRegex.test(data.customer_email)) {
            frappe.msgprint("Please enter a valid email address.");
            return false;
        }

        // Phone Number Validation 
        // You'll likely need to customize this regex based on your expected phone number format
        var phoneRegex = /^\d{10,15}$/; 
        if (!data.customer_phone_number || !phoneRegex.test(data.customer_phone_number)) {
            frappe.msgprint("Please enter a valid phone number.");
            return false;
        }

        // Country Validation
        if (!data.customer_country) {
            frappe.msgprint("Please select your country.");
            return false;
        }

        // You can add further validation for other fields as needed
    };
})