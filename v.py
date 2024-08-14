# Simple Itinerary Planner

# Function to get user input for destinations and activities
def get_itinerary():
    itinerary = {}
    
    while True:
        destination = input("Enter a destination (or type 'done' to finish): ")
        if destination.lower() == 'done':
            break
        
        activities = input(f"Enter activities for {destination} (separated by commas): ").split(',')
        activities = [activity.strip() for activity in activities]
        
        itinerary[destination] = activities
    
    return itinerary

# Function to display the itinerary
def display_itinerary(itinerary):
    print("\nYour Travel Itinerary:")
    for destination, activities in itinerary.items():
        print(f"\nDestination: {destination}")
        print("Activities:")
        for activity in activities:
            print(f" - {activity}")

# Main function to run the itinerary planner
def main():
    print("Welcome to the Simple Itinerary Planner!")
    
    itinerary = get_itinerary()
    display_itinerary(itinerary)

    print("\nEnjoy your trip!")

if __name__ == "__main__":
    main()
