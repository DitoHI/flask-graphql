from mongoengine import connect


def init_db(app):
    db_name = app.config.get("DB_NAME")
    db_uri = app.config.get("GRAPHQL_DATABASE_URI")
    db_url = db_uri + "/" + db_name

    connect(host=db_url, alias="default")
