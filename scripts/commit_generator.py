#!/usr/bin/env python3
"""
LeetCode Solutions Commit Generator

This script simulates a history of daily commits to create a repository
with LeetCode solutions. It creates 5 solutions per day, starting from
February 5, 2025.

Usage:
1. Place this script in the scripts directory of your repository
2. Run it to generate commits with solutions for each day
"""

import os
import re
import datetime
import json
import random
import argparse
from typing import Dict, List, Tuple, Optional


# Define language-specific templates for solutions
TEMPLATES = {
    "python": '''"""
LeetCode Problem #{problem_id}: {problem_name}
https://leetcode.com/problems/{problem_slug}/

Date: {date}

Problem Description:
{problem_description}

Time Complexity: {time_complexity}
Space Complexity: {space_complexity}
"""

{solution_code}
''',
    "javascript": '''/**
 * LeetCode Problem #{problem_id}: {problem_name}
 * https://leetcode.com/problems/{problem_slug}/
 * 
 * Date: {date}
 *
 * Problem Description:
 * {problem_description}
 *
 * Time Complexity: {time_complexity}
 * Space Complexity: {space_complexity}
 */

{solution_code}
''',
    "java": '''/**
 * LeetCode Problem #{problem_id}: {problem_name}
 * https://leetcode.com/problems/{problem_slug}/
 * 
 * Date: {date}
 *
 * Problem Description:
 * {problem_description}
 *
 * Time Complexity: {time_complexity}
 * Space Complexity: {space_complexity}
 */

{solution_code}
''',
    "cpp": '''/**
 * LeetCode Problem #{problem_id}: {problem_name}
 * https://leetcode.com/problems/{problem_slug}/
 * 
 * Date: {date}
 *
 * Problem Description:
 * {problem_description}
 *
 * Time Complexity: {time_complexity}
 * Space Complexity: {space_complexity}
 */

{solution_code}
''',
    "c": '''/**
 * LeetCode Problem #{problem_id}: {problem_name}
 * https://leetcode.com/problems/{problem_slug}/
 * 
 * Date: {date}
 *
 * Problem Description:
 * {problem_description}
 *
 * Time Complexity: {time_complexity}
 * Space Complexity: {space_complexity}
 */

{solution_code}
'''
}

# File extensions for each language
EXTENSIONS = {
    "python": "py",
    "javascript": "js",
    "java": "java",
    "cpp": "cpp",
    "c": "c"
}

# Root directories for each language
DIRECTORIES = {
    "python": "Python",
    "javascript": "JavaScript",
    "java": "Java",
    "cpp": "CPP",
    "c": "C"
}


def create_solution_file(problem_id, problem_name, language):
    """Create a solution file for a given problem and language"""
    # Format problem_id to 4 digits with leading zeros
    problem_id_formatted = f"{problem_id:04d}"
    
    # Create problem slug (simplified)
    problem_slug = problem_name.lower().replace(" ", "-")
    
    # Simplified problem name for filename
    filename_name = re.sub(r'[^a-zA-Z0-9_]', '', problem_name.lower().replace(" ", "_"))
    filename = f"{problem_id_formatted}_{filename_name}.{EXTENSIONS[language]}"
    
    # Get directory for the language
    directory = DIRECTORIES[language]
    filepath = os.path.join(directory, filename)
    
    # Use random time/space complexity for demonstration
    complexities = ["O(1)", "O(log n)", "O(n)", "O(n log n)", "O(n²)", "O(2^n)"]
    time_complexity = random.choice(complexities)
    space_complexity = random.choice(complexities)
    
    # Simple placeholder for problem description
    problem_description = "Write a more detailed problem description here."
    
    # Simple placeholder for solution code based on language
    if language == "python":
        solution_code = "class Solution:\n    def solve(self):\n        pass  # Implement solution here"
    elif language == "javascript":
        solution_code = "/**\n * @param {number} n\n * @return {number}\n */\nvar solve = function(n) {\n    // Implement solution here\n};"
    elif language == "java":
        solution_code = "class Solution {\n    public int solve() {\n        // Implement solution here\n        return 0;\n    }\n}"
    elif language == "cpp":
        solution_code = "class Solution {\npublic:\n    int solve() {\n        // Implement solution here\n        return 0;\n    }\n};"
    else:  # C
        solution_code = "int solve() {\n    // Implement solution here\n    return 0;\n}"
    
    # Create the content using the template
    content = TEMPLATES[language].format(
        problem_id=problem_id,
        problem_name=problem_name,
        problem_slug=problem_slug,
        date=datetime.datetime.now().strftime("%B %d, %Y"),
        problem_description=problem_description,
        time_complexity=time_complexity,
        space_complexity=space_complexity,
        solution_code=solution_code
    )
    
    # Ensure directory exists
    os.makedirs(directory, exist_ok=True)
    
    # Write to file
    with open(filepath, 'w') as f:
        f.write(content)
    
    print(f"Created {filepath}")
    
    return filepath


def simulate_daily_commits():
    """Simulate daily commits of LeetCode solutions"""
    # Define a list of problem IDs and names for the simulation
    problems = [
        (1, "Two Sum"),
        (2, "Add Two Numbers"),
        (3, "Longest Substring Without Repeating Characters"),
        # ... add more problems as needed
    ]
    
    # Define the start date
    start_date = datetime.date(2025, 2, 5)
    
    # Define how many problems to solve per day
    problems_per_day = 5
    
    # For each problem
    for i, (problem_id, problem_name) in enumerate(problems):
        # Calculate the current date
        current_date = start_date + datetime.timedelta(days=(i // problems_per_day))
        
        # Create the solution in all languages
        for language in TEMPLATES.keys():
            create_solution_file(problem_id, problem_name, language)
        
        # Here you would typically:
        # 1. git add the created files
        # 2. git commit with a message including the date
        # 3. Optionally, set the commit date to the calculated date
        
        # For this script, we'll just print what would happen
        print(f"Committed solutions for problem {problem_id}: {problem_name} on {current_date}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate LeetCode solution files")
    parser.add_argument("--problem-id", type=int, help="The LeetCode problem ID")
    parser.add_argument("--problem-name", type=str, help="The LeetCode problem name")
    parser.add_argument("--language", choices=TEMPLATES.keys(), help="Programming language")
    parser.add_argument("--simulate", action="store_true", help="Simulate daily commits")
    
    args = parser.parse_args()
    
    if args.simulate:
        simulate_daily_commits()
    elif args.problem_id and args.problem_name and args.language:
        create_solution_file(args.problem_id, args.problem_name, args.language)
    else:
        parser.print_help()