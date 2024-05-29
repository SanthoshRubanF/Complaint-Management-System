import tkinter
from tkinter import ttk


window = tkinter.Tk()
window.title("Complaint Management System")

frame = tkinter.Frame(window)
frame.pack()

#User info
user_info_main = tkinter.LabelFrame(frame, text="User Details")
user_info_main.grid(row=0, column=0, sticky="news", padx=50, pady=25)

title_lable = tkinter.Label(user_info_main, text="Title")
title_lable.grid(row=1, column=0)
title_combobox = ttk.Combobox(user_info_main, values=["", "Mr.", "Ms.", "Dr.", "Er."])
title_combobox.grid(row=2, column=0)

name_label1 = tkinter.Label(user_info_main, text="First Name")
name_label1.grid(row=1, column=1)
name_label2 = tkinter.Label(user_info_main, text="Middle Name")
name_label2.grid(row=1, column=2)
name_label3 = tkinter.Label(user_info_main, text="Last Name")
name_label3.grid(row=1, column=3)

name_label1_entry = tkinter.Entry(user_info_main)
name_label1_entry.grid(row=2, column=1)
name_label2_entry = tkinter.Entry(user_info_main)
name_label2_entry.grid(row=2, column=2)
name_label3_entry = tkinter.Entry(user_info_main)
name_label3_entry.grid(row=2, column=3)

age_label = tkinter.Label(user_info_main, text="Age")
age_label.grid(row=3, column=0)
age_spinbox = tkinter.Spinbox(user_info_main, to=100)
age_spinbox.grid(row=4, column=0)

country_label = tkinter.Label(user_info_main, text="Nationality")
country_label.grid(row=3, column=1)
country_combobox = ttk.Combobox(user_info_main, values=["Afghanistan", "Åland Islands", "Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Anguilla", "Antarctica", "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas (the)", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia (Plurinational State of)", "Bonaire, Sint Eustatius and Saba", "Bosnia and Herzegovina", "Botswana", "Bouvet Island", "Brazil",  "Brunei Darussalam", "Bulgaria", "Burkina Faso", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Cayman Islands (the)", "Central African Republic (the)", "Chad", "Chile", "China", "Christmas Island", "Cocos (Keeling) Islands (the)", "Colombia", "Comoros (the)", "Congo (the Democratic Republic of the)", "Congo (the)", "Cook Islands (the)", "Costa Rica", "Curaçao", "Cyprus", "Czechia", "Côte d'Ivoire", "Denmark", "Djibouti", "Dominican Republic (the)", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Falkland Islands (the) [Malvinas]", "Faroe Islands (the)", "Fiji",  "France", "French Polynesia", "French Southern Territories (the)", "Gabon", "Gambia (the)", "Georgia", "Germany", "Ghana", "Gibraltar", "Greece", "Greenland", "Grenada", "Guadeloupe", "Guam", "Guatemala", "Guernsey", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Heard Island and McDonald Islands", "Holy See (the)", "Honduras", "Hong Kong", "Hungary", "Iceland",  "Indonesia",  "Iraq", "Ireland", "Isle of Man", "Israel", "Italy", "India", "Jamaica", "Japan", "Jersey", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea (the Democratic People's Republic of)", "Korea (the Republic of)", "Kuwait", "Kyrgyzstan", "Lao People's Democratic Republic (the)", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macao", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands (the)", "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico", "Micronesia (Federated States of)", "Moldova (the Republic of)", "Monaco", "Mongolia", "Montenegro", "Montserrat", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands (the)", "New Caledonia", "New Zealand", "Nicaragua", "Niger (the)", "Nigeria", "Niue", "Norfolk Island", "Northern Mariana Islands (the)", "Norway", "Oman", "Pakistan", "Palau", "Palestine, State of", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines (the)", "Pitcairn", "Poland", "Portugal", "Puerto Rico", "Qatar", "Republic of North Macedonia", "Romania", "Russian Federation (the)", "Rwanda", "Réunion", "Saint Barthélemy", "Saint Helena, Ascension and Tristan da Cunha", "Saint Kitts and Nevis", "Saint Lucia", "Saint Martin (French part)", "Saint Pierre and Miquelon", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Sint Maarten (Dutch part)", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Georgia and the South Sandwich Islands", "South Sudan", "Spain", "Sri Lanka", "Sudan (the)", "Suriname",  "Sweden", "Switzerland", "Syrian Arab Republic", "Taiwan (Province of China)", "Tajikistan", "Tanzania, United Republic of", "Thailand", "Timor-Leste", "Togo", "Tokelau", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Turks and Caicos Islands (the)", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates (the)", "United Kingdom of Great Britain and Northern Ireland (the)", "United States Minor Outlying Islands (the)", "United States of America (the)", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela (Bolivarian Republic of)", "Viet Nam", "Virgin Islands (British)", "Virgin Islands (U.S.)", "Wallis and Futuna", "Western Sahara", "Yemen", "Zambia", "Zimbabwe"])
country_combobox.grid(row=4, column=1)

sex_label = tkinter.Label(user_info_main, text="Sex")
sex_label.grid(row=3, column=2)
sex_combobox = ttk.Combobox(user_info_main, values=["Male", "Female", "Others"])
sex_combobox.grid(row=4, column=2)

for widget in user_info_main.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Complaints
complaint_data = tkinter.LabelFrame(frame, text="Complaints")
complaint_data.grid(row=1, column=0, sticky="news", padx=50, pady=25)

complaint_write = tkinter.Label(complaint_data, text="Write Your Complaints:-")
complaint_write.grid(row=0, column=0)
complaint_write_entry = tkinter.Entry(complaint_data)
complaint_write_entry.grid(row=0, column=1, sticky="news", ipadx=150, ipady=40)

for widget in complaint_data.winfo_children():
    widget.grid_configure(padx=10, pady=5)

def given_data():
    title = title_combobox.get()
    firstname = name_label1_entry.get()
    middelname = name_label2_entry.get()
    lastname = name_label3_entry.get()
    age = age_spinbox.get()
    sex = sex_combobox.get()
    nationality = country_combobox.get()
    complaint = complaint_write_entry.get()

    print("Title: ", title, "First Name: ", firstname,"Middle Name: ", middelname,"Last Name: ", lastname, "Age: ", age, "Gender: ", sex, "Nationality: ", nationality)
    print("Complaints:- ", complaint)
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")

def list_of_complaint():
    list = [given_data()]

    print(list)

button_list = tkinter.Button(frame, text="List of Complaints", command= list_of_complaint)
button_list.grid(row=2, column=0, sticky="news", padx=10, pady=10)

button = tkinter.Button(frame, text="SUBMIT", command= given_data)
button.grid(row=2, column=1, sticky="news", padx=10, pady=10)


window.mainloop()