frappe.listview_settings['Almarine Shipment Request'] = {
    // Set default filters to show only the current user's requests
    filters: [
        ['customer_link', '=', frappe.session.user] // Assuming 'customer_link' is linked to the User doctype
    ],

    onload: function(listview) {
        // You can add any additional onload logic here if needed
    }
};