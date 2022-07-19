# Copyright (c) 2013, Bestway and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import getdate, cstr, flt, fmt_money

def execute(filters=None):
	conditions,filters = get_conditions(filters)
	columns = get_columns(filters)
	data = get_data(conditions,filters)

	return columns,data

def get_data(conditions,filters):
        
		
		item = frappe.db.sql(""" 
		SELECT employee,employee_name,st_hours,SUM(total_working_hours) as total,SUM(total_working_hours) - 40 as OT_Time

		FROM `tabEmployee Checkin` Where time between %(from_date)s and %(to_date)s

		GROUP BY employee_name

		HAVING SUM(total_working_hours) >= 40


		{conditions}
 		""".format(conditions=conditions), filters, as_dict=1)
		
		return item


def get_conditions(filters):
	conditions = ""
	# if filters.get("employee"): conditions += " and employee = %(employee)s"
	if filters.get("time"): conditions += " and time >= %(from_date)s"
	if filters.get("out_time"): conditions += " and time > %(to_date)s"
	
	return conditions,filters   
   
def get_columns(filters):

	return  [
		
		{
			"label": ("Employee"),
			"fieldname": "employee",
			"fieldtype": "Link",
			"options": "Employee",
			"width": 200
		},
		{
			"label": ("Employee Name"),
			"fieldname": "employee_name",
			"width": 200
		},
		{
			"label": ("Standarad Hours"),
			"fieldname": "st_hours",
			"width": 150
		},
		{
			"label": ("Over Time Hours"),
			"fieldname": "OT_Time",
			"width": 180
		},
		{
			"label": ("Total Working Hours"),
			"fieldname": "total",
			"width": 180
		},
		
        
        ]

