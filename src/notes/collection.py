from __init__ import Note
from datetime import datetime
import csv

notes = []

def load_notes(file):
    with open(file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['id'] != 'id':
                note = Note(row['id'], row['title'], row['body'], row['date'])
                notes.append(note)
        return

def save_notes(file):
    with open(file, 'w', newline='') as f:
        for note in notes:
            fieldnames = ['id', 'title', 'body', 'date']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'id': note.id, 'title': note.title, 'body': note.body, 'date': note.date})
    print()
    print('...changes saved...')
    print()

def max_id(file):
    load_notes(file)
    max_id = 0
    id_arr = []
    for note in notes:
        id_arr.append(note.id)
    return max(id_arr)

def add_note(file, title, body):
    x = max_id(file)
    id = int(x)+1
    date = datetime.now().strftime("%Y-%m-%d")
    note = Note(id, title, body, date)
    notes.append(note)

def print_notes(file):
    load_notes(file)
    if len(notes) == 0:
        print()
        print('Notes not found')
    else:
        for note in notes:
            print(f"ID: {note.id}")
            print(f"   Title: {note.title}")
            print(f"   Body: {note.body}")
            print(f"   Date: {note.date}")

def edit_note(file, id, new_title, new_body):
    try:
        load_notes(file)
        for note in notes:
            if note.id == id:
                note.title = new_title
                note.body = new_body
                note.date = datetime.now().strftime("%Y-%m-%d")
                return
        print()
    except KeyError:
        print('"ID" not found.')

def delete_note(file, id):
    try:
        load_notes(file)
        for note in notes:
            if note.id == id:
                notes.remove(note)
                save_notes(file)
        print()
    except KeyError:
        print('"ID" not found.')

def selection_by_date(file, date):
    try:
        load_notes(file)
        if len(notes) == 0:
            print()
            print('Notes not found')
        else:
            for note in notes:
                if note.date == date:
                    print()
                    print(f"ID: {note.id}")
                    print(f"   Title: {note.title}")
                    print(f"   Body: {note.body}")
                    print(f"   Date: {note.date}")   
    except KeyError:
        print('"Date" not found.')

def start_app(file):
    try:
        while True:
            print()
            print('1 - Show notes.')
            print('2 - Add a note')
            print('3 - Edit a note')
            print('4 - Delete a note')
            print('5 - Selection by date')
            print('6 - Exit')
            print()
            choise = input('Select an action:  ')
            print()
            if choise == '1':
                print_notes(file)
            elif choise == '2':
                title = input('Enter the title:  ')
                body = input('Enter the text:  ')
                print()
                add_note(file, title, body)
                save_notes(file)
            elif choise == '3':
                id = input("Enter note's ID for edit:  ")
                title = input('Enter the new title:  ')
                body = input("Enter the note's new text:  ")
                print()
                edit_note(file, id, title, body)
                save_notes(file)
            elif choise == '4':
                id = input("Enter note's ID for delete:  ")
                delete_note(file, id)
            elif choise == '5':
                date = datetime(int(input("year:  ")), int(input("month:  ")), int(input("day:  "))).strftime("%Y-%m-%d")
                selection_by_date(file, date) 
            elif choise == '6':
                break
            else :
                print('Try again, the input was incorrect.')
    except  FileNotFoundError:
        print()
        print('File Not Found')
        

