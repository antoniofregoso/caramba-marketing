# -*- coding: utf-8 -*-
{
    'name': "RH Mac Adrress reader",

    'summary': "Attendance control when connecting and disconnecting from the network.",

    'description': """
        Control of assistance through the connection to the res of the employee's cell phone. When you connect for the first time in the day you check-in, at the end of the work schedule you check-out.
    """,

    'author': "Antonio Fregoso",
    'website': "http://www.yourcompany.com",

  
    'category': 'Human Resources',
    'version': '12.0.0.0.0',

    
    'depends': ['hr_attendance'],

   
    'data': [
        # 'security/ir.model.access.csv',
        'views/hr_employee_view.xml'
    ],
   
}