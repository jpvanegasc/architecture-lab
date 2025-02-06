from app.articles.models import Tag
from app.db import DatabaseSession


def get_or_create_tags(db: DatabaseSession, tag_list: list[str]) -> list[Tag]:
    existing_tags = db.query(Tag).filter(Tag.tag.in_(tag_list)).all()
    if create_tags := (set(tag_list) - set(tag.tag for tag in existing_tags)):
        new_tags = [Tag(tag=tag) for tag in create_tags]
        db.add_all(new_tags)
        db.commit()
        return existing_tags + new_tags

    return existing_tags
