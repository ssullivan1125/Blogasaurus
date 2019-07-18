import webapp2
import jinja2
import os
import datetime

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

currentDT = datetime.datetime.now()

class blogasaurus(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_env.get_template("templates/index.html")
        self.response.write(start_template.render())

class BlogHandler(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_env.get_template("templates/new_post.html")
        self.response.write(start_template.render())
    def post(self):
        title_var = self.request.get('title')
        content_var = self.request.get('content')
        author_var = self.request.get('author')

        the_post_var = {
            "title_var": title_var,
            "content_var": content_var,
            "author_var": author_var,
        }
        template = jinja_env.get_template('templates/view_post.html')
        self.response.write(template.render(the_post_var))




app = webapp2.WSGIApplication([
    ('/', blogasaurus),
    ('/new_post', BlogHandler)
], debug=True)
