from pythonFuncs import scan_survey, print_info, clear_survey

if __name__ == '__main__':
    s=scan_survey("survey2")
    print_info(s,0,"Woman",10,30,"Omnivore")
    clear_survey(s)