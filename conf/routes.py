
urls = (
    '/', 'index',
    '/addUser', 'addUser',
    '/login', 'Login',
    '/(js|css|fonts)/(.*)', 'static',
    '/images/(.*)','ImageDisplay',
    '/logout', 'Reset'
    )