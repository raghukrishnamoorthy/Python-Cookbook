from urllib.request import urlopen

class urlTemplate:

    def __init__(self, template):
        self.template = template
    
    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))
    

yahoo = urlTemplate("http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}")
for line in yahoo.open(names='IBM,AAPL,FB', fields='sl1c1v'):
    print(line.decode('utf-8'))

#The above can be replaced with a function like so

def urlTemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))
    return opener

yahoo = urlTemplate("http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}")
for line in yahoo(names="IBM,AAPL,FB", fields = 'sl1c1v'):
    print(line.decode('utf-8'))

# Whenever you want to attach state to a function, think CLOSURES!!!!!