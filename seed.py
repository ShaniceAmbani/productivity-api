from faker import Faker

from app import app
from models.dbconfig import db
from models.user import User
from models.note import Note

fake = Faker()

with app.app_context():
    print("Clearing database...")

    Note.query.delete()
    User.query.delete()

    db.session.commit()

    print("Creating users...")

    users = []

    for i in range(5):
        user = User(
            username=f"user{i+1}",
            email=f"user{i+1}@example.com"
        )
        user.password = "password123"

        db.session.add(user)
        users.append(user)

    db.session.commit()

    print("Creating notes...")

    for user in users:
        for _ in range(3):
            note = Note(
                title=fake.sentence(nb_words=4),
                content=fake.paragraph(nb_sentences=3),
                user_id=user.id
            )

            db.session.add(note)

    db.session.commit()

    print("Database seeded successfully!")