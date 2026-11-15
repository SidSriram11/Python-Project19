blank_list = []
print(blank_list)

scores = [81, 64, 93, 75, 88]
print("Class Scores:", scores)

repeated_test = [15, 25, 35] * 2
print("Duplicated Sample Scores:", repeated_test)

print("Total entries:", len(scores))

print("Initial score:", scores[0])
print("Final score:", scores[-1])

top_three_entries = scores[0:3]
print("Opening three scores:", top_three_entries)

flipped_scores = scores[::-1]
print("Scores in reverse order:", flipped_scores)

def check_matching_digits(data):
    total_matches = 0
    found_values = []

    for item in data:
        num_str = str(item)

        if len(num_str) > 1 and num_str[0] == num_str[-1]:
            total_matches += 1
            found_values.append(item)

    print("Scores starting and ending with the same digit:", found_values)
    return total_matches

matching_total = check_matching_digits([66, 84, 55, 91, 44])
print("Count of matching scores:", matching_total)

sum_of_scores = 0

for value in scores:
    sum_of_scores += value

mean_score = sum_of_scores / len(scores)

print("Combined score:", sum_of_scores)
print("Mean score:", mean_score)

scores.sort()

print("Minimum score recorded:", scores[0])
print("Maximum score recorded:", scores[-1])

print("")
print("***** CLASS SCORE REPORT *****")
print("Ordered Scores:", scores)
print("Combined Score:", sum_of_scores)
print("Mean Score:", mean_score)
print("Minimum Score:", scores[0])
print("Maximum Score:", scores[-1])
print("******************************")
