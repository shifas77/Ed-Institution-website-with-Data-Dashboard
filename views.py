"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib import messages






from distutils.command import upload
from random import Random
from django.shortcuts import render, redirect 
from django.http import HttpRequest
from app.forms import studentform, student_stat
from app.forms import admin_loginform
from django.views.generic import TemplateView
from app.forms import EmployeeForm
from app.forms import HigherEDform
from app.forms import CSelectionform
from app.models import course_selection
from app.models import student,admin_login,UploadImage,student_stat,Final_HS
from app.forms import FinalHSform
from app.forms import UserImageForm
from datetime import date
import pandas as pd
import ast
import sqlite3




def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )


def Display(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Dispalystat.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def stud_detail(request):
 
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/student_home.html',
        {'form': studentform}
    )




def get_admin_data():
    queryset = admin_login.objects.all()
    return queryset

def get_student_data():
    queryset = student.objects.all()
    return queryset

def get_stat_col_data():
    queryset = student_stat.objects.all()
    return queryset

import pandas as pd
from django.db import connection
import matplotlib.pyplot as plt
import io
import base64
import seaborn as sns
import os

import seaborn as sns

import seaborn as sns

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#def get_stat_data():
#    with connection.cursor() as cursor:
#        cursor.execute("SELECT * FROM student_stat")
#        columns = [col[0] for col in cursor.description]
#        rows = cursor.fetchall()
#        dataframe = pd.DataFrame(rows, columns=columns)

#    # Set the style to a modern theme
#    sns.set_style("whitegrid")

#    # Generate the bar plot for Column 1
#    plt.figure(figsize=(8, 6))
#    sns.countplot(data=dataframe, x='color', palette='pastel')
#    plt.title('Color Preference', fontsize=14, fontweight='bold')
#    plt.xlabel('Colors', fontsize=12)
#    plt.ylabel('Count', fontsize=12)
#    plt.savefig("C:/Users/user/source/repos/DjangoWebProject8/DjangoWebProject8/app/static/plot1.png")

#    # Generate the pie chart for Column 1
#    plt.figure(figsize=(8, 6))
#    color_counts = dataframe['color'].value_counts()
#    plt.pie(color_counts, labels=color_counts.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'))
#    plt.title('Color Preference', fontsize=14, fontweight='bold')
#    plt.legend(title='Colors', loc='center left', bbox_to_anchor=(1, 0.5))
#    plt.savefig("C:/Users/user/source/repos/DjangoWebProject8/DjangoWebProject8/app/static/pie1.png")

#    # Generate the bar plot for Column 2
#    plt.figure(figsize=(8, 6))
#    sns.countplot(data=dataframe, x='animal', palette='pastel')
#    plt.title('Animal Preference', fontsize=14, fontweight='bold')
#    plt.xlabel('Animals', fontsize=12)
#    plt.ylabel('Count', fontsize=12)
#    plt.savefig("C:/Users/user/source/repos/DjangoWebProject8/DjangoWebProject8/app/static/plot2.png")

#    # Generate the pie chart for Column 2
#    plt.figure(figsize=(8, 6))
#    animal_counts = dataframe['animal'].value_counts()
#    plt.pie(animal_counts, labels=animal_counts.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'))
#    plt.title('Animal Preference', fontsize=14, fontweight='bold')
#    plt.legend(title='Animals', loc='center left', bbox_to_anchor=(1, 0.5))
#    plt.savefig("C:/Users/user/source/repos/DjangoWebProject8/DjangoWebProject8/app/static/pie2.png")

#    # Generate the bar plot for Column 3
#    plt.figure(figsize=(8, 6))
#    sns.countplot(data=dataframe, x='activity', palette='pastel')
#    plt.title('Activity Preference', fontsize=14, fontweight='bold')
#    plt.xlabel('Activities', fontsize=12)
#    plt.ylabel('Count', fontsize=12)
#    plt.savefig("C:/Users/user/source/repos/DjangoWebProject8/DjangoWebProject8/app/static/plot3.png")

#    # Generate the pie chart for Column 3
#    plt.figure(figsize=(8, 6))
#    activity_counts = dataframe['activity'].value_counts()
#    plt.pie(activity_counts, labels=activity_counts.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'))
#    plt.title('Activity Preference', fontsize=14, fontweight='bold')
#    plt.legend(title='Activities', loc='center left', bbox_to_anchor=(1, 0.5))
#    plt.savefig("C:/Users/user/source/repos/DjangoWebProject8/DjangoWebProject8/app/static/pie3.png")



#get_stat_data()






