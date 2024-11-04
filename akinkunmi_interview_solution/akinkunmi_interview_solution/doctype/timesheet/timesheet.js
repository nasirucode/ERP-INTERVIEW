// Copyright (c) 2024, nasirucode and contributors
// For license information, please see license.txt

frappe.ui.form.on("Timesheet", {
	refresh(frm) {
        let has_role = has_common(frappe.user_roles, ["Timesheet Manager"])

        if(has_role){
            frm.set_df_property('status', 'read_only', 0)
        }
        
	},
});
