import re
from fuzzywuzzy import process

# Entity extraction using regular expressions
def extract_entities_regex(query):
    # Regular expressions for entity extraction
    time_regex = r'\b(\d{1,2}:\d{2}\s?[ap]m)\b'  # Extract time in HH:MM AM/PM format
    date_regex = r'(\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b)|(\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2}(?:st|nd|rd|th)?(?:,?\s\d{2,4})?)\b'  # Extract date in various formats
    link_regex = r'(?:https?:\/\/)?(?:www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:\/[^\s]*)?'  # Extract URL

    # Extract entities using regular expressions
    entities = {}
    entities['time'] = re.findall(time_regex, query)
    entities['date'] = re.findall(date_regex, query)
    entities['link'] = re.findall(link_regex, query)

    return entities

# Entity extraction using FuzzyWuzzy
def extract_entities_fuzzy(query, entity_list, score_cutoff=0):
    # Extract entities using FuzzyWuzzy
    entities = process.extract(query, entity_list)
    entities = [entity[0] for entity in entities if entity[1] >= score_cutoff]
    return entities

# Main function
def main():
    # Example entity list for FuzzyWuzzy for Fuzzy Search
    # This allows you to detect these keywords directly, but less rigid then RegEx
    # In a production environment, you would likely use multiple of these with specifically labeled lists
    # which would each classify as a subcategory in entities, like variable:age,name,email
    # so your program knows what part of a query the user is providing input to
    entity_list = ['description', 'location', 'variable']
    # you can also control cutoff (simularity check) of your fuzzy search function matches
    score_cutoff = 45  # Set your desired score cutoff here.
    # Higher = more rigid, harder to detect
    # Lower = better chance of matching, more false positives

    while True:
        # Prompt for user input
        query = input("Enter your command (or 'q' to quit): ")

        if query.lower() == 'q':
            break

        #this is where you would put your intent extraction in a production pipeline

        # Entity extraction using regular expressions
        entities_regex = extract_entities_regex(query)
        print("Entities (Regex):", entities_regex)

        # Entity extraction using FuzzyWuzzy
        entities_fuzzy = extract_entities_fuzzy(query, entity_list, score_cutoff=score_cutoff)
        print("Entities (FuzzyWuzzy):", entities_fuzzy)

        #this iw where you would put your machiine learning entity extraction in a production pipeline

        #this is where you would send off all your entities or start using them to execute real commands

if __name__ == "__main__":
    main()
