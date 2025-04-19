#!/bin/bash
# LeetCode Solutions Commit Script
#
# This script helps create Git commits with proper dates for LeetCode solutions
# It assumes you have git installed and are in the repository root directory
#
# Usage: ./scripts/commit.sh <problem_id> <problem_name> <date>
#
# Example: ./scripts/commit.sh 42 "Trapping Rain Water" "2025-02-25"

# Check if the correct number of arguments are provided
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <problem_id> <problem_name> <date>"
    echo "Example: $0 42 \"Trapping Rain Water\" \"2025-02-25\""
    exit 1
fi

PROBLEM_ID=$1
PROBLEM_NAME=$2
DATE=$3

# Format the problem ID with leading zeros (4 digits)
FORMATTED_ID=$(printf "%04d" $PROBLEM_ID)

# Find files related to this problem
FILES=$(find . -name "${FORMATTED_ID}_*" | tr '\n' ' ')

if [ -z "$FILES" ]; then
    echo "No files found for problem #$PROBLEM_ID"
    exit 1
fi

# Create commit message
COMMIT_MSG="Add solution for LeetCode problem #$PROBLEM_ID: $PROBLEM_NAME"

# Add files to git
git add $FILES

# Create commit with specified date
GIT_AUTHOR_DATE="$DATE T12:00:00" GIT_COMMITTER_DATE="$DATE T12:00:00" git commit -m "$COMMIT_MSG"

echo "Created commit for problem #$PROBLEM_ID: $PROBLEM_NAME with date $DATE"
echo "Files included in commit: $FILES"