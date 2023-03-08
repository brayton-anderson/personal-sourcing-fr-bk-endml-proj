from . import db
from website.models import (
    Skill,
    Roles,
    Workavailability,
    Educationlevel,
    Competency,
    Languagepro,
    Programinglanguage,
    Framework,
)


class Insertdata:
    def insert_language_data():
        data = [
            {
                "title": "Great",
                "details": "Both U.S. engineering managers and I can easily understand each other without having to repeat much.",
            },
            {
                "title": "Average",
                "details": "I can communicate with a U.S. engineering managers if we both speak slowly and occasionally repeat sentences that the other person did not understand.",
            },
            {
                "title": "Basic",
                "details": "I can only communicate in written form over email or Slack effectively. Verbal commumication in english with a U.S. manager would be slow and impractical.",
            },
        ]
        db.session.bulk_insert_mappings(Languagepro, data)
        db.session.commit()
        return "Data inserted successfully"

    def insert_competency_data():
        data = [
            {
                "title": "Beginner",
                "details": "I do not have any proffecional experience in this skill.",
            },
            {
                "title": "Experienced",
                "details": "I have used this skill proffecionally on a limited capacity.",
            },
            {
                "title": "Advanced",
                "details": "I have used this skill proffecionally at least once per week. (example: while deploying).",
            },
            {
                "title": "Expert",
                "details": "I have used this skill proffecionally on a daily basis.",
            },
        ]
        db.session.bulk_insert_mappings(Competency, data)
        db.session.commit()
        return "Data inserted successfully"

    def insert_educationlevel_data():
        data = [
            {
                "title": "Bachelors (or equivalent)",
                "details": "I do not have any proffecional experience in this skill.",
            },
            {
                "title": "Doctorate (or equivalent)",
                "details": "I have used this skill proffecionally on a limited capacity.",
            },
            {
                "title": "MBA (or equivalent)",
                "details": "I have used this skill proffecionally at least once per week. (example: while deploying).",
            },
            {
                "title": "Masters (or equivalent)",
                "details": "I have used this skill proffecionally on a daily basis.",
            },
            {
                "title": "Secondary/Highschool (or equivalent)",
                "details": "I have used this skill proffecionally on a daily basis.",
            },
            {
                "title": "Other degree",
                "details": "I have used this skill proffecionally on a daily basis.",
            },
        ]
        db.session.bulk_insert_mappings(Educationlevel, data)
        db.session.commit()
        return "Data inserted successfully"

    def insert_workavailability_data():
        data = [
            {
                "title": "Ready to Interview",
                "details": "I am actively looking for a new remote software job.",
            },
            {
                "title": "Open to Offers",
                "details": "I am not actively looking for a new remote software job, but I am available to hear about new job opportunities for the next 30 days.",
            },
            {
                "title": "Unavailable for Jobs",
                "details": "I am not looking for a new remote software job at the moment.",
            },
        ]
        db.session.bulk_insert_mappings(Workavailability, data)
        db.session.commit()
        return "Data inserted successfully"

    def insert_roles_data():
        data = [
            {"title": "Web Frontend", "details": "I am "},
            {"title": "Web Backend", "details": "I am "},
            {"title": "Fullstack (BE-Heavy)", "details": "I am "},
            {"title": "Fullstack (FE-Heavy)", "details": "I am "},
            {"title": "Mobile", "details": "I am "},
            {"title": "Machine Learning", "details": "I am "},
            {"title": "Dev Ops", "details": "I am "},
            {"title": "Cloud - Security", "details": "I am "},
            {"title": "Cloud - Networking", "details": "I am "},
            {"title": "Cloud - Solutions Architecture", "details": "I am "},
            {"title": "Cloud - Data", "details": "I am "},
            {"title": "Cloud - AI/ML", "details": "I am "},
            {"title": "Other", "details": "I am "},
        ]
        db.session.bulk_insert_mappings(Roles, data)
        db.session.commit()
        return "Data inserted successfully"

    def insert_skills_data():
        data = [
            {"title": "React + Node", "category": "Fullstack", "details": "I am "},
            {
                "title": "React (Frontend Only)",
                "category": "Frontend",
                "details": "I am ",
            },
            {"title": "React + Backend", "category": "Fullstack", "details": "I am "},
            {"title": "React Native", "category": "Fullstack", "details": "I am "},
            {
                "title": "Ruby on Rails (Full-Stack)",
                "category": "Fullstack",
                "details": "I am ",
            },
            {
                "title": "Ruby on Rails (Backend)",
                "category": "Backend",
                "details": "I am ",
            },
            {"title": "Python (Django)", "category": "Frontend", "details": "I am "},
            {"title": "Python + React", "category": "Fullstack", "details": "I am "},
            {
                "title": "Python (Flask/Vue/Angular)",
                "category": "Fullstack",
                "details": "I am ",
            },
            {
                "title": "Python (Backend Only)",
                "category": "Backend",
                "details": "I am ",
            },
            {"title": "Angular + Backend", "category": "Fullstack", "details": "I am "},
            {"title": "PHP + Laravel", "category": "Fullstack", "details": "I am "},
            {"title": "Android (Kotlin)", "category": "Mobile", "details": "I am "},
            {"title": "Vue + Backend", "category": "Fullstack", "details": "I am "},
            {"title": "Golang + Frontend", "category": "Fullstack", "details": "I am "},
            {"title": "iOS Swift", "category": "Mobile", "details": "I am "},
            {"title": "Flutter", "category": "Frontend", "details": "I am "},
            {"title": "DevOps + AWS", "category": "DevOps", "details": "I am "},
            {
                "title": "Machine Learning/Data Science",
                "category": "Machine Learning",
                "details": "I am ",
            },
            {
                "title": "Data Engineering (+Python)",
                "category": "Data Engineering",
                "details": "I am ",
            },
            {"title": "C# / .NET", "category": "Fullstack", "details": "I am "},
            {
                "title": "DevOps + Google Cloud Platform",
                "category": "Fullstack",
                "details": "I am ",
            },
            {"title": "DevOps + Azure", "category": "Fullstack", "details": "I am "},
            {
                "title": "Data Engineer + AWS",
                "category": "Fullstack",
                "details": "I am ",
            },
            {
                "title": "Data Engineer + Google Cloud Platform",
                "category": "Fullstack",
                "details": "I am ",
            },
            {"title": "Salesforce", "category": "DevOps", "details": "I am "},
            {"title": "DevOps Cloud", "category": "DevOps", "details": "I am "},
            {
                "title": "Cloud Security + AWS",
                "category": "Data Engineering",
                "details": "I am ",
            },
            {
                "title": "Cloud Security + GCP",
                "category": "Data Engineering",
                "details": "I am ",
            },
            {"title": "Other (please specify)", "category": "", "details": "I am "},
        ]
        db.session.bulk_insert_mappings(Skill, data)
        db.session.commit()
        return "Data inserted successfully"

    def insert_programinglanguages_data():
        data = [
            {
                "title": "HTML",
                "category": "Frontend",
                "details": "Hypertext Markup Language",
            },
            {
                "title": "CSS",
                "category": "Frontend",
                "details": "Cascading Style Sheets",
            },
            {
                "title": "JavaScript",
                "category": "Frontend",
                "details": "JavaScript, often abbreviated as JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.",
            },
            {
                "title": "TypeScript",
                "category": "Frontend",
                "details": "TypeScript is a free and open source high-level programming language developed and maintained by Microsoft.",
            },
            {
                "title": "Dart",
                "category": "Frontend",
                "details": "Dart is a client-optimized language for fast apps on any platform.",
            },
            {
                "title": "Elm",
                "category": "Frontend",
                "details": "Elm is a domain-specific programming language for declaratively creating web browser-based graphical user interfaces.",
            },
            {
                "title": "Haml",
                "category": "Frontend",
                "details": "Haml is a templating system that is designed to avoid writing inline code in a web document and make the HTML cleaner",
            },
            {
                "title": "Pug",
                "category": "Frontend",
                "details": "Pugs is a compiler and interpreter for the Raku programming language, started on February 1, 2005, by Audrey Tang.",
            },
            {
                "title": "CoffeeScript",
                "category": "Frontend",
                "details": "CoffeeScript is a little language that compiles into JavaScript. Underneath that awkward Java-esque patina, JavaScript has always had a gorgeous heart.",
            },
            {
                "title": "Handlebars",
                "category": "Frontend",
                "details": "Handlebars compiles templates into JavaScript functions. This makes the template execution faster than most other template engines.",
            },
            {
                "title": "Java",
                "category": "Backend",
                "details": "Java is a high-level, class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible.",
            },
            {
                "title": "Python",
                "category": "Backend",
                "details": "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.",
            },
            {
                "title": "Ruby",
                "category": "Backend",
                "details": "Ruby is an interpreted, high-level, general-purpose programming language which supports multiple programming paradigms.",
            },
            {
                "title": "PHP",
                "category": "Backend",
                "details": "PHP is a general-purpose scripting language geared toward web development.",
            },
            {
                "title": "Node.js",
                "category": "Backend",
                "details": "Node.js® is a JavaScript runtime built on Chromes V8 JavaScript engine.",
            },
            {
                "title": "Go",
                "category": "Backend",
                "details": "Go is an open source programming language that makes it simple to build secure, scalable systems.",
            },
            {
                "title": "Rust",
                "category": "Backend",
                "details": "Rust is a multi-paradigm, high-level, general-purpose programming language. Rust emphasizes performance, type safety, and concurrency.",
            },
            {
                "title": "C#",
                "category": "Backend",
                "details": "C# is a general-purpose high-level programming language supporting multiple paradigms. C# encompasses static typing, strong typing, lexically scoped, imperative, declarative, functional, generic, object-oriented, and component-oriented programming disciplines.",
            },
            {
                "title": "Kotlin",
                "category": "Backend",
                "details": "Kotlin is a cross-platform, statically typed, general-purpose high-level programming language with type inference. Kotlin is designed to interoperate fully with Java, and the JVM version of Kotlins standard library depends on the Java Class Library, but type inference allows its syntax to be more concise.",
            },
            {
                "title": "Swift",
                "category": "Backend",
                "details": "The Society for Worldwide Interbank Financial Telecommunication, legally S.W.I.F.T. SC, is a Belgian cooperative society providing services related to the execution of financial transactions and payments between banks worldwide.",
            },
            {
                "title": "Perl",
                "category": "Backend",
                "details": 'Perl is a family of two high-level, general-purpose, interpreted, dynamic programming languages. "Perl" refers to Perl 5, but from 2000 to 2019 it also referred to its redesigned "sister language", Perl 6, before the latters name was officially changed to Raku in October 2019.',
            },
            {
                "title": "Scala",
                "category": "Backend",
                "details": "Scala is a strong statically typed high-level general-purpose programming language that supports both object-oriented programming and functional programming. Designed to be concise, many of Scalas design decisions are aimed to address criticisms of Java.",
            },
            {
                "title": "Haskell",
                "category": "Backend",
                "details": "Haskell is a general-purpose, statically-typed, purely functional programming language with type inference and lazy evaluation.",
            },
        ]
        db.session.bulk_insert_mappings(Programinglanguage, data)
        db.session.commit()
        return "Data inserted successfully"

    def insert_frameworks_data():
        data = [
            {
                "title": "React",
                "pl_id": "3",
                "category": "Frontend",
                "details": "React is a free and open-source front-end JavaScript library for building user interfaces based on components.",
            },
            {
                "title": "Angular",
                "pl_id": "3",
                "category": "Frontend",
                "details": "Angular is a TypeScript-based, free and open-source web application framework led by the Angular Team at Google and by a community of individuals and corporations.",
            },
            {
                "title": "Vue.js",
                "pl_id": "3",
                "category": "Frontend",
                "details": "Vue.js is an open-source model–view–viewmodel front end JavaScript framework for building user interfaces and single-page applications.",
            },
            {
                "title": "Ember.js",
                "pl_id": "3",
                "category": "Frontend",
                "details": "Ember.js is an open-source JavaScript web framework that utilizes a component-service pattern.",
            },
            {
                "title": "Backbone.js",
                "pl_id": "3",
                "category": "Frontend",
                "details": "Backbone.js is a JavaScript rich-client web app framework based on the model–view–controller design paradigm, intended to connect to an API over a RESTful JSON interface.",
            },
            {
                "title": "Svelte",
                "pl_id": "3",
                "category": "Frontend",
                "details": "Svelte is a free and open-source front end component framework or language created by Rich Harris and maintained by the Svelte core team members.",
            },
            {
                "title": "Flutter",
                "pl_id": "3",
                "category": "Frontend",
                "details": "Flutter is an open-source UI software development kit created by Google. It is used to develop cross-platform applications for Android, iOS, Linux, macOS, Windows, Google Fuchsia, and the web from a single codebase.",
            },
            {
                "title": "React",
                "pl_id": "4",
                "category": "Frontend",
                "details": "React is a free and open-source front-end JavaScript library for building user interfaces based on components.",
            },
            {
                "title": "Angular",
                "pl_id": "4",
                "category": "Frontend",
                "details": "Angular is a TypeScript-based, free and open-source web application framework led by the Angular Team at Google and by a community of individuals and corporations.",
            },
            {
                "title": "Vue.js",
                "pl_id": "4",
                "category": "Frontend",
                "details": "Vue.js is an open-source model–view–viewmodel front end JavaScript framework for building user interfaces and single-page applications.",
            },
            {
                "title": "NestJS",
                "pl_id": "4",
                "category": "Frontend",
                "details": "Nest. JS is a framework that helps build Node. JS server-side applications. The Nest framework is built using TypeScript which allows developers to build highly scalable and testable applications.",
            },
            {
                "title": "Flutter",
                "pl_id": "5",
                "category": "Frontend",
                "details": "Flutter is an open-source UI software development kit created by Google. It is used to develop cross-platform applications for Android, iOS, Linux, macOS, Windows, Google Fuchsia, and the web from a single codebase.",
            },
            {
                "title": "Spring",
                "pl_id": "11",
                "category": "Backend",
                "details": "The Spring Framework is an application framework and inversion of control container for the Java platform.",
            },
            {
                "title": "Django",
                "pl_id": "12",
                "category": "Backend",
                "details": "Django is a free and open-source, Python-based web framework that follows the model–template–views architectural pattern.",
            },
            {
                "title": "Flask",
                "pl_id": "12",
                "category": "Backend",
                "details": "Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.",
            },
            {
                "title": "FastAPI",
                "pl_id": "12",
                "category": "Backend",
                "details": "FastAPI is a Web framework for developing RESTful APIs in Python.",
            },
            {
                "title": "Ruby on Rails",
                "pl_id": "13",
                "category": "Backend",
                "details": "Ruby on Rails is a server-side web application framework written in Ruby under the MIT License.",
            },
            {
                "title": "Laravel",
                "pl_id": "14",
                "category": "Backend",
                "details": "Laravel is a free and open-source PHP web framework, created by Taylor Otwell and intended for the development of web applications following the model–view–controller architectural pattern and based on Symfony.",
            },
            {
                "title": "Symfony",
                "pl_id": "14",
                "category": "Backend",
                "details": "Symfony is a free and open-source PHP web application framework and a set of reusable PHP component libraries.",
            },
            {
                "title": "Express.js",
                "pl_id": "15",
                "category": "Backend",
                "details": "Express.js, or simply Express, is a back end web application framework for building RESTful APIs with Node.js, released as free and open-source software under the MIT License.",
            },
            {
                "title": "Koa.js",
                "pl_id": "15",
                "category": "Backend",
                "details": "Koa is a new web framework designed by the team behind Express, which aims to be a smaller, more expressive, and more robust foundation for web applications.",
            },
            {
                "title": "ASP.NET",
                "pl_id": "18",
                "category": "Backend",
                "details": "ASP.NET is an open-source, server-side web-application framework designed for web development to produce dynamic web pages.",
            },
        ]
        db.session.bulk_insert_mappings(Framework, data)
        db.session.commit()
        return "Data inserted successfully"
