from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

skills = []
Role = ''
buffer = None
def draw_line(c, x, y, width):
    c.setStrokeColor(colors.black)
    c.line(x, y, width - 40, y)

def check_page_space(c, y, needed_space, height):
    if y < needed_space:
        c.showPage()
        return height - 40
    return y

def draw_personal_section(c, x, y):
    c.setFont("Times-Bold", 16)
    c.drawString(x, y, "GOKUL VASANTH")
    y -= 20
    c.setFont("Times-Bold", 14)
    c.drawString(x, y, Role)
    c.setFont("Times-Roman", 12)
    y -= 15
    c.drawString(x, y, "Chennai, Tamil Nadu 600042 | +91 7339557072")
    y -= 15
    c.drawString(x, y, "gokulvbe1303@gmail.com | https://g0c001.github.io/Portfolio/")
    y -= 30
    draw_line(c, x, y, letter[0])
    return y - 20

def draw_professional_summary(c, x, y):
    c.setFont("Times-Bold", 14)
    c.drawString(x, y, "Professional Summary:")
    y -= 15
    c.setFont("Times-Roman", 12)

    """ 
    I am a proactive Computer Science Engineering graduate from Anna University, 
    with a strong background in technology and innovation. I thrive in creating 
    impactful solutions and have a passion for delivering high-quality results. My 
    excellent problem-solving abilities and eagerness to contribute make me a great 
    fit for entry-level roles."""
    c.drawString(x + 20, y, "I am a proactive Computer Science Engineering graduate from Anna University, with a strong")
    y -= 15
    c.drawString(x + 20, y, "background in technology and innovation. I thrive in creating impactful solutions and have")
    y -= 15
    c.drawString(x + 20, y, "a passion for delivering high-quality results. My excellent problem-solving abilities and")
    y -= 15
    c.drawString(x + 20, y, "eagerness to contribute make me a great fit for entry-level roles.")
    y -= 30
    draw_line(c, x, y, letter[0])
    return y - 20

def draw_projects_section(c, x, y):
    c.setFont("Times-Bold", 14)
    c.drawString(x, y, "Projects:")
    y -= 20
    projects = [
        ("W3Schools (Frontend)", "Jul 2023 - Jul 2023", "Built using HTML, CSS, Bootstrap, and JavaScript for a modern and user-friendly web experience."),
        ("Trendy (Full-stack)", "Aug 2023 - Aug 2023", "Developed a full stack website using HTML, CSS, Bootstrap, JavaScript, Django, Python, MySQL."),
        ("Test Portal (Full-stack)", "Sep 2023 - Oct 2023", "Created a test portal for students to attend exams with mic, camera, and speaker permissions."),
        ("Helper Bot (Full-stack)", "Jan 2024 - Feb 2024", "Developed a query-answer bot with intuitive hover effects, adjusting gracefully to different screen sizes.")
    ]

    for project, duration, description in projects:
        c.setFont("Times-Bold", 12)
        c.drawString(x + 20, y, f"{project}  {duration}")
        y -= 15
        c.setFont("Times-Roman", 12)
        c.drawString(x + 20, y, description)
        y -= 30
        y = check_page_space(c, y, 40, letter[1])

    draw_line(c, x, y, letter[0])
    return y - 20

def draw_strengths_section(c, x, y):
    c.setFont("Times-Bold", 14)
    c.drawString(x, y, "Key Strengths:")
    y -= 15
    strengths = [
        "Strong analytical and problem-solving skills", 
        "Adaptability in learning new technologies",
        "Collaboration and teamwork experience", 
        "Attention to detail in writing clean code", 
        "Effective time management and multitasking"
    ]

    for strength in strengths:
        c.setFont("Times-Roman", 12)
        c.drawString(x + 20, y, f"- {strength}")
        y -= 15
        y = check_page_space(c, y, 40, letter[1])

    y -= 20
    draw_line(c, x, y, letter[0])
    return y - 20

def draw_skills_section(c, x, y, width):
    c.setFont("Times-Bold", 14)
    c.drawString(x, y, "Core Skills:")
    y -= 20

    column_count = 4  
    column_width = (width - 80) // column_count  
    row_height = 20  
    rows_needed = (len(skills) + column_count - 1) // column_count  

    for row in range(rows_needed):
        for col in range(column_count):
            index = row + col * rows_needed  
            if index < len(skills):
                c.drawString(x + col * column_width, y, f"\u2022 {skills[index]}")
        y -= row_height  

    y -= row_height  
    draw_line(c, x, y, width)
    return y - 20

