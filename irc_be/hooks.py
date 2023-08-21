from . import __version__ as app_version

app_name = "irc_be"
app_title = "IRC Business Essentials"
app_publisher = "IRC Business Essentials"
app_description = "customisation"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "ircengg@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/irc_be/css/irc_be.css"
# app_include_js = "/assets/irc_be/js/irc_be.js"

# include js, css files in header of web template
# web_include_css = "/assets/irc_be/css/irc_be.css"
# web_include_js = "/assets/irc_be/js/irc_be.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "irc_be/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Project" : "public/js/project.js",
              "Leave Application" : "public/js/leave_application.js",
              "Sales Order" : "public/js/sales_order.js",
              "Payroll Entry" : "public/js/payroll_entry.js",
              "Task" : "public/js/task.js",
              "Salary Slip" : "public/js/salary_slip.js",
              "Expense Claim" : "public/js/expense_claim.js",
              "Employee" : "public/js/employee.js",
              "Attendance" : "public/js/attendance.js",
              "Attendance Request" : "public/js/attendance_request.js",
              "Employee Advance" : "public/js/employee_advance.js"
              }
doctype_list_js = {"Attendance" : "public/js/attendance_list.js",
                   "Employee" : "public/js/employee_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# InstallationS
# ------------

# before_install = "irc_be.install.before_install"
# after_install = "irc_be.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "irc_be.uninstall.before_uninstall"
# after_uninstall = "irc_be.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "irc_be.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

permission_query_conditions = {
	"Task": "irc_be.permissions.task.update_task_conditions",
    "Project": "irc_be.permissions.project.project_user_conditions"
}


# permission_query_conditions = {
# 	"Task": "irc_be.irc_be.custom_py.task.update_task_conditions",
#     "Project": "irc_be.irc_be.custom_py.project.get_user_conditions"
# }

# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }
override_doctype_class = {
	"Asset Movement": "irc_be.irc_be.custom_py.asset_movement.transfer_asset_movement"
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }
doc_events = {
	"Leave Allocation": {
		"on_update": "irc_be.irc_be.custom_py.leave_allocation.leave_allocation"
	},
	"Attendance": {
		"before_submit": "irc_be.irc_be.custom_py.attendance.attendance_leave"
	},
    "Task": {
		"on_update": "irc_be.irc_be.custom_py.task.task_assignment",
        "after_insert": "irc_be.irc_be.custom_py.task.task_before_after_days",
	},
    "Project": {
		"on_update": "irc_be.irc_be.custom_py.project.task_dependency"
	},
	"Sales Order": {
		"on_update": "irc_be.irc_be.custom_py.sales_order.sales_order"
	}
}


# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"irc_be.tasks.all"
#	],
#	"daily": [
#		"irc_be.tasks.daily"
#	],
#	"hourly": [
#		"irc_be.tasks.hourly"
#	],
#	"weekly": [
#		"irc_be.tasks.weekly"
#	]
#	"monthly": [
#		"irc_be.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "irc_be.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "irc_be.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "irc_be.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Request Events
# ----------------
# before_request = ["irc_be.utils.before_request"]
# after_request = ["irc_be.utils.after_request"]

# Job Events
# ----------
# before_job = ["irc_be.utils.before_job"]
# after_job = ["irc_be.utils.after_job"]

# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"irc_be.auth.validate"
# ]

