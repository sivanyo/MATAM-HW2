# Filters a survey and prints to screen the corrected answers:
# old_survey_path: The path to the unfiltered survey
def correct_myfile(old_survey_path):
    lines_array = generate_initial_array_from_file(old_survey_path)
    print('Our result array looks like this:')
    for line in lines_array:
        print(line)

    unique_ids = generate_unique_ids_array(lines_array)
    print('Unique IDs array:')
    print(unique_ids)


# Returns a new Survey item with the data of a new survey file:
# survey_path: The path to the survey
def scan_survey(survey_path):
    pass


# Prints a python list containing the number of votes for each rating of a group according to the arguments
# s: the data of the Survey object
# choc_type: the number of the chocolate (between 0 and 4)
# gender: the gender of the group (string of "Man" or "Woman"
# min_age: the minimum age of the group (a number)
# max_age: the maximum age of the group (a number)
# eating_habits: the eating habits of the group (string of "Omnivore", "Vegan" or "Vegetarian")
def print_info(s, choc_type, gender, min_age, max_age, eating_habits):
    pass


# Clears a Survey object data
# s: the data of the Survey object
def clear_survey(s):
    pass


def generate_initial_array_from_file(old_survey_path):
    """
    This function receives the path to the survey file, read it's contents
    and returns an array with each object being a string array of the split
    words from lines in the file.
    """
    lines_array = []

    with open(old_survey_path, 'r') as fp:
        line = fp.readline()
        while line:
            single_line = line.split()
            for i in range(len(single_line)):
                single_line[i] = single_line[i].rstrip()
            lines_array.append(single_line)
            line = fp.readline()

    return lines_array


def generate_unique_ids_array(lines_array):
    """
    This function receives the line array and creates an array of unique ids
    from the list of available ID entries.
    """
    unique_ids = []
    for i in range(len(lines_array)):
        if lines_array[i][0] not in unique_ids:
            unique_ids.append(lines_array[i][0])
    return unique_ids

def main():
    correct_myfile('./survey1')


if __name__ == '__main__':
    main()
