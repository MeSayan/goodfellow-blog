import sys
import shlex
from subprocess import Popen, PIPE

def writeTemplate(name, author, date):

    outputfile = name[:-3] + '.html'
    title = name[:-3].split('-')
    title = ' '.join(title)
    #Convert to title case
    title = title.title()
    
    with open(outputfile,"w+") as f:    
        f.write('<!DOCTYPE HTML>\n')
        f.write('<html>\n')
        f.write('<meta charset=\"utf-8">\n')
        f.write("<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n")
        f.write('<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n')
        f.write('<title>{}</title>\n'.format(title))
        f.write('<!--Bootstrap-->\n')
        f.write('<link href=\"../css/bootstrap.min.css\" rel=\"stylesheet\">\n')
        f.write('<link href=\"../css/style.css\" rel=\"stylesheet\">\n')
        f.write('<!--[if lt IE 9]-->\n')
        f.write('<script src=\"https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.j\"></script>\n')
        f.write('<script src=\"https://oss.maxcdn.com/respond/1.4.2/respond.min.j\"></script>\n')
        f.write('<!--[endif]-->\n')
        f.write('</head>\n')

        f.write('<body>\n')
        f.write('<nav class=\"navbar navbar-custom\">\n')
        f.write('<div class=\"container-fluid\">\n')
        f.write('<div class=\"navbar-header\">\n')
        f.write('<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">\n')
        f.write('<span class="icon-bar"></span>\n')
        f.write('<span class="icon-bar"></span>\n')
        f.write('<span class="icon-bar"></span>\n')
        f.write('</button>\n')
        f.write('<a class="navbar-brand" href="../index.html">GoodFellow</a>\n')
        f.write('</div>\n')
        f.write('<div class="collapse navbar-collapse" id="myNavbar">\n')
        f.write('<ul class="nav navbar-nav navbar-right">\n')
        f.write('<li><a href="../index.html">Home</a></li>\n')
        f.write('<li><a href="../article.html">Articles</a></li>\n')
        f.write('</ul>\n')
        f.write('</div>\n')
        f.write('</div>\n')
        f.write('</nav>\n')

        #container
        f.write('<div class="container" data-date="{}" data-author="{}">\n'.format(date,author))
        f.write('<div class="page col-sm-8 col-sm-offset-2 text-justify">\n')
        f.write('<div class="article">\n')
            
        f.write('<h1 class="article-title">{}</h1>\n'.format(title))
        f.write('<div class="row art-credentials">\n')
        f.write('<div class="col-sm-6">Date: {}</div>\n'.format(date))
        f.write('<div class="col-sm-6">By: {}</div>\n'.format(author))
        f.write('</div>\n')
        f.write('<div class="row share-buttons">\n')
        f.write('<button class="btn" id="wapp-btn"><a href="whatsapp://send?text=Check out this blog post." data-action="share/whatsapp/share"> Whatsapp</a></button>\n')
        f.write('</div>\n')
        #f.write('</div>\n')

            
            

        # input file from markdown here
        cmd = "markdown " + name
        process = Popen(shlex.split(cmd),stdout=PIPE)
        (out,erno) = process.communicate()
        st_no  = process.wait()

        #decode the bytes in utf-8 string
        output = out.decode('utf-8')
        f.write(output)

        f.write('</div>\n')
        #pager
        f.write('<ul class="pager">\n')
        f.write('<li><a href="">Previous</a></li>\n')
        f.write('<li><a href="">Next</a></li>\n')
        f.write('</ul>\n')
        f.write('</div>\n')
        f.write('</div>\n')
        #footer
        f.write('<footer class="page">\n')
        f.write('<p>Designed by Sayan Mahapatra</p>\n')
        f.write('<p>Copyright &copy; Sayan Mahapatra</p>\n')
        f.write('</footer>\n')


        #jQuery
        #f.write('<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>\n')
        #Bootstrap js
        #f.write('<script src="../js/bootstrap.min.js"></script>\n')
        f.write('</body>\n')
        f.write('</html>\n')
		
    
if __name__=="__main__":
    # params: (name, data, author)

    if len(sys.argv) < 4:
        print('Usage: htmlizer filename date author')
    else:
        name = sys.argv[1]
        date = sys.argv[2]
        author = sys.argv[3]
        writeTemplate(name,author,date)
