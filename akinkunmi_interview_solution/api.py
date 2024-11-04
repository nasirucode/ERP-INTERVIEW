import frappe
from frappe import _


@frappe.whitelist(allow_guest = True)
def customer_api():
    data = frappe.request.json
    customer = frappe.get_doc({'doctype': 'Customer API'})
    try:
        if frappe.request.method == 'POST':
            customer.update(data)
            customer.insert()
            frappe.db.commit()
            return customer
        elif frappe.request.method == 'PUT':
            customer_exist = frappe.db.exists("Customer API", data['mobile_number'])
            if(customer_exist):
                frappe.db.set_value('Customer API', data['mobile_number'], data)
                frappe.db.commit()
                return "Customer Successfully Updated"
            else:
                frappe.throw('Customner does not exist')
        else:
            frappe.throw('Unsupport Request')
    except Exception as e:
        if isinstance(e, frappe.ValidationError):
            return {'error_code': 400, 'message': str(e)}
        return {'error_code': 500, 'message': "Internal Server Error"}
