import csv

def sort_csv(choice):
    with open("top50.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        data = [row for row in reader]

    # Find the index of the chosen song
    for i, row in enumerate(data):
        if row[0] == str(choice):
            chosen_song = row
            chosen_index = i
            break

    # Sort the data based on all factors, in order of importance
    #other factors can be included in it
    sort_order = [ "Beats.Per.Minute", "Energy", "Danceability", "Loudness..dB..", "Liveness", "Valence.",
                  "Length.", "Acousticness..", "Speechiness.", "Popularity"]

    sort_indices = [header.index(sort) for sort in sort_order]
    data.sort(key=lambda x: [x[i] for i in sort_indices])

    # Move the chosen song to the first row
    data.pop(chosen_index)
    data = [chosen_song] + data

    # Print the sorted data
    print(header[0], header[1], header[2])
    for row in data:
        print(row[0], row[1], row[2])

# Prompt the user for their choice
choice = int(input("Enter the number of the song you want to choose: "))

sort_csv(choice)