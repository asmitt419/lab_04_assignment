class MatchTable:
    def _init_(self):
        # Initialize the match data as a list of dictionaries
        self.matches = [
            {"Location": "Mumbai", "Team 01": "India", "Team 02": "Sri Lanka", "Timing": "DAY"},
            {"Location": "Delhi", "Team 01": "England", "Team 02": "Australia", "Timing": "DAY-NIGHT"},
            {"Location": "Chennai", "Team 01": "India", "Team 02": "South Africa", "Timing": "DAY"},
            {"Location": "Indore", "Team 01": "England", "Team 02": "Sri Lanka", "Timing": "DAY-NIGHT"},
            {"Location": "Mohali", "Team 01": "Australia", "Team 02": "South Africa", "Timing": "DAY-NIGHT"},
            {"Location": "Delhi", "Team 01": "India", "Team 02": "Australia", "Timing": "DAY"}
        ]

    def search_by_team(self, team_name):
        matches = []
        for match in self.matches:
            if team_name in (match["Team 01"], match["Team 02"]):
                matches.append(match)
        return matches

    def search_by_location(self, location):
        matches = []
        for match in self.matches:
            if match["Location"] == location:
                matches.append(match)
        return matches

    def search_by_timing(self, timing):
        matches = []
        for match in self.matches:
            if match["Timing"] == timing:
                matches.append(match)
        return matches

    def display_matches(self, matches):
        if not matches:
            print("No matches found.")
        else:
            print("Location\tTeam 01\tTeam 02\tTiming")
            for match in matches:
                print(f"{match['Location']}\t{match['Team 01']}\t{match['Team 02']}\t{match['Timing']}")

def main():
    match_table = MatchTable()
    while True:
        print("\nSearch Options:")
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Quit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            team_name = input("Enter the team name: ")
            matches = match_table.search_by_team(team_name)
            match_table.display_matches(matches)
        elif choice == "2":
            location = input("Enter the location: ")
            matches = match_table.search_by_location(location)
            match_table.display_matches(matches)
        elif choice == "3":
            timing = input("Enter the timing: ")
            matches = match_table.search_by_timing(timing)
            match_table.display_matches(matches)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2/3/4).")

if __name__ == "__main__":
    main()