def draw_languages_section(c, x, y):
    c.setFont("Times-Bold", 14)
    c.drawString(x, y, "Languages:")
    y -= 15
    c.setFont("Times-Roman", 12)
    c.drawString(x + 20, y, "English (Excellent), Tamil (Excellent)")
    y -= 30
    draw_line(c, x, y, letter[0])
    return y - 20

def draw_education_section(c, x, y):
    
    y = check_page_space(c, y, 160, letter[1])  

    
    c.setFont("Times-Bold", 14)
    c.drawString(x, y, "Education:")
    y -= 20  

    education = [
        ("Besant Technologies", "Jul 2023 - Dec 2024", 
         "Besant Technologies is an EdTech company that offers IT software training and "
         "placement services in India. Successfully completed a Full Stack Python course at "
         "Besant Technologies, gaining practical experience in HTML, CSS, JavaScript, Python, "
         "Django, and MySQL for building scalable software solutions."),
        ("Anna University College of Engineering", "Aug 2019 - Aug 2023", 
         "Bachelor of Engineering | Computer Science Engineering"),
        ("Bharani Park Matriculation Higher Secondary School", "Jan 2018 - Dec 2019", 
         "+2 Higher Secondary School Certificate"),
        ("Bharani Park Matriculation Higher Secondary School", "Jul 2016 - Mar 2017", 
         "Secondary School Certificate")
    ]

    
    max_width = letter[0] - 100

    def draw_text_with_wrap(c, x, y, text, max_width, font_size):
        """Helper function to draw text with word wrapping."""
        c.setFont("Times-Roman", font_size)
        
        words = text.split(' ')
        line = ''
        
        for word in words:
            
            test_line = f"{line} {word}".strip()
            text_width = c.stringWidth(test_line, "Times-Roman", font_size)
            
            if text_width > max_width:
                
                c.drawString(x, y, line)
                y -= 15  
                line = word  
            else:
                line = test_line  
        
        
        if line:
            c.drawString(x, y, line)
            y -= 15  
        
        return y

    
    for institution, duration, qualification in education:
        c.setFont("Times-Bold", 12)
        c.drawString(x + 20, y, f"{institution}  {duration}")
        y -= 15  
        
        
        y = draw_text_with_wrap(c, x + 20, y, qualification, max_width, 12)
        
        
        y -= 10  
        
        
        y = check_page_space(c, y, 40, letter[1])

    
    draw_line(c, x, y, letter[0])
    
    return y - 20  

def draw_certificates_section(c, x, y):
    c.setFont("Times-Bold", 14)
    c.drawString(x, y, "Certificates:")
    y -= 20

    certificates = [
        ("Python", "Oct 2023", "HackerRank"),
        ("JavaScript", "Sep 2023", "HackerRank"),
        ("SQL", "Oct 2023", "HackerRank")
    ]

    for cert, date, provider in certificates:
        c.setFont("Times-Bold", 12)
        c.drawString(x + 20, y, f"{cert}  {date}")
        y -= 15
        c.setFont("Times-Roman", 12)
        c.drawString(x + 20, y, provider)
        y -= 30
        y = check_page_space(c, y, 40, letter[1])

    draw_line(c, x, y, letter[0])
    return y - 20

def draw_interests_section(c, x, y):
    c.setFont("Times-Bold", 14)
    c.drawString(x, y, "Interests:")
    y -= 15
    c.setFont("Times-Roman", 12)
    c.drawString(x + 20, y, "Cooking, Games, Anime")
    return y - 30


def create_pdf(filename):
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    x, y = 40, height - 40  

    y = draw_personal_section(c, x, y)
    y = draw_professional_summary(c, x, y)
    y = draw_projects_section(c, x, y)
    y = draw_strengths_section(c, x, y)
    y = draw_skills_section(c, x, y, width)
    y = draw_education_section(c, x, y)
    y = draw_languages_section(c, x, y)
    y = draw_certificates_section(c, x, y)
    y = draw_interests_section(c, x, y)

    c.save()

