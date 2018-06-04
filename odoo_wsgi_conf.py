import odoo

odoo.multi_process = True 
odoo.conf.server_wide_modules = ['web']

conf = odoo.tools.config

conf['log_level'] = 40

conf['addons_path'] = '/opt/odoo/11/addons, /opt/odoo/addons'

conf['static_http_document_root'] = '/opt/odoo/11/odoo-bin'

conf['db_name'] = ''

conf['db_host'] = 'localhost'

conf['db_user'] = 'eklavya'

conf['db_port'] = 5432

conf['db_password'] = '123'

conf['admin_passwd'] = 'admin'

application = odoo.service.wsgi_server.application

odoo.service.server.load_server_wide_modules()

bind = '0.0.0.0:8069'

pidfile = '.gunicorn.pid'

workers = 5

threads = 5

timeout = 120

max_requests = 1000

proxy_mode = True
