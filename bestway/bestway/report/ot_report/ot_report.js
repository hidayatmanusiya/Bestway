// Copyright (c) 2016, Bestway and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["OT Report"] = {
    "filters": [{
            "fieldname": "from_date",
            "label": __("In Date From"),
            "fieldtype": "Date",
            "default": frappe.datetime.month_start(),
        },
        {
            "fieldname": "to_date",
            "label": __("To"),
            "fieldtype": "Date",
            "default": frappe.datetime.month_end(),
        }

    ]
};