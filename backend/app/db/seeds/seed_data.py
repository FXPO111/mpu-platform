from sqlalchemy.orm import Session

from app.domain.models import Product, Question, Rubric, Topic


def seed_questions(db: Session):
    topic = Topic(slug="alcohol", title_de="Alkohol", title_en="Alcohol")
    db.add(topic)
    db.flush()
    db.add(Question(topic_id=topic.id, level=2, question_de="Was hat sich seit dem Vorfall verändert?", question_en="What changed after the incident?", intent="behavioral change", tags=["change", "responsibility"]))


def seed_rubrics(db: Session):
    db.add_all([
        Rubric(code="clarity", title_de="Klarheit", title_en="Clarity", description="Clear narrative"),
        Rubric(code="responsibility", title_de="Verantwortung", title_en="Responsibility", description="Owns responsibility"),
    ])


def seed_products(db: Session):
    db.add_all([
        Product(code="AI_PACK_50", type="ai_pack", name_de="AI 50", name_en="AI 50", price_cents=4900, currency="EUR", metadata_json={"credits": 50}),
        Product(code="CALL_60", type="booking", name_de="Beratung 60", name_en="Consultation 60", price_cents=9900, currency="EUR", metadata_json={}),
    ])
