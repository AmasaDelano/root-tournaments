import os
import csv
from datetime import datetime

tournament_name = "Winter Tournament"
data_file = "data3.csv"
round = "3"

# Read CSV data into data structure.

script_dir = os.path.dirname(__file__)
csv_file_path = os.path.join(script_dir, data_file)

with open(csv_file_path) as csv_file:
    data = csv.reader(csv_file)
    next(data)

    for row in data:
        # Create new file with 4 HTML table rows based on the CSV data.

        # CSV:
        #  0: 11/27/2020 18:09:36 PM CST
        #  1: Group 6
        #  2: Fall
        #  3: Exiles & Partisans
        #  4: "Eyrie Dynasties, Vagabond, Riverfolk Company, Underground Duchy, 2nd Vagabond"
        #  5: Adventurer
        #  6: 
        #  7: Thextera
        #  8: Underground Duchy
        #  9: 29
        # 10:
        # 11: Postis
        # 12: Riverfolk Company
        # 13: 27
        # 14: 
        # 15: Shair
        # 16: Vagabond
        # 17: Coalition
        # 18: Eyrie Dynasties
        # 19: MarcustheCat
        # 20: Eyrie Dynasties
        # 21: 30
        # 22: 
        # 23: Eyrie Dynasties
        #
        # HTML:
        # <tr>
        #   <td>Winter Tournament</td>
        #   <td>1</td>
        #   <td>7</td>
        #   <td>22 Nov 2020</td>
        #   <td>Fall</td>
        #   <td>Standard</td>
        #   <td>Guerric</td>
        #   <td>Vagabond (Thief)</td>
        #   <td>14</td>
        #   <td>Lost</td>
        # </tr>

        cell_separator = "</td><td>"
        end_of_row = "</td></tr>"

        winner = row[23]
        
        # Tournament Name
        html_common_data = "<tr><td>" + tournament_name + cell_separator
        
        # Round Number
        html_common_data += round + cell_separator
        
        # Group/Game Number
        group_num = "".join(filter(str.isdigit, row[1]))
        html_common_data += group_num + cell_separator
        
        # Date
        parsed_date = datetime.strptime(row[0], "%Y/%m/%d %H:%M:%S %p CST")
        formatted_date = parsed_date.strftime("%d %b %Y")
        html_common_data += formatted_date + cell_separator

        # Map
        html_common_data += row[2] + cell_separator

        # Deck
        html_common_data += row[3] + cell_separator

        html = "<!-- ROUND " + round + ", GROUP " + group_num + " -->\n" + html_common_data

        def getPrettyFaction(row_data, player_index):
            faction = row[player_index + 1]
            if faction == "Vagabond":
                faction += " (" + row_data[5] + ")"
            elif faction == "2nd Vagabond":
                faction += " (" + row_data[6] + ")"
            return faction

        def getScore(row_data, player_index):
            score = row_data[player_index + 2]
            faction = row_data[player_index + 1]
            if (faction == "Vagabond" or faction == "2nd Vagabond") and score == "Coalition":
                score += " (w/" + row_data[player_index + 3] + ")"
            return score

        def getWonOrLost(row_data, player_index):
            faction = row_data[player_index + 1]
            coalition_with = row_data[player_index + 3]
            return "Won" if faction == winner or coalition_with == winner else "Lost"

        # Player 1
        html += row[7] + cell_separator

        # Turn Order 1
        html += "1" + cell_separator

        # Faction 1
        html += getPrettyFaction(row, 7) + cell_separator

        # Final Score 1
        html += getScore(row, 7) + cell_separator

        # Won/Lost 1
        html += getWonOrLost(row, 7) + end_of_row + "\n\r"

        # Player 2
        html += html_common_data + row[11] + cell_separator

        # Turn Order 2
        html += "2" + cell_separator

        # Faction 2
        html += getPrettyFaction(row, 11) + cell_separator

        # Final Score 2
        html += getScore(row, 11) + cell_separator

        # Won/Lost 2
        html += getWonOrLost(row, 11) + end_of_row + "\n\r"

        # Player 3
        html += html_common_data + row[15] + cell_separator
        
        # Turn Order 3
        html += "3" + cell_separator

        # Faction 3
        html += getPrettyFaction(row, 15) + cell_separator

        # Final Score 3
        html += getScore(row, 15) + cell_separator

        # Won/Lost 3
        html += getWonOrLost(row, 15) + end_of_row + "\n\r"

        # Player 4
        html += html_common_data + row[19] + cell_separator

        # Turn Order 4
        html += "4" + cell_separator

        # Faction 4
        html += getPrettyFaction(row, 19) + cell_separator

        # Final Score 4
        html += getScore(row, 19) + cell_separator

        # Won/Lost 4
        html += getWonOrLost(row, 19) + end_of_row

        # TODO: Figure out why line breaks are inconsistent.
        print(html)
        
# ...

# Profit!