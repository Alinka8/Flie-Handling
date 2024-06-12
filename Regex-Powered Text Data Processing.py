import re

def extract_emails(filename):
    email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    emails = set()
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                matches = email_pattern.findall(line)
                emails.update(matches)
                
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Permission denied to read the file '{filename}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return list(emails)

if __name__ == "__main__":
    filename = 'contacts.txt'
    emails = extract_emails(filename)
    print("Extracted emails:")
    for email in emails:
        print(email)
