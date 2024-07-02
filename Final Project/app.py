class VotingMachine:
    def __init__(self):
        self.candidates = {}
        self.votes = {}
        self.voters = set()  # Set to store unique voter IDs
        self.vote_limit = 1  # Maximum number of votes per voter

    def register_candidate(self, candidate, option):
        if option not in self.candidates:
            self.candidates[option] = []
            self.votes[option] = {}
        self.candidates[option].append(candidate)
        self.votes[option][candidate] = 0

    def vote(self, candidate, option, voter_id):
        if voter_id in self.voters:
            print("You have already voted.")
            return
        if option in self.candidates:
            if candidate in self.candidates[option]:
                self.votes[option][candidate] += 1
                self.voters.add(voter_id)
                print(f"\rVote for {candidate} in option {option} recorded successfully! ", end="")
                self.display_results(option)
            else:
                print("Invalid candidate for this option!")
        else:
            print("Invalid voting option!")

    def display_results(self, option=None):
        if option:
            print(f"\nVoting Results for Option {option}:")
            for candidate, votes in self.votes[option].items():
                print(f"{candidate}: {votes} votes")
            print("")
        else:
            print("\nOverall Voting Results:")
            for option, candidates in self.candidates.items():
                print(f"\nOption: {option}")
                for candidate, votes in self.votes[option].items():
                    print(f"{candidate}: {votes} votes")
            print("")

    def edit_option(self, old_option, new_option):
        if old_option in self.candidates:
            self.candidates[new_option] = self.candidates.pop(old_option)
            self.votes[new_option] = self.votes.pop(old_option)
        else:
            print("Option not found!")

    def delete_option(self, option):
        if option in self.candidates:
            del self.candidates[option]
            del self.votes[option]
        else:
            print("Option not found!")

def main():
    voting_machine = VotingMachine()

    print("Welcome to the Voting Machine!")

    while True:
        print("\nVoting Options:")
        print("1. Presidential Election")
        print("2. Local Council Election")
        print("3. Referendum")
        print("4. Edit Option")
        print("5. Delete Option")

        option = input("Enter your choice (1-5), or 'exit' to quit: ")

        if option.lower() == 'exit':
            print("\nExiting the Voting Machine.")
            break

        if option not in ['1', '2', '3', '4', '5']:
            print("Invalid option! Please enter a number between 1 and 5.")
            continue

        if option == '1':
            option_name = "Presidential Election"
        elif option == '2':
            option_name = "Local Council Election"
        elif option == '3':
            option_name = "Referendum"
        elif option == '4':
            old_option = input("Enter the name of the option to edit: ")
            new_option = input("Enter the new name for the option: ")
            voting_machine.edit_option(old_option, new_option)
            print(f"Option '{old_option}' edited successfully to '{new_option}'!")
            continue
        elif option == '5':
            option_to_delete = input("Enter the name of the option to delete: ")
            voting_machine.delete_option(option_to_delete)
            print(f"Option '{option_to_delete}' deleted successfully!")
            continue

        choice = input(f"\nOption {option}: \n1. Register Candidate \n2. Vote \n3. Display Results \nEnter your choice: ")

        if choice == '1':
            candidate = input("Enter the name of the candidate to register: ")
            voting_machine.register_candidate(candidate, option_name)
            print(f"{candidate} registered successfully for {option_name}!")
        elif choice == '2':
            if option_name not in voting_machine.candidates:
                print("No candidates registered yet for this option!")
                continue
            print(f"\nCandidates for {option_name}:")
            for idx, candidate in enumerate(voting_machine.candidates[option_name], start=1):
                print(f"{idx}. {candidate}")
            candidate_idx = int(input("Enter the number of your choice: ")) - 1
            selected_candidate = voting_machine.candidates[option_name][candidate_idx]
            voter_id = input("Enter your voter ID: ")
            voting_machine.vote(selected_candidate, option_name, voter_id)
        elif choice == '3':
            if option_name not in voting_machine.candidates:
                print("No candidates registered yet for this option!")
                continue
            voting_machine.display_results(option_name)
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
