class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'daniel'
    MYSQL_PASSWORD = 'root'
    MYSQL_DB = 'api_utl'
    
    config={
        'development':DevelopmentConfig
    }