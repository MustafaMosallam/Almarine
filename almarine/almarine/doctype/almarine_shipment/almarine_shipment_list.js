frappe.listview_settings['Almarine Shipment'] = {
    onload: function(listview) {
        // Apply filter only if the user is a truck owner
        if (frappe.user_roles.includes("Almarine Truck Owner")) {
            // Fetch the truck owned by the current user
            frappe.call({
                method: "almarine.almarine.doctype.almarine_shipment.almarine_shipment.get_truck_for_owner", 
                callback: function(r) {
                    if (r.message) {
                        var truck_name = r.message; 

                        // Apply the filter but allow manual removal
                        listview.filter_area.add(
                            ["Almarine Shipment", "truck", "=", truck_name], 
                            "My Truck's Shipments" 
                        );

                        listview.refresh(); 
                    } else {
                        frappe.msgprint(__("You don't own any trucks. Please register a truck first.")); 
                    }
                }
            });
        }
    },onload: function(listview) {
        // ... (your existing code to fetch the truck and apply the initial filter)

        // Add an event listener to handle filter changes
        listview.filter_area.on('filter_change', function() {
            // Check if the user is a truck owner
            if (frappe.user_roles.includes("Almarine Truck Owner")) {
                // Check if the forced filter is still present
                let forcedFilterExists = listview.filter_area.filter_list.get_filters().some(filter => {
                    return filter[1] === "truck" && filter[2] === "=" && filter[3] === truck_name;
                });

                if (!forcedFilterExists) {
                    // If the forced filter is removed, reapply it
                    listview.filter_area.add(
                        ["Almarine Shipment", "truck_owner", "=", truck_name],
                        "My Truck's Shipments"
                    );

                    frappe.show_alert(__("This filter cannot be removed."));
                }
            }
        });
    }
};