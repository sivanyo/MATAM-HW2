import Survey

AGE_STARTING_POSITION_IN_LINE = 2
MIN_AGE = 10
MAX_AGE = 100
MIN_SCORE = 1
MAX_SCORE = 10
NUM_OF_SCORES = 10
NUM_OF_CHOCOLATES = 5
ID_SIZE = 8
GENDER_MAN = "Man"
GENDER_WOMAN = "Woman"
VEGAN = "Vegan"
VEGETARIAN = "Vegetarian"
OMNIVORE = "Omnivore"
ID_INDEX = 0
HABITS_INDEX = 1
AGE_INDEX = 2
GENDER_INDEX = 3
SCORES_STARTING_INDEX = 4


# Filters a survey and prints to screen the corrected answers:
# old_survey_path: The path to the unfiltered survey
def correct_myfile(old_survey_path):
    lines_array = generate_initial_array_from_file(old_survey_path)
    unique_ids = generate_unique_ids_array(lines_array)
    filter_results(lines_array, unique_ids)
    sort_lines_by_id(lines_array)
    print_lines_array(lines_array)


# Returns a new Survey item with the data of a new survey file:
# survey_path: The path to the survey
def scan_survey(survey_path):
    lines_array = generate_initial_array_from_file(survey_path, True)
    survey = Survey.SurveyCreateSurvey()
    for line in lines_array:
        habits = parse_eating_habits(line[HABITS_INDEX])
        python_scores_list = line[SCORES_STARTING_INDEX:]
        # Generating int* array to store chocolate scores
        int_scores_array = Survey.SurveyCreateIntAr(NUM_OF_CHOCOLATES)
        # Inserting scores into int* array
        for i in range(NUM_OF_CHOCOLATES):
            Survey.SurveySetIntArIdxVal(int_scores_array, i,
                                        int(python_scores_list[i]))
        # Converting gender bool to corresponding integer type in C
        if line[GENDER_INDEX] is GENDER_WOMAN:
            gender = 0
        else:
            gender = 1
        Survey.SurveyAddPerson(survey, int(line[ID_INDEX]),
                               int(line[AGE_INDEX]), gender, habits,
                               int_scores_array)
        Survey.SurveyDestoryIntAr(int_scores_array)
    return survey


# Prints a python list containing the number of votes for each rating of a group according to the arguments
# s: the data of the Survey object
# choc_type: the number of the chocolate (between 0 and 4)
# gender: the gender of the group (string of "Man" or "Woman"
# min_age: the minimum age of the group (a number)
# max_age: the maximum age of the group (a number)
# eating_habits: the eating habits of the group (string of "Omnivore", "Vegan" or "Vegetarian")
def print_info(s, choc_type, gender, min_age, max_age, eating_habits):
    habits = parse_eating_habits(eating_habits)
    results = Survey.SurveyQuerySurvey(s, choc_type, gender, min_age,
                                       max_age, habits)
    output = []
    for i in range(NUM_OF_SCORES):
        output.append(Survey.SurveyGetIntArIdxVal(results, i))
    print(output)
    Survey.SurveyQueryDestroy(results)


# Clears a Survey object data
# s: the data of the Survey object
def clear_survey(s):
    Survey.SurveyDestroySurvey(s)


def generate_initial_array_from_file(old_survey_path, remove_spaces=False):
    """
    This function receives the path to the survey file, read it's contents
    and returns an array with each object being a string array of the split
    words from lines in the file.
    """
    lines_array = []

    with open(old_survey_path, 'r') as fp:
        line = fp.readline()
        while line:
            if remove_spaces is True:
                single_line = line.split()
            else:
                single_line = line.split(" ")
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
    for line in lines_array:
        # Remove spaces from input line for easy checks.
        clean_line = list(filter(lambda a: a != '', line))
        if clean_line[0] not in unique_ids \
                and len(clean_line[0]) == ID_SIZE:
            unique_ids.append(clean_line[0])
    return unique_ids


def check_valid_information(line):
    """
    This function checks if a line entry in the survey contains
    """
    # Remove spaces from input line for easy checks.
    clean_line = list(filter(lambda a: a != '', line))
    if int(clean_line[AGE_STARTING_POSITION_IN_LINE]) < MIN_AGE \
            or int(clean_line[AGE_STARTING_POSITION_IN_LINE]) > MAX_AGE:
        return False
    for score in clean_line[4:]:
        if int(score) < MIN_SCORE or int(score) > MAX_SCORE:
            return False
    return True


def filter_results(lines_array, unique_ids):
    for line in lines_array[::-1]:
        if line[0] in unique_ids:
            if check_valid_information(line):
                unique_ids.remove(line[0])
            else:
                lines_array.remove(line)
        else:
            lines_array.remove(line)
    return lines_array


def print_lines_array(lines_array):
    """
    This function prints the survey lines after filtering for compliant lines
    """
    for line in lines_array:
        print_survey_line(line)


def print_survey_line(line):
    """
    This function prints a single line in the survey file format
    """
    for word in line[:-1]:
        print(word, end=" ")
    print(line[-1])


def sort_lines_by_id(lines_array):
    """
    This function sorts the lines of the survey results array according to
    ascending IDs order
    """
    lines_array.sort(key=lambda x: x[0])
    return lines_array


def parse_eating_habits(habits):
    """
    This function receives a string of eating habits and converts it's value
    to the corresponding int
    """
    if habits == VEGAN:
        return 0
    elif habits == VEGETARIAN:
        return 1
    else:
        return 2
