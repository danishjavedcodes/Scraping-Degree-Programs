import scrapy

class texas_spidy(scrapy.Spider):
    name = 'texas-spidy'
    start_urls  = [ 'https://www.mastersportal.com/search/master?kw-where=texas']
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


