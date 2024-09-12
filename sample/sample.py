class Portfolio:
    def __init__(self):
        self.name = "Subin Das"
        self.profession = "Software Developer"

    def about_me(self):
        about_me_text = "I'm an enthusiastic MSc Computer Science graduate with a solid foundation in web development technologies. I'm eager to apply my academic knowledge to real-world projects, and I'm committed to delivering high-quality results."
        print("About Me:")
        print(about_me_text)
        return about_me_text

portfolio = Portfolio()
portfolio.about_me()

class AboutMe:
    def __init__(self):
        self.education = [
            "Dept. of Computer Science, University of Calicut - MSc Computer Science (2022-2024)",
            "AWH College of Science and Technology - BSc Computer Science (2019-2022)"
        ]
        self.languages_spoken = ["English", "Malayalam", "Hindi", "Tamil"]
        self.languages_written = ["English", "Malayalam", "Hindi"]
        self.hobbies = ["Watching movies, animes, web series", "Playing mobile games", "Reading books and comics"]

    def get_education(self):
        education = self.education
        print("Education:")
        for item in education:
            print(f"- {item}")
        return education

    def get_languages(self):
        languages = {
            'Spoken': self.languages_spoken,
            'Written': self.languages_written
        }
        print("Languages:")
        for lang_type, langs in languages.items():
            print(f"{lang_type}:")
            for lang in langs:
                print(f"- {lang}")
        return languages

    def get_hobbies(self):
        hobbies = self.hobbies
        print("Hobbies:")
        for hobby in hobbies:
            print(f"- {hobby}")
        return hobbies

about_me = AboutMe()
about_me.get_education()
about_me.get_languages()
about_me.get_hobbies()

class Skills:
    def __init__(self):
        self.technical_skills = {
            'Programming': "Python, JavaScript, C Programming",
            'Frontend': "HTML, CSS (Bootstrap)",
            'Backend': "Python (Django), Java, C#, PHP",
            'Database': "MySQL, PostgreSQL",
            'Other Tools': "Git, Linux, AI, ML, NLP"
        }
        self.soft_skills = ["Communication", "Problem Solving", "Adaptability", "Teamwork"]

    def get_technical_skills(self):
        print("Technical Skills:")
        for category, skills in self.technical_skills.items():
            print(f"{category}: {skills}")
        return self.technical_skills

    def get_soft_skills(self):
        print("Soft Skills:")
        for skill in self.soft_skills:
            print(f"- {skill}")
        return self.soft_skills

# Create an instance of the Skills class
skills = Skills()

# Print and get the technical and soft skills
skills.get_technical_skills()
skills.get_soft_skills()

class Projects:
    def __init__(self):
        self.project_1 = {
            'title': "Online Journal Portal for Universities and Colleges (2024)",
            'description': "Simplifies the submission process for authors and editors with a user-friendly flip book format.",
            'frontend': "HTML, CSS, JavaScript, Bootstrap",
            'backend': "Python Django",
            'database': "MySQL"
        }
        self.project_2 = {
            'title': "AR Based Food Menu (2022)",
            'description': "Digital menu accessible via Android app for restaurants, with direct orders to the kitchen.",
            'frontend': "HTML, CSS, JavaScript, Android",
            'backend': "Python Flask",
            'database': "MySQL"
        }
        self.certificates = [
            "AI and NLP - 5 Day Faculty Development program by CUIET and ICFOSS (2024)",
            "Full Stack Development with React and Drupal - 25-hour internship by University of Calicut (2022)"
        ]

    def get_projects(self):
        print("Projects:")
        for project in [self.project_1, self.project_2]:
            print(f"Title: {project['title']}")
            print(f"Description: {project['description']}")
            print(f"Frontend: {project['frontend']}")
            print(f"Backend: {project['backend']}")
            print(f"Database: {project['database']}")
            print()  # Blank line for separation
        return [self.project_1, self.project_2]

    def get_certificates(self):
        print("Certificates:")
        for cert in self.certificates:
            print(f"- {cert}")
        return self.certificates

# Create an instance of the Projects class
projects = Projects()

# Print and get the projects and certificates
projects.get_projects()
projects.get_certificates()

class Contact:
    def __init__(self):
        self.phone = ["+971 522314789", "+91 7594005888"]
        self.email = "subindax@gmail.com"
        self.linkedin = "https://www.linkedin.com/in/subin-das-47495831b"
        self.current_address = "Ajman, UAE"
        self.permanent_address = "Palakkad, Kerala, India"

    def get_contact_details(self):
        contact_details = {
            'Phone': self.phone,
            'Email': self.email,
            'LinkedIn': self.linkedin,
            'Current Address': self.current_address,
            'Permanent Address': self.permanent_address
        }
        print("Contact Details:")
        print("Phone:")
        for number in self.phone:
            print(f"- {number}")
        print(f"Email: {self.email}")
        print(f"LinkedIn: {self.linkedin}")
        print(f"Current Address: {self.current_address}")
        print(f"Permanent Address: {self.permanent_address}")
        return contact_details

# Create an instance of the Contact class
contact = Contact()

# Print and get the contact details
contact.get_contact_details()