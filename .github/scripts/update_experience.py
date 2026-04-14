import os
import re
from datetime import datetime

def main():
    # Set the start date for experience calculation
    start_date = datetime(2024, 1, 18)
    today = datetime.now()
    
    # Calculate years of experience, rounded to 1 decimal place
    days = (today - start_date).days
    years = round(days / 365.25, 1)
    
    # Regex to find existing 'X.X years of experience' or similar
    # Supports optional 'of' and floating point numbers
    pattern = re.compile(r'\b(\d+\.\d+)\s+(years of experience)\b')
    
    # Correct path calculation for root of repo
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(os.path.dirname(script_dir))
    resume_dir = os.path.join(repo_root, "resume")
    
    for root, dirs, files in os.walk(resume_dir):
        if "resume.tex" in files:
            filepath = os.path.join(root, "resume.tex")
            with open(filepath, 'r') as f:
                content = f.read()
            
            # Replace occurrences with the newly calculated years
            new_content = pattern.sub(f"{years} \g<2>", content)
            
            if new_content != content:
                with open(filepath, 'w') as f:
                    f.write(new_content)
                print(f"Updated years of experience to {years} in {os.path.relpath(filepath, repo_root)}")

if __name__ == "__main__":
    main()
