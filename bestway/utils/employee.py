import frappe


@frappe.whitelist()
def fetch_data(employee):
  items = []	
  scrapitems = frappe.db.sql("select standard_hours,pay_rate_amount from `tabEmployee` where name = %s", employee)
  for item in scrapitems:
    # if (item.enable == 1):
      items.append(item[0])
  return items

# @frappe.whitelist()
# def fetch_rate(customer,item_code):
    
#     scrapitems = frappe.db.sql("select special_mrp from `tabBrand child 1` where customer = %s AND item_code = %s AND enable = 1", (customer,item_code),as_dict=True)
#     return scrapitems



# @frappe.whitelist()
# def fetch_price(customer):
#    	frappe.db.sql("""update `tabBrand child 1` set price_list_rate = (price_list_rate + (price_list_rate * 10 ) / 100) where customer = %s """, customer)    
  
