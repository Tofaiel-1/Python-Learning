class VotingSystem:
    def __init__(self, candidates):
        self.candidates = candidates
        self.votes = {candidate: 0 for candidate in candidates}

    def vote(self, candidate):
        if candidate in self.candidates:
            self.votes[candidate] += 1
            print(f"Vote for {candidate} recorded successfully!")
        else:
            print("Invalid candidate!")

    def set_results(self, results):
        for candidate, votes in results.items():
            if candidate in self.candidates:
                self.votes[candidate] = votes
            else:
                print(f"Invalid candidate '{candidate}'. Results not updated.")

    def display_results(self):
        print("Voting Results:")
        for candidate, votes in self.votes.items():
            print(f"{candidate}: {votes} votes")


def main():
    candidates = ["Candidate A", "Candidate B", "Candidate C"]
    voting_system = VotingSystem(candidates)

    print("Welcome to the Voting System!")
    # Simulate 10 votes
    for _ in range(10):
        print("\nCandidates:")
        for idx, candidate in enumerate(candidates, start=1):
            print(f"{idx}. {candidate}")
        choice = input("Enter your choice (number): ")
        if choice.isdigit() and 0 < int(choice) <= len(candidates):
            candidate_idx = int(choice) - 1
            selected_candidate = candidates[candidate_idx]
            voting_system.vote(selected_candidate)
        else:
            print("Invalid choice! Please enter a valid number.")

    print("\nVoting completed. Setting results manually.")

    # Set results manually
    results = {
        "Candidate A": 5,
        "Candidate B": 3,
        "Candidate C": 2
    }
    voting_system.set_results(results)

    # Display final results
    voting_system.display_results()


if __name__ == "__main__":
    main()
