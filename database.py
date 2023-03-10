import sqlalchemy
from sqlalchemy import create_engine, text
import os

conn_string = os.environ['DB_CONN_STRING']
engine = create_engine(conn_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


# Load the menu(ingredients, method, category name, etc) in menupage using category and recipeid.
# Here , the category is breakfast-dinner/lunch/snacks
# Recipeid is the id of the recipes in each category.
def load_menu_using_category_and_id(category, recipeid):
  with engine.connect() as conn:
    sql_stmt = f'''select * from recipes where recipeid = {recipeid} and category = "{category}"'''
    result = conn.execute(text(sql_stmt))
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]
