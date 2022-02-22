# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 10:08:40 2022

@author: david
"""

import csv

with open('wordle_list_nyt.csv') as csvfile:
    wordle_list = list(csv.reader(csvfile))[0]

# Define variables
global program_running
global orange_letter, orange_pos
global green_letter, green_pos

wordle_list_reduced = []

wordle_list_reduced = wordle_list[:]

# Define functions
# Function to remove words with orange letters
def Orange(letter, pos):
    for i in wordle_list_reduced:
        if i[pos] == letter:
            try:
                wordle_list_reduced.remove(i)
            except:
                continue
    return wordle_list_reduced

# Function to remove words without green letters
def Green(letter, pos):
    for i in wordle_list:
        if i[pos] != letter:
            try:
                wordle_list_reduced.remove(i)
            except:
                continue
    return wordle_list_reduced

# Function to remove words with grey letters
def Grey(letter):
    for i in wordle_list:
        if letter in i:
            try:
                wordle_list_reduced.remove(i)
            except:
                continue
    return wordle_list_reduced

# Function to iterate through input of grey letters
def Remove_Grey(grey_letters):
    for j in grey_letters:
        Grey(j)
        wordle_list = wordle_list_reduced[:]
    return wordle_list_reduced

# Main function
def main_function():
    program_running=""
    print("Let's figure out your Wordle.")
    print("==============================")
    while program_running != "y":
        
        #Greys
        print("Firstly, enter any 'grey' letters. (If none, type 'none'):")
        grey_letters = input()
        if grey_letters != "none":
            Remove_Grey(grey_letters)
        elif grey_letters == "none":
            continue
        print("==============================")    
        #Oranges
        orange = "y"
        while orange == "y":
            print("Enter an orange letter (if none, type 'none'):")
            orange_letter = input()
            if orange_letter != "none":
                print("Ok, what position is that letter in?:")
                orange_pos = input()
                orange_pos= int(orange_pos)
                Orange(orange_letter, orange_pos)
            elif orange_letter == "none":
                break
            print("==============================")
            print("Any more oranges? y/n:")
            orange = input()
        print("==============================")
        #Greens
        green = "y"
        while green == "y":
            print("Enter a green letter (if none, type 'none'):")
            green_letter = input()
            if green_letter != "none":
                print("Ok, what position is that letter in?:")
                green_pos = input()
                green_pos = int(green_pos)
                Green(green_letter, green_pos)
            elif green_letter == "none":
                break
            print("==============================")
            print("Any more greens? y/n:")
            green = input()            
        
        print(len(wordle_list_reduced))
        print("==============================")
        view = ""
        print("View Wordle list? y/n:")
        print("==============================")
        view = input()
        if view == "y":
            print(wordle_list_reduced)
        else:
            continue
        print("Stop process? y/n:")
        program_running = input()

main_function()
