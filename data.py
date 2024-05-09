from models import User, date

db_users = [
    User(id=1, username="Вадим", wallet=10.0, birthdate=date(1990, 1, 1)),
    User(id=2, username="Eric", wallet=200.0, birthdate=date(1982, 5, 15)),
    User(id=3, username="Gera", wallet=50.0, birthdate=date(1995, 6, 12)),
    User(id=4, username="Kurt", wallet=2000.0, birthdate=date(1975, 2, 17)),
    User(id=5, username="Simon", wallet=30000.0, birthdate=date(1989, 12, 22)),
]
