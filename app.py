import scrapy

class UniversitySpider(scrapy.Spider):
    name = "university_spider"
    start_urls = [
    "https://gradschool.utexas.edu/degrees-programs",
    "https://www.gradcollege.txstate.edu/programs.html",
    "https://www.depts.ttu.edu/gradschool/",
    "https://catalog.tamu.edu/graduate/degrees-programs/",
    "https://www.tsu.edu/academics/colleges-and-schools/the-graduate-school/",
    "https://www.uh.edu/graduate-school/prospective-students/programs/",
    "https://www.depts.ttu.edu/gradschool/programs/",
    "https://www.utdallas.edu/academics/graduate/",
    "https://www.baylor.edu/graduate/",
    "https://www.smu.edu/graduate"
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