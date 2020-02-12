from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
      {
        "label":_("Setup"),
        "icon": "octicon octicon-file-directory",
        "items": [
            {
              "type": "doctype",
              "name": "Scheduled Tax",
              "onboard": 1,
              "label": _("Scheduled Tax"),
              "description": _("Articles which members issue and return."),
            },
            # {
            #   "type": "doctype",
            #   "name": "To Do Exception",
              
            #   "label": _("To Do (Exception) Table for Payroll"),
            #   "description": _("Articles which members issue and return."),
            # },
          ]
      }
  ]
