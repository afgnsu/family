# -*- coding: utf-8 -*-
{
    'name': "family (家)",  # 插件名稱
    'summary': "家庭成員",  # 插件副標題
    'description': "介吾測試",  # 插件描述
    'author': "蘇介吾",  # 作者
    'website': "http://afgn.cc",  # 網站
    'category': 'Uncategorized',  # 插件分類(未分類)
    'version': '12.0.1',  # Odoo版本(重要)
    # any module necessary for this one to work correctly
    'depends': ['base'],  # 相依模組
    # always loaded
    'data': [  # 權限、選單、視圖
        'security/ir.model.access.csv',  # 權限要放在最前面
        'views/family_parent.xml',
        'views/family_child.xml',
        'views/family_pet.xml',
        'views/family_menu.xml',  # 選單要放在最後面
    ],
    # only loaded in demonstration mode
    # 'demo': ['demo/demo.xml'],   #範例
    'test': [],
    'installable': True,  # 允許安裝
    'auto_install': True,  # 是否自動安裝
    # 'post_init_hook': 'post_init',
}
