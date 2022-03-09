from mongoengine import connect


#The connexion to database
def get_connexion():
    connect(db="ingeniance",host="localhost",port=27017)

