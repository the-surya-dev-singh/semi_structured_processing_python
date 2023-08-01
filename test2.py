import pandas as pd
from pandas import json_normalize

# Your JSON data
data = [
    {
        'id': '001',
        'company': 'XYZ pvt ltd',
        'location': 'London',
        'info': {
            'president': 'Rakesh Kapoor',
            'contacts': {
                    'email': 'contact@xyz.com',
                    'tel': '9876543210'
            }
        }
    },
    {
        'id': '002',
        'company': 'PQR Associates',
        'location': 'Abu Dhabi',
        'info': {
            'president': 'Neelam Subramaniyam',
            'contacts': {
                    'email': 'contact@pqr.com',
                    'tel': '8876443210'
            }
        }
    }
]
data=json_normalize(data,sep="_")
data=data.rename(columns={
    'info_president':'president_name',
    'info_contacts_email':'email','info_contacts_tel':'mobile'
}
)
print(data)
