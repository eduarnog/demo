## READ ME

# Introduction

This project is a web-based tool that aims to assist users in applying visual identities with the help of generative design. The tool is designed to allow a group of users to input a design system and define the rules by which the tool will generate layout variations. The project was started in 2022, with the creation of a prototype using JavaScript (P5.js) and initial user and market research. The software aims to enable users with less visual design expertise to create visual communication while maintaining brand consistency.

The project is built using Python's Flask framework, and the front-end is developed using Jinja templating. This READ ME file will guide you on how to set up and run the application on your local machine.

## Techstack

• Python 3 as the primary programming language. 
• Flask as the web framework. 
• Jinja templating engine for generating HTML templates. 
• PostgreSQL as the database management system. 
• Alembic for database migrations. 
• HTML, CSS, and JavaScript for the front-end. 
• Gunicorn as the production server. 
• Git for version control. 

### To install the dependencies, run the following command in the terminal:

```bash
pip install -r requirements.txt
```

## Running the Application
To run the application, execute the following command in the terminal:

```bash
python run.py
```

## Viewing the Application

After running the application, open your web browser and navigate to `http://127.0.0.1:5000` to view the home page. The flow of the application is as follows: home page > register > login > dashboard > add content.

### Conclusion

This project is a work in progress, and the login flow presented here is just an exercise exploring some front-end concepts. There are still many good practices to learn regarding front-end development. Please feel free to contribute and share your ideas on how to optimize this code.
