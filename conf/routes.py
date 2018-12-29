
urls = (
    '/', 'index',
    '/addUser', 'addUser',
    '/users', 'Users',
    '/signin', 'Login',
    '/del_user/(.*)', 'DeleteUser',
    '/lock_user/(.*)', 'LockUser',
    '/unlock_user/(.*)', 'UnlockUser',
    '/edit_user/(.*)', 'EditUser',
    '/edit_user', 'UpdateUser',
    '/(js|css|fonts)/(.*)', 'static',
    '/images/(.*)','ImageDisplay',
    '/logout', 'Reset',
    '/admin', 'Admin',
    '/add_app', 'AddApp',
    '/apps', 'Apps',
    '/del_app/(.*)', 'DeleteApp',
    '/activate_app/(.*)', 'ActivateApp',
    '/deactivate_app/(.*)', 'DeactivateApp',
    '/edit_app/(.*)', 'EditApp',
    '/edit_app', 'UpdateApp'
    )

admin_urls = [
    '/admin',
    '/users',
    '/edit_user',
    '/del_user',
    '/lock_user',
    '/unlock_user',
    '/apps',
    '/add_app',
    '/edit_app',
    '/del_app',
    '/activate_app',
    '/deactivate_app'
    ]