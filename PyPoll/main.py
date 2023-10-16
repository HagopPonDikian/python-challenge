import os
import csv

csvpath = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

total_votes = 0
tatal = rows = 0
unique_names = []
candidate_list = []
candidate_vote = []
percentage = []
i = 0


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    next(csvreader, None)

    for row in csvreader:
        total_votes = total_votes + 1
    
        
        if row[2] in candidate_list:
            i = candidate_list.index(row[2])
            candidate_vote[i] = candidate_vote[i] + 1
        else:
            candidate_list.append(row[2])
            candidate_vote.append(1)

    for j in candidate_vote:
        k = candidate_vote.index(j)
        x = round(candidate_vote[k] / total_votes * 100, 4)
        percentage.append(x)


    for k in candidate_vote:
        max_votes = max(candidate_vote)
        winner = candidate_list[candidate_vote.index(max_votes)]




        # test if the text it correct

        # print("""Election Results
        # -------------------------""")
        # print(f"Total Votes : {total_votes}")
        # print("-------------------------")
        # print(f"{candidate_list[0]} {percentage[0]}% ({candidate_vote[0]})")
        # print("")
        # print(f"{candidate_list[1]} {percentage[1]}% ({candidate_vote[1]})")
        # print("")
        # print(f"{candidate_list[2]} {percentage[2]}% ({candidate_vote[2]})")
        # print("-------------------------")
        # print(f"Winner: {winner}")
        # print("-------------------------")

        # set the path
        analysis = os.path.join("Analysis","analysis.txt")
        
with open(analysis, 'w') as text_file:

    text_file.write(f"""Election Results
    -------------------------
    Total Votes : {total_votes}
    --------------------------------
    {candidate_list[0]} {percentage[0]}% ({candidate_vote[0]})
    {candidate_list[1]} {percentage[1]}% ({candidate_vote[1]})
    {candidate_list[2]} {percentage[2]}% ({candidate_vote[2]})
    --------------------------------
    Winner: {winner}
    --------------------------------""")


