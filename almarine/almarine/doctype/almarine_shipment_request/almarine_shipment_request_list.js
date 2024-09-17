frappe.listview_settings['Almarine Shipment Request'] = {
    onload: function(listview) {
        // Fetch the customer linked to the current user
        frappe.call({
            method: "almarine.almarine.doctype.almarine_shipment_request.almarine_shipment_request.get_customer_for_user",
            args: {},
            callback: function(r) {
                if (r.message) {
                    var customer_name = r.message; 

                    // Apply the filter but allow manual removal
                    listview.filter_area.add(
                        ["Almarine Shipment Request", "customer_link", "=", customer_name],
                        "جميع الشحنات المطلوبة" 
                    );

                    listview.refresh(); 

                    // Add an event listener to handle filter changes
                    listview.filter_area.on('filter_change', function() {
                        // Check if the forced filter is still present
                        let forcedFilterExists = listview.filter_area.filter_list.get_filters().some(filter => {
                            return filter[1] === "customer_link" && filter[2] === "=" && filter[3] === customer_name;
                        });

                        if (!forcedFilterExists) {
                            // If the forced filter is removed, reapply it
                            listview.filter_area.add(
                                ["Almarine Shipment Request", "customer_link", "=", customer_name],
                                "جميع الشحنات المطلوبة"
                            );

                            frappe.show_alert(__("This filter cannot be removed."));
                        }
                    });

                } else {
                    frappe.msgprint("Error fetching customer information. Please log in again.");
                }
            }
        });
    }
};