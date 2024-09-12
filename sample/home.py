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