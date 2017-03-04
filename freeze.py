from flask_frozen import Freezer
from app import app, get_csv
freezer = Freezer(app)

@freezer.register_generator			# This is needed to "freeze" every details page, not just index.html
def detail():
    for row in get_csv():
        yield {'row_id': row['id']}

if __name__ == '__main__':
    freezer.freeze()