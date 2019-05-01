from mongoengine import connect


def init_db(app):
    db_name = app.config.get("DB_NAME")
    db_uri = app.config.get("GRAPHQL_DATABASE_URI")
    connect(db_name, host="mongodb://localhost:27017/" + db_uri, alias="default")
