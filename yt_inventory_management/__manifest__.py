{
    'name': 'Construction Inventory Management',
    'version': '1.0',
    'summary': 'Quản lý tồn kho cho công trường xây dựng',
    'author': 'Yeyetha',
    'category': 'Inventory',
    'depends': ['stock', 'purchase', 'project', 'account'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        
        'views/inventory_dashboard_view.xml',
        'views/material_request_view.xml',
        'views/transfer_approval_view.xml',
        'views/budget_control_panel.xml',
        'views/reports_dashboard_view.xml',
        'views/product_views.xml',

        'views/inventory_menu.xml',
    ],
    'installable': True,
    'application': True,
}