def login(request):
    if request.method == "POST":
        username=request.POST.get('uname') 
        password=request.POST.get('pswd') 
        admin_data = get_admin_data()
      
        if (1 in ([1 if (stack.uname == username and stack.pswd==password) else 0 for stack in admin_data])):
             return render(request,'app/Student_all.html')
        else:
             return render(request,'app/login.html',{'form': admin_loginform( request.POST)})
    else:  
           
        form =  admin_loginform( request.POST)  
        return render(request,'app/login.html',{'form': form})





def Slogin(request):
    if request.method == "POST":

        form = studentform(request.POST)
        username = request.POST.get('uname')
        password = request.POST.get('pswd')
        student_data = get_student_data()
        print(username)
        print(password)
        print(student_data[0].uname)
        print(student_data[0].pswd)
        print([1 if (stack.uname == username and stack.pswd==password) else 0 for stack in student_data])
        if (1 in [1 if (stack.uname == username and stack.pswd==password) else 0 for stack in student_data]):
            # Authentication successful, create session for the user
            print("shifas")
            request.session['username'] = username
            return redirect('profile')  # Redirect to the profile view
        else:
            # Authentication failed
            messages.error(request, 'Invalid username or password.')
            return render(request, 'app/Studentlogin.html', {'form': form})
    else:
        form = studentform()
        return render(request, 'app/Studentlogin.html', {'form': form})





