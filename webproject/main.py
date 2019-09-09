import web

urls = (
    '/(.*)', 'index'
)

app = web.application(urls, globals())

class index: 
    def GET(self, name):
        return '<h3>Hoi ' + name + '.</h3> What is up?'

if __name__ == "__main__":
    app.run()