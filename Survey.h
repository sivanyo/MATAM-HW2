
#ifndef SURVEY_H
#define SURVEY_H

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>


#define SURVEY_NUM_GRADES 10
#define SURVEY_NUM_OF_CHOCOLATES 5


typedef struct survey_t * Survey;

typedef struct survey_person_t * SurveyPerson;

//typedef int SurveyEatingHabits;

#define SURVEY_VEGAN 0
#define SURVEY_VEGATERIAN 1
#define SURVEY_OMNIVORE 2

typedef enum { SURVEY_ALLOCATION_FAILED, SURVEY_SUCCESS} SurveyReturnValue;

//Creates the survey structure. Returns NULL if fails.
Survey SurveyCreateSurvey();

//Adds a person to the survey structure. Returns ALLOCATION_FAILED if fails, otherwise SUCCESS
SurveyReturnValue SurveyAddPerson(Survey Survey, int Id, int Age, bool Gender, int EatingHabits , int* Scores);

//Outputs a query to the survey (can be accessed as an int array).  Returns NULL if fails.
int* SurveyQuerySurvey(Survey survey, int ChocolateType, bool Gender, int AgeMin, int AgeMax, int EatingHabits);

//Destroys the query. 
void SurveyQueryDestroy(int* histogram);

//Destroys the survey structure
void SurveyDestroySurvey(Survey survey);

//Creates an int array of 'size' elements
int* SurveyCreateIntAr(unsigned int size);

//Releases int array 'ar'
void SurveyDestoryIntAr(int* ar);

//Sets an element of int array 'ar' of index 'idx' with value 'val'
void SurveySetIntArIdxVal (int* ar, unsigned int idx, int val);

//Returns an element of 'ar' of index 'idx'
int SurveyGetIntArIdxVal(int* ar, unsigned int idx);


#endif //SURVEY_H
