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
