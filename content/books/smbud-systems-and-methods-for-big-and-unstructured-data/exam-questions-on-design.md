---
book_slug: smbud-systems-and-methods-for-big-and-unstructured-data
book_title: SMBUD - Systems and Methods for Big and Unstructured Data
created_at: '2022-01-02T21:33:56.000000Z'
id: 85
priority: 13
slug: exam-questions-on-design
title: Exam questions on design
type: page
updated_at: '2022-01-14T16:11:18.000000Z'
---

# Exam questions on design

## 2021 01 15 Q1 (10 points)
Suppose you need to design the data model that supports the structure and organization of a university campus. The campus comprises several buildings. Each building has an address, a map, some photos, an opening schedule. Every building is either: a Department (office building for faculty), a service building (i.e., Dean’s office, administration, general services, and so on), a teaching building (including classrooms). A building has several floors that, in turn, have several rooms. Each building, each floor, and each room has a unique code, and a type (classroom, restroom, hall, ... ). Each room includes a set of facilities, a set of furniture items, the number of available seats, and the access level. The possible access levels are: public, restricted to all employees, and restricted only to one or more specific employees. In the latter case, the room is associated with the respective employees (one or more). Courses have a title, code, description, and associated main instructor and teaching team, and a list of subscribed students. Courses have also associated websites, materials, and exams. Access to buildings and offices are registered electronically. Moreover, a building automation solution monitors the buildings by observing the temperature, the electricity consumption, and the presence of people. 
Describe a high-level model of the data focusing on which parts of the data you would implement using relational and non-relational solutions. **Motivate your choice**, and for each piece of the solution, represent a schema (if relational) or exemplify the data model (if not relational).