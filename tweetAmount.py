import pandas as pd
import mysql.connector as sql

config = {
    'user': 'root',
    'password': 'root',
    'host': 'Randy',
    'port': '3307',
    'database' : 'test'
}

def tweetAmount():
    
    query = """
    SELECT FULLNAME, TWEETS
    FROM USERS_USER
    WHERE USERS_USER.TWEETS>0
    """

    cnn  = sql.connect(**config)
    cursor =  cnn.cursor()
    cursor.execute(query)

    amount = []
    index = []
    data = cursor.fetchall()
    for elem in data:
        index.append(elem[0])
        amount.append(elem[1])
    df = pd.Series(amount,index = index)
    ax = df.plot(kind='bar',color='k', alpha=0.7)
    fig = ax.get_figure()
    fig.savefig('tweetAmount.png')


if __name__ == "__main__":
    tweetAmount()
