from sqlalchemy import create_engine, Integer, Column, String, Text, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///database/itrenddata.db", echo = False)

Base = declarative_base()

class Viewer(Base):
    __tablename__ = "viewers"
    viewer_id = Column(Integer, primary_key=True)
    viewer_name = Column(String, nullable=False, unique = True)
    viewer_email = Column(String, nullable = False, unique = True)
    viewer_password = Column(String, nullable = False)
    viewer_sex = Column(String, nullable = False)
    viewer_interests = Column(String, nullable = False)

class Topic(Base):
    __tablename__ = "topics"
    topic_id = Column(Integer, primary_key=True)
    topic_title = Column(String, nullable=False)
    topic_category = Column(String, nullable = False)
    topic_description = Column(Text, nullable = False)
    topic_media_url = Column(String)
    like_count = Column(Integer, default=0)
    dislike_count = Column(Integer, default=0)
    comment_count = Column(Integer, default=0)
    share_count = Column(Integer, default=0)
    favorite_count = Column(Integer, default=0)
    reported_count = Column(Integer, default=0)

class Comment(Base):
    __tablename__ = "comments"
    comment_id = Column(Integer, primary_key=True)
    viewer_id = Column(Integer, ForeignKey("viewers.viewer_id"))
    topic_id = Column(Integer, ForeignKey("topics.topic_id"))
    comment = Column(String)
    viewer_commenting = relationship("Viewer", backref="comments")
    topic_commented = relationship("Topic", backref="comments")
    
class Like(Base):
    __tablename__ = "likes"
    likes_id = Column(Integer, primary_key=True)
    viewer_id = Column(Integer, ForeignKey("viewers.viewer_id"))
    topic_id = Column(Integer, ForeignKey("topics.topic_id"))
    viewer_liking = relationship("Viewer", backref="likes")
    topic_liked = relationship("Topic", backref="likes")
    def __str__(self):
        return f"\n{self.viewer_liking}\n{self.topic_liked}"

class Dislike(Base):
    __tablename__ = "dislikes"
    dislikes_id = Column(Integer, primary_key=True)
    viewer_id = Column(Integer, ForeignKey("viewers.viewer_id"))
    topic_id = Column(Integer, ForeignKey("topics.topic_id"))
    viewer_disliking = relationship("Viewer", backref="dislikes")
    topic_disliked = relationship("Topic", backref="dislikes")

class Share(Base):
    __tablename__ = "shares"
    shares_id = Column(Integer, primary_key=True)
    viewer_id = Column(Integer, ForeignKey("viewers.viewer_id"))
    topic_id = Column(Integer, ForeignKey("topics.topic_id"))
    destination_link = Column(String, nullable = False)
    viewer_sharing = relationship("Viewer", backref="shares")
    topic_shared = relationship("Topic", backref="shares")

class Favorite(Base):
    __tablename__ = "favorites"
    favorites_id = Column(Integer, primary_key=True)
    viewer_id = Column(Integer, ForeignKey("viewers.viewer_id"))
    topic_id = Column(Integer, ForeignKey("topics.topic_id"))
    viewer_favoriting = relationship("Viewer", backref="favorites")
    topic_favorited = relationship("Topic", backref="favorites")
    
class Reported(Base):
    __tablename__ = "reporteds"
    reported_id = Column(Integer, primary_key=True)
    viewer_id = Column(Integer, ForeignKey("viewers.viewer_id"))
    topic_id = Column(Integer, ForeignKey("topics.topic_id"))
    viewer_reporting = relationship("Viewer", backref="report")
    topic_reported = relationship("Topic", backref="reports")

class Viewing(Base):
    __tablename__ = "viewings"
    viewing_id = Column(Integer, primary_key=True)
    viewer_id = Column(Integer, ForeignKey("viewers.viewer_id"))
    topic_id = Column(Integer, ForeignKey("topics.topic_id"))
    viewer_viewing = relationship("Viewer", backref="views")
    topic_viewed = relationship("Topic", backref="views")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def get_viewer_by_uname(username):
    return session.query(Viewer).filter_by(viewer_name = username).first()

def get_topic_by_title(title):
    return session.query(Topic).filter_by(topic_title = title).first()

def add_viewer():
    name, email = input("Name: "), input("Email: ")
    password, confirm_pass = input("Password: "), input("Confirm Password: ")
    if password != confirm_pass:
        print("Password mismatch...\n Try again...")
        return
    sex, interests = input("Sex: "), input("Topics of Interest: ")
    session.add(Viewer(viewer_name = name, viewer_email = email, viewer_password = password,
                       viewer_sex = sex, viewer_interests = interests))
    session.commit()
    print(f"{name} added successfully...")

