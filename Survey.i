%module Survey
%{
#define SWIG_FILE_WITH_INIT
#include "Survey.h"
%}

typedef enum { SURVEY_ALLOCATION_FAILED, SURVEY_SUCCESS} SurveyReturnValue;

typedef struct survey_t* Survey;

Survey SurveyCreateSurvey();

SurveyReturnValue SurveyAddPerson(Survey Survey, int Id, int Age, bool Gender, int EatingHabits , int* Scores);

int* SurveyQuerySurvey(Survey survey, int ChocolateType, bool Gender, int AgeMin, int AgeMax, int EatingHabits);

void SurveyQueryDestroy(int* histogram);

void SurveyDestroySurvey(Survey survey);

int* SurveyCreateIntAr(unsigned int size);

void SurveyDestoryIntAr(int* ar);

void SurveySetIntArIdxVal (int* ar, unsigned int idx, int val);

int SurveyGetIntArIdxVal(int* ar, unsigned int idx);
