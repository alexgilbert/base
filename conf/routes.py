
urls = (
    '/', 'index',
    '/addUser', 'addUser',
    '/users', 'Users',
    '/signin', 'Login',
    '/del_user/(.*)', 'DeleteUser',
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
    '/edit_user'
    ]