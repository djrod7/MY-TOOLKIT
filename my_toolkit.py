
numbers = [71, 94, 97, 80, 75, 89, 93]

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
    

def find_max_and_min(numbers):
    if not numbers:
        return (0, 0)

    max_value = numbers[0]
    min_value = numbers[0]

    for num in numbers:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num

    return (max_value, min_value)
  
    
def count_occurrences(items, target):
    count = 0

    for item in items:
        if item == target:
            count += 1
    
    return count

def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned


def create_report(title, scores):
    average = calculate_average(scores)
    max_value, min_value = find_max_and_min(scores)

    report = (
        f"--- {title} ---\n"
        f"Total Students : {len(scores)}\n"
        f"Average Score  : {average:.2f}\n"
        f"Highest Score  : {max_value}\n"
        f"Lowest Score   : {min_value}\n"
    )

    return report


if __name__ == "__main__":
    test_scores = [85, 92, 78, 95, 88, 70, 93]

    print(f"Average: {calculate_average(test_scores)}")
    print(f"Max/Min: {find_max_and_min(test_scores)}")
    print(f"Count of 85: {count_occurrences(test_scores, 85)}")
    print(f"'racecar' palindrome: {is_palindrome('racecar')}")
    print(f"'hello' palindrome: {is_palindrome('hello')}")
    print()
    print(create_report("Class Scores", test_scores))

