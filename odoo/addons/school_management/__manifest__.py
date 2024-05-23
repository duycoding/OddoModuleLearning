{
    'name': 'School',
    'version': '1.0',
    'summary': 'Đây là sự sửa đổi đầu',
    'description': 'Mô tả chi tiết hơn về module của bạn',
    'author': 'Tên của bạn',
    'website': 'Website của bạn',
    'category': 'Uncategorized',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/my_model_view.xml',
        'data/models_data.xml',
        'data/school_student_data.xml',
        'views/school_student_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',  # Adding the license key
}
