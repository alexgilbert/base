
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
    '/admin', 'Admin'
    )

admin_urls = [
    '/admin',
    '/users',
    '/edit_user',
    '/del_user',
    '/lock_user',
    '/unlock_user'
    ]