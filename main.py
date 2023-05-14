from flask import Flask
from flask_restx import Api
from app.config import Config
from app.database import db
from app.models import Book, Author
from app.views.authors import author_ns
from app.views.books import book_ns


def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    # sets configuration via the from_object() method
    application.config.from_object(config)
    # applies configuration set before via the app_context() push() methods
    application.app_context().push()
    return application


def configure_app(application):
    db.init_app(application)  # <db = SQLAlchemy(app)> equivalent, via the init_app() method
    api = Api(app)
    api.add_namespace(book_ns)
    api.add_namespace(author_ns)


def load_data():
    b1 = Book(id=1, name="Harry Potter", year=2000)
    b2 = Book(id=2, name="Le Conte De Monte-Cristo", year=1844)
    a1 = Author(id=1, first_name="Joan", last_name="Rowling")
    a2 = Author(id=2, first_name="Alexandre", last_name="Dumas")

    with app.app_context():
        db.drop_all()
        db.create_all()

        with db.session.begin():
            db.session.add_all([b1, b2])
            db.session.add_all([a1, a2])


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    configure_app(app)
    load_data()
    app.run()
