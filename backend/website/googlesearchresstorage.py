from . import db
from website.models import Googlesearchresl


class DBStorage:
    def query_results(self, query):
        df = (
            Googlesearchresl.query.filter_by(query=query)
            .order_by(Googlesearchresl.y_index.asc())
            .all()
        )
        return df
    
    def query_results_by_relevance(self, query):
        df = (
            Googlesearchresl.query.filter_by(query=query)
            .order_by(Googlesearchresl.relevance.desc())
            .all()
        )
        return df
    #write a machine learning model to predict relevance
    #should be a function that takes in a query and returns a list of links
    #the list of links should be ordered by relevance
    #the model should be trained on the data in the database
    #the model should be saved in a file called model.pkl
    #the model should be loaded in the __init__ function
    #the model should be used in the query_results_by_relevance function
    #can use the scikit-learn library
    #can use the pickle library
    #can use the pandas library
    #can use the numpy library
    #can use the flask sqlalchemy library
    #can use the imbalanced-learn library

    
    

    def insert_row(self, values):
        cur = self.con.cursor()
        try:
            data = Googlesearchresl(
                query=values["query"],
                rank=values["rank"],
                link=values["link"],
                title=values["title"],
                snippet=values["snippet"],
                html=values["html"],
                relevance=values["relevance"],
                created=values["created"],
            )
            db.session.add_all(data)
            db.session.commit()
        except Exception:
            pass
        cur.close()

    def update_relevance(self, query, link, relevance):
        ggle = Googlesearchresl.query.filter_by(query=query, link=link).first()
        ggle.relevance = relevance
        db.session.commit()
