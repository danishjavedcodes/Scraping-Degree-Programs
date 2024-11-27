import scrapy

class texas_spidy(scrapy.Spider):
    name = 'texas-spidy'
    start_urls  = [
    "https://gradschool.utexas.edu/degrees-programs",  # University of Texas at Austin
    "https://www.gradcollege.txstate.edu/programs.html",  # Texas State University
    "https://www.depts.ttu.edu/gradschool/",  # Texas Tech University
    "https://grad.tamu.edu/",  # Texas A&M University
    "https://www.baylor.edu/graduate/",  # Baylor University
    "https://www.uta.edu/academics/schools-colleges/graduate-school",  # University of Texas at Arlington
    "https://www.unthsc.edu/academics/",  # University of North Texas Health Science Center
    "https://www.ttuhsc.edu/biomedical-sciences/default.aspx",  # Texas Tech University Health Sciences Center
    "https://www.ischool.utexas.edu/programs/",  # University of Texas at Austin School of Information
    "https://www.gradcollege.txstate.edu/",  # Texas State University Graduate College
    "https://www.gradschools.com/graduate-schools-in-united-states/texas"  # General resource for graduate schools in Texas
    ]
    def parse(self, response):
        for program in response.css('div.program'):
            yield {
                'name': program.css('h2::text').get(),
                'degree_program': program.css('span.degree::text').get(),
                'university_name': program.css('span.university::text').get(),  
                'country': 'USA',  
                'city': 'Texas',  
                'fee': program.css('span.fee::text').get(),
                'application_fee': program.css('span.application-fee::text').get(),
                'apply_date': program.css('span.apply-date::text').get(),
                'deadline': program.css('span.deadline::text').get(),
                'intake_type': program.css('span.intake-type::text').get(),
                'program_start_date': program.css('span.start-date::text').get(),
                'program_duration': program.css('span.duration::text').get(),
                'requirements': {
                    'ielts': program.css('span.ielts::text').get(),
                    'ielts_score': program.css('span.ielts-score::text').get(),
                    'block_account': program.css('span.block-account::text').get(),
                    'gre': program.css('span.gre::text').get(),
                    'gpa': program.css('span.gpa::text').get(),
                    'documents': program.css('span.documents::text').getall(),
                }
            }


