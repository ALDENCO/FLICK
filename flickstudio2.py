from flask import Flask, request

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>FlickList</title>
    </head>
    <body>
        <h1>FlickList</h1>
"""

page_footer = """
    </body>
</html>
"""

# a form for adding new movies
add_form = """
    <form action="/add" method="post">
        <label for="new-movie">
            I want to add
            <input type="text" id="new-movie" name="new-movie"/>
            to my watchlist.
        </label>
        <input type="submit" value="Add It"/>
    </form>
"""

# TODO:
# Create the HTML for the form below so the user can check off a movie from their list 
# when they've watched it.
# Name the action for the form '/crossoff' and make its method 'post'.

# a form for crossing off watched movies
def get_current_watchlist():
    # returns user's current watchlist--hard coded for now
    return [ "HEAT", "Casino", "Goodfellas", "Saving Private Ryan" ]

# a form for crossing off watched movies
# (first we build a dropdown from the current watchlist items)
crossoff_options = ""
for movie in get_current_watchlist():
    crossoff_options += '<option value="{0}">{0}</option>'.format(movie)


for movie in get_current_watchlist():
    crossoff_options += '<option value="{0}">{0}</option>'.format(movie)

crossoff_form = """
    <form action="/crossoff" method="post">
        <label>
            I want to cross off
            <select name="crossed-off-movie"/>
                {0}
            </select>
            from my watchlist.
        </label>
        <input type="submit" value="Cross It Off"/>
    </form>
""".format(crossoff_options)


@app.route("/crossoff", methods=['POST'])
def crossoff_movie():
    crossed_off_movie = request.form['crossed-off-movie']

    # if we didn't redirect by now, then all is well
    crossed_off_movie_element = "<strike>" + crossed_off_movie + "</strike>"
    confirmation = crossed_off_movie_element + " has been crossed off your Watchlist."
    content = page_header + "<p>" + confirmation + "</p>" + page_footer

    return content


@app.route("/add", methods=['POST'])
def add_movie():
    new_movie = request.form['new-movie']

    # TODO 
    # 'escape' the user's input so that if they typed HTML, it doesn't mess up our site
    
    # TODO 
    # if the user typed nothing at all, redirect and tell them the error

    # TODO 
    # if the user wants to add a terrible movie, redirect and tell them not to add it b/c it sucks

    # build response content
    new_movie_element = "<strong>" + new_movie + "</strong>"
    sentence = new_movie_element + " has been added to your Watchlist!"
    content = page_header + "<p>" + sentence + "</p>" + page_footer

    return content


@app.route("/")
def index():
    edit_header = "<h2>Edit My Watchlist</h2>"

    # combine all the pieces to build the content of our response
    main_content = edit_header + add_form + crossoff_form


    # build the response string
    content = page_header + main_content + page_footer

    return content


app.run()