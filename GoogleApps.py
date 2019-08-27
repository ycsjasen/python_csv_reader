#initiate csv
from csv import reader
opened_file = open('googleplaystore.csv', encoding ="utf-8")
read_file = reader(opened_file)
app_data = list(read_file)

#creating empty list
free_ratings = []
paid_ratings = []

#iterating through csv, ignoring header
for row in app_data[1:]:
    #if a rating is 'NaN', skip to next iteration
    if "NaN" in row:
        continue
    #prices listed with and without '$'
    try:
        price = float(row[7])
    except:
        price = float(row[7][1:])
    rating = float(row[2])
    reviews = float(row[3])

    #calculating number of installs; removing '+' at end
    install_st = row[5][:-1]
    install_st
    try:
        install = float(install_st)
    except:
        install = float(install_st.replace(',',''))

    if row[6] == 'Free':
        free_ratings.append(rating)

    elif row[6] == 'Paid':
        paid_ratings.append(rating)


#calculating average ratings of free and paid

free_avg_rating = sum(free_ratings)/len(free_ratings)
paid_avg_rating = sum(paid_ratings)/len(paid_ratings)

print('Average rating of free apps: {}'.format(free_avg_rating))
print('Average rating of paid apps: {}'.format(paid_avg_rating))