def add_topic():
    title, category, description, media = input("Title: "), input("Category: "), input("Description: "), input("Media: ")
    session.add(Topic(topic_title = title, topic_category = category, topic_media_url = media, topic_description = description))
    session.commit()
    print("Topic added successfully...")

def like_topic():
    viewer_username = input("Enter Username: ")
    topic_title = input("Enter Topic: ")
    viewer_object = get_viewer_by_uname(viewer_username)
    topic_object = get_topic_by_title(topic_title)
    
    if viewer_object:
        session.add(Like(viewer_id = viewer_object.viewer_id, topic_id = topic_object.topic_id))
        topic = session.query(Topic).filter_by(topic_id = topic_object.topic_id).first()
        topic.like_count += 1
        session.commit()
        print("Liked successfully...")

def dislike_topic():
    viewer_username = input("Enter Username: ")
    topic_title = input("Enter Topic: ")
    viewer_object = get_viewer_by_uname(viewer_username)
    topic_object = get_topic_by_title(topic_title)
    
    if viewer_object:
        session.add(Dislike(viewer_id = viewer_object.viewer_id, topic_id = topic_object.topic_id))
        topic = session.query(Topic).filter_by(topic_id = topic_object.topic_id).first()
        topic.dislike_count += 1
        topic.like_count -= 1
        session.commit()
        print("Disliked successfully...")

def comment_on_topic():
    viewer_username = input("Enter Username: ")
    topic_title = input("Enter Topic: ")
    viewer_comment = input("Enter the comment: ")
    viewer_object = get_viewer_by_uname(viewer_username)
    topic_object = get_topic_by_title(topic_title)
    
    if viewer_object:
        session.add(Comment(viewer_id = viewer_object.viewer_id, topic_id = topic_object.topic_id, comment = viewer_comment))
        topic = session.query(Topic).filter_by(topic_id = topic_object.topic_id).first()
        topic.comment_count += 1
        session.commit()
        print("Commented successfully...")

def get_comment_by_topic_id(topic_id):
    print(session.query(Comment).filter_by(topic_id = topic_id).first().comment)

def report_topic():
    viewer_username = input("Enter Username: ")
    topic_title = input("Enter Topic: ")
    viewer_object = get_viewer_by_uname(viewer_username)
    topic_object = get_topic_by_title(topic_title)
    
    if viewer_object:
        session.add(Reported(viewer_id = viewer_object.viewer_id, topic_id = topic_object.topic_id))
        topic = session.query(Topic).filter_by(topic_id = topic_object.topic_id).first()
        topic.reported_count += 1
        session.commit()
        print("Reported successfully...")

def favorite_topic():
    viewer_username = input("Enter Username: ")
    topic_title = input("Enter Topic: ")
    viewer_object = get_viewer_by_uname(viewer_username)
    topic_object = get_topic_by_title(topic_title)
    
    if viewer_object:
        session.add(Favorite(viewer_id = viewer_object.viewer_id, topic_id = topic_object.topic_id))
        topic = session.query(Topic).filter_by(topic_id = topic_object.topic_id).first()
        topic.favorite_count += 1
        session.commit()
        print("Added to favorites successfully...")

def share_topic():
    viewer_username = input("Enter Username: ")
    topic_title = input("Enter Topic: ")
    viewer_object = get_viewer_by_uname(viewer_username)
    topic_object = get_topic_by_title(topic_title)
    destination = input("Enter destination link: ")
    
    if viewer_object:
        session.add(Share(viewer_id = viewer_object.viewer_id, topic_id = topic_object.topic_id, destination_link = destination))
        topic = session.query(Topic).filter_by(topic_id = topic_object.topic_id).first()
        topic.share_count += 1
        session.commit()
        print("Shared successfully...")
        
def delete_topic():
    session.query(Topic).delete()
    session.commit()
    print("All topics deleted successfully...")


        

def main():
    while True:
        actions = [
            "Add Viewer",
            "Add Topic",
            "Like Topic",
            "Dislike Topic",
            "Comment On Topic",
            "Report Topic",
            "Share Topic",
            "Add To Favorites",
            "Delete all topics",
            "Show a comment"
            "Exit"  # Add an exit option
        ]
        count = 1
        for action in actions:
            print(f"{count}. {action}")
            count += 1

        choice = input("Choose Action: ")

        if choice == "1":
            add_viewer()
        elif choice == "2":
            add_topic()
        elif choice == "3":
            like_topic()
        elif choice == "4":
            dislike_topic()
        elif choice == "5":
            comment_on_topic()
        elif choice == "6":
            report_topic()
        elif choice == "7":
            share_topic()
        elif choice == "8":
            favorite_topic()
        elif choice == "9":
            delete_topic()
        elif choice == "10":
            topic_id = input("enter_topic_id: ")
            get_comment_by_topic_id(topic_id)
        elif choice == "11":  # Exit condition
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

        
if __name__ == "__main__":
    main()
    