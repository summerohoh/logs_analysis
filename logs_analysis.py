# "Database code" for Logs Analysis
import psycopg2
import datetime

DBNAME = "news"

# 1. What are the most popular three articles of all time?
query1 = '''SELECT ARTICLE_VIEWS.title, views
            FROM(SELECT articles.title, count(*) AS views
                FROM articles JOIN log ON log.path LIKE '%'||articles.slug
                GROUP BY articles.title) AS ARTICLE_VIEWS
            ORDER BY views DESC
            LIMIT 3;
         '''

# 2. Who are the most popular article authors of all time?
query2 = '''SELECT authors.name, sum(views) as total_views
          FROM authors JOIN
          (SELECT articles.author, articles.title, count(*) AS views
                FROM articles JOIN log ON log.path LIKE '%'||articles.slug
                GROUP BY articles.author, articles.title) AS article_views
          ON authors.id=article_views.author
          GROUP BY authors.id
          ORDER BY total_views DESC;
       '''

# 3. On which days did more than 1% of requests lead to errors?
query3 = '''SELECT allrequests.date,
           round(error.total_error*100/allrequests.total_requests,2)
           as error_percentage
           FROM (SELECT date(time) as date, count(*)
                 as total_requests FROM log GROUP BY date) as allrequests
           JOIN (SELECT date(time) as date, count(*) as total_error FROM log
                 WHERE log.status = '404 NOT FOUND' GROUP BY date) as error
           ON allrequests.date=error.date
           WHERE round(error.total_error*100/allrequests.total_requests,2) > 1;
       '''


def get_query_result(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    return result
    db.close()


def print_views(result):
    for r in result:
        print('\t' + str(r[0]) + ' -- ' + str(r[1]) + ' views')


def print_error(result):
    for r in result:
        dateOfError = datetime.datetime.strptime(str(r[0]), '%Y-%m-%d')
        print(
              '\t' + dateOfError.strftime('%B %d, %Y') +
              ' -- ' + "{0:0.1f}".format(r[1]) + '% error'
             )


print("1. What are the most popular three articles of all time?")
query_result1 = get_query_result(query1)
print_views(query_result1)

print("2. Who are the most popular article authors of all time?")
query_result2 = get_query_result(query2)
print_views(query_result2)

print("3. On which days did more than 1% of requests lead to errors?")
query_result3 = get_query_result(query3)
print_error(query_result3)
