#pylint: disable=missing-docstring, C0103
'''The queries.py file is a file containing multiple functions that take in SQL code
that acquires and sorts certain data from an SQL document.
'''

def directors_count(db):
    # return the number of directors contained in the database
    query = """ SELECT COUNT ("directors".id)
    FROM "directors"
    """
    db.execute(query)
    results = db.fetchall()
    # results in a list (rows) of tuples (columns)

    # Then you'll need to return something.
    return int(results[0][0])


def directors_list(db):
    # return the list of all the directors sorted in alphabetical order
    query = '''SELECT directors.name
    FROM directors
    ORDER BY directors.name ASC
    '''
    db.execute(query)
    results = db.fetchall()
    # results in a list (rows) of tuples (columns)

    new_list = []
    for row in results:
        new_list.append(row[0])
    # Then you'll need to return something.
    return new_list



def love_movies(db):
    # return the list of all movies which contain the exact word "love"
    # in their title, sorted in alphabetical order
    query = ''' SELECT movies.title
    FROM movies
    WHERE UPPER(title) LIKE '% LOVE %'
        OR UPPER(title) LIKE 'LOVE %'
        OR UPPER(title) LIKE '% LOVE'
        OR UPPER(title) LIKE 'LOVE'
        OR UPPER(title) LIKE '% LOVE''%'
        OR UPPER(title) LIKE '% LOVE.'
        OR UPPER(title) LIKE 'LOVE,%'
        ORDER BY title
    '''
    db.execute(query)
    results = db.fetchall()
    # results in a list (rows) of tuples (columns)

    new_list = []
    for row in results:
        new_list.append(row[0])
    # Then you'll need to return something.
    return new_list




def directors_named_like_count(db, name):
    # return the number of directors which contain a given word in their name

    query = f'''SELECT COUNT(directors.name)
    FROM directors
    WHERE directors.name LIKE '% {name} %'
        OR UPPER(directors.name) LIKE '{name} %'
        OR UPPER(directors.name) LIKE '% {name}'
        OR UPPER(directors.name) LIKE '{name}'
        OR UPPER(directors.name) LIKE '%{name}%'
    '''

    db.execute(query)
    results = db.fetchall()
    # results in a list (rows) of tuples (columns)

    # Then you'll need to return something.
    return int(results[0][0])


def movies_longer_than(db, min_length):
    # return this list of all movies which are longer than a given duration,
    # sorted in the alphabetical order
    query = f''' SELECT movies.minutes, movies.title
    FROM movies
    WHERE movies.minutes > {min_length}
    ORDER BY movies.title ASC, movies.minutes ASC
    '''
    db.execute(query)
    results = db.fetchall()

    new_list = []
    for row in results:
        new_list.append(row[1])
    # results in a list (rows) of tuples (columns)

    # Then you'll need to return something.
    return new_list