def student_reg(request):  
    if request.method == "POST":  
        form =  studentform( request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return render(request,'app/Student_home.html',{'form': form})
            except:  
                pass 
    else:  
        form = studentform( request.POST)
    return render(request,'app/Student_home.html',{'form': form})

def question(request):  
    if request.method == "POST":  
        form =  student_stat( request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return render(request,'app/Studentlogin.html',{'form': studentform( request.POST)})
            except:  
                pass 
    else:  
        form = student_stat( request.POST)
    return render(request,'app/question.html',{'form': form})






from django.shortcuts import render
import pandas as pd
from django.db import connection

def Course(request):
    # Retrieve the data from the database
    data = student.objects.all()

    # Extract the column names
    columns = data[0]._meta.get_fields()
    print(columns)
    # Extract the row values
    Elim=((pd.DataFrame([[getattr(record, column.name) for column in Final_HS.objects.all()[0]._meta.get_fields()] for record in Final_HS.objects.all()])).iloc[:, 0]).tolist()
    rows = [ows for ows in [[getattr(record, column.name) for column in columns] for record in data] if ows[0] not in Elim ]
    print(Elim)
    print(rows)
    
    # Add the extra column name
    columns_with_extra = columns + ('Course',)

    # Iterate over the rows and add an empty value to the extra column
    for row in rows:
        row.append('')

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM hs_table")
        columns_D = [col[0] for col in cursor.description]
        ows = cursor.fetchall()
        dataframe = pd.DataFrame(ows, columns=columns_D)
        options=(dataframe.head(1)).values.tolist()
        extra="Not Specified"
        names=[extra]+options[0]+(dataframe.iloc[1]).values.tolist()
        unames=['UG','PG',1,2]
        filtered_names = [name for name in names if name not in unames]
        

    # Render the template with the data
    return render(request, 'app/Course_Selection.html', {'columns': columns_with_extra, 'rows': rows,'options':filtered_names})



from django.http import HttpResponse

def confirmSelection(request):
    if request.method == "POST":
        selected_options = request.body.decode('utf-8')
        
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM studenttb WHERE id NOT IN (SELECT id FROM Final_HS);")
            columns_D = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            dataframe = pd.DataFrame(rows, columns=columns_D)
            names = ast.literal_eval(selected_options)
            dataframe['Course'] = names

            # Extract the column names
            columns = dataframe.columns.tolist()

            # Extract the updated rows
            updated_rows = dataframe.values.tolist()

            # Connect to the SQLite database
            conn = sqlite3.connect('db6.sqlite3')
            cursor = conn.cursor()

            # Delete all rows from the table
            cursor.execute("DELETE FROM course_selection")

            # Save the rows and columns to a DataFrame
            df_updated = pd.DataFrame(updated_rows, columns=columns)

            # Save the DataFrame to the "course_selection" table in the database
            df_updated.to_sql('course_selection', conn, if_exists='append', index=False)

            # Commit the changes and close the cursor
            conn.commit()
            cursor.close()

            # Close the database connection
            conn.close()

            return HttpResponse(status=200)






def Next(request):
    

    # Establish a connection to the SQLite database
    conn = sqlite3.connect('db6.sqlite3')

    # Create a cursor object
    cursor = conn.cursor()

    # Write the SQL query with the JOIN clause and specify the desired columns
	
    query = '''
        SELECT course_selection.id, course_selection.eid, course_selection.uname, course_selection.Course
        FROM course_selection
        WHERE course_selection.Course <> "Not Specified";
    
    
    '''

    # Execute the query
    cursor.execute(query)

    # Fetch the results
    rows = cursor.fetchall()

    # Get the column names
    columns = [description[0] for description in cursor.description]

    # Close the cursor and the connection
    cursor.close()
    conn.close()

    # Render the template with the table data and column headers
    return render(request, 'app/Course_Final.html', {'columns': columns, 'rows': rows})



def DBS(request):
    # Establish a connection to the database
    conn = sqlite3.connect('db6.sqlite3')
    cursor = conn.cursor()

    # Execute the query to fetch the desired data
    query = '''
        SELECT course_selection.id, course_selection.eid, course_selection.uname, course_selection.Course
        FROM course_selection
        WHERE course_selection.Course <> "Not Specified";
    '''
    cursor.execute(query)

    # Fetch the results
    rows = cursor.fetchall()

    # Append the fetched rows to the existing table
    insert_query = "INSERT INTO Final_HS (id, eid, uname, Course) VALUES (?, ?, ?, ?)"
    cursor.executemany(insert_query, rows)
    conn.commit()

    # Close the connection
    conn.close()

    return HttpResponse("Data saved to the database successfully.")


def Presentation(request):
    # Establish a connection to the SQLite database
    conn = sqlite3.connect('db6.sqlite3')

    # Create a cursor object
    cursor = conn.cursor()

    # Write the SQL query with the JOIN clause and specify the desired columns
    query = '''
    SELECT Final_HS.id,Final_HS.eid,Final_HS.uname, studenttb.mno,Final_HS.Course
    FROM Final_HS
    INNER JOIN studenttb ON Final_HS.id = studenttb.id;


 
    '''

    # Execute the query
    cursor.execute(query)

    # Fetch the results
    rows = cursor.fetchall()

    # Get the column names
    columns = [description[0] for description in cursor.description]

    # Close the cursor and the connection
    cursor.close()
    conn.close()

    return render(request, 'app/Candidate_Info.html', {'columns': columns, 'rows': rows})






def Profile(request):

    # Use the username or perform further operations with session data
    username_s = request.session.get('username')

    # Establish a connection to the SQLite database
    conn = sqlite3.connect('db6.sqlite3')

    # Create a cursor object
    cursor = conn.cursor()

    # Write the SQL query with the JOIN clause and specify the desired columns
    query = '''
    SELECT Final_HS.id,Final_HS.eid,Final_HS.uname, studenttb.mno,Final_HS.Course
    FROM Final_HS
    INNER JOIN studenttb ON Final_HS.id = studenttb.id;


 
    '''

    # Execute the query
    cursor.execute(query)

    # Fetch the results
    rows = cursor.fetchall()
    rows=[ows for ows in rows if ows[2] == username_s]
    print(rows)

    # Get the column names
    columns = [description[0] for description in cursor.description]

    # Close the cursor and the connection
    cursor.close()
    conn.close()
    profile_url = username_s +".jpg"
    

    #Image exists:# Get the directory path where the image is stored
    image_directory = 'C:\\Users\\user\\source\\repos\\DjangoWebProject8\\DjangoWebProject8\\app\\static'
    # Get the list of files in the directory
    files = os.listdir(image_directory)
    # Check if the directory exists
    if any(file==profile_url  for file in files):
        image_exists = True


    else:
        # Directory does not exist, image does not exist
        image_exists = False



   
    return render(request, 'app/Profile.html', {'columns': columns, 'rows_values': rows, 'image_exists': image_exists,'profile_url': profile_url})



from django.shortcuts import render

def upload_profile_photo(request):
    username_s = request.session.get('username')
    if request.method == 'POST':
        # Get the uploaded file
        profile_photo = request.FILES.get('profile_photo')

        # Handle the file validation and saving logic
        # (e.g., check file type, size, save to the server or database)

        # Example: Save the file to the server (media/uploads folder)
        if profile_photo:
            # Assuming you have a "uploads" folder in your media directory
            path = 'static/' + username_s +".jpg"
            with open('app/' + path, 'wb') as f:
                for chunk in profile_photo.chunks():
                    f.write(chunk)

            # Optionally, you can save the file path to the user's profile
            # profile.photo = path
            # profile.save()

        # Redirect or render a response
        # Example: Redirect back to the profile page
        return redirect('profile')

    # Handle GET requests or render a form if needed
    # Example: Render a template with a form to upload the profile photo
    return redirect('profile')


