---
book_slug: smbud-systems-and-methods-for-big-and-unstructured-data
book_title: SMBUD - Systems and Methods for Big and Unstructured Data
chapter_slug: 07-document-databases
chapter_title: 07 Document Databases
created_at: '2022-01-02T21:25:16.000000Z'
id: 82
priority: 3
slug: exam-questions-xJD
title: Exam questions
type: page
updated_at: '2022-01-17T14:17:26.000000Z'
---

# Exam questions

## 2021 06 22 Q2 (6 points)
A dedicated online review and social networking system tracks the activities of customers of hotels, including their stays, their searches and their online interactions, friendships, and activities. Hotels are described by their services, rooms, owner, and employees. Customers can write reviews about each of these aspects. 
1) 	How would you structure the document(s)? (2)

<details>
  <summary>Solution 1</summary>
  
I would store three collections: customers, hotels, interactions, friendships.

The owners, employees, rooms and services would be subdocuments of the hotel document. Reviews would be stored as subdocuments of the entity subject to the interview (hotel, employee, ...). 

Friendships are document where there is reference to the id of the two customers. Interactions work the same way with some fields that specify the type of interaction.

Customers documente include everything about customers. Searched and activities are stored as subdocuments.
Also Stays are stored as subdocuments of customers and they include a reference to the hotel.
</details>

2) 	Which solution is more effective between the document DB and the graph DB, in case we want to explore the connections between customers, reviews, and hotels? Why? (2)
<details>
  <summary>Solution 2</summary>
  
In a such highly connected databsa where there are a lot of reltion a graph db is better. Modeling suchrelations in a document database which does not support joins is painful.
</details>

3) 	Write a graph query using the MongoDB API that extracts hotels that include a swimming pool among their services (2)
<details>
  <summary>Solution 3</summary>
  
```javascript
db.hotels.find({ 
  services: { $elemMatch: { name: "swimming pool" } }
})
```
</details>

4) 	Write a command that adds a new hotel in the database. (2)
<details>
  <summary>Solution 4</summary>
  
```javascript
db.hotels.insert({ 
  name: "Superior",
  address: "Viale 11, milano, italia",
  services: [ { name: "swimming pool" } ],
  owners: [ {name: "Mario Rossi"} ],
  ...
})
```
</details>

## 2021 02 04 (6 points)
A maintenance and service management company supports public administrations in the management of public properties (parks, streets, and so on). The company needs to record the notification of maintenance needs and how they are addressed. Citizens can submit issues in the system which can be of different types (urgent maintenance, cleaning services, damage repair), and are described by a title, city, address, and description, possibly including photos.
City administrators can review the notifications and approve them. Approved ones need to be addressed, therefore the company assigns a maintenance team to the issue and assigns a schedule for the operations. The team may be composed of employees, including a team leader plus one or more team members, plus a set of vehicles and of devices (cleaning machines, lawn mowers, and so on). At the end, a report on the work done is filed into the system.  Information about the employees, vehicles and devices is stored in the system.

Suppose you want to record in a document-based storage the reports of works done. The report must include: the reference to the issue, address, date, start time, end time, the team structure (as a subdocument including the leader and the members), the list of consumables used (with name, brand, quantity used), a description of the issue and work done, and possible request for follow-up interventions. Assume you can use a DB technology like MongoDB.
1.  Represent as a JSON an example document that supports these needs. (1.5)
<details>
  <summary>Solution 1</summary>
  
```json
{
	"issue": "urgent mainteance",
	"address": {
		"street": "Viale Monza",
		"number": "28B",
		"city": "Milan"
	},
	"date": ISODate("2021-12-13"),
	"startTime": ISODate("2021-12-13T13:20:00Z"),
	"endTime": ISODate("2021-12-13T15:20:00Z"),
	"team": {
		"leader": {
			"fullName": "Mario Rossi",
			"birthDate": ISODate("1990-12-01")
		},
		"members": [
			{
				"fullName": "Mario Bianchi",
				"birthDate": ISODate("1990-11-01")
			}
		]
	},
	"consumables": [
		{
			"name": "Acido XX",
			"brand": "Perdue",
			"quantity": 1
		}
	],
	"issueDescription": "E' esploso un idrante",
	"workDescription": "Abbiamo sostituito l'idrante. Tutto dovrebbe funzionare",
	"needFollowUp": false
}
```
</details>

2.  Write the following query: Find the documents that describe interventions in the city of Milano on January 29. (1.5)
<details>
  <summary>Solution 2</summary>
  
```javascript
db.reports.find({
  "date" : {"$eq": ISODate("2022-01-29")},
  "address.city": "Milano"
});
```
</details>

3. Write the following query: Find the documents that describe interventions that consumed more than 5 consumables (meaning, total quantity of consumables being at least 5, counting all the consumables in the intervention). (1.5)
<details>
  <summary>Solution 3</summary>
  
```javascript
db.reports.aggregate([
    {
        '$addFields': {
            'totalConsumables': {
                '$sum': '$consumables.quantity'
            }
        }
    }, {
        '$match': {
            'totalConsumables': {
                '$gte': 5
            }
        }
    }, {
        '$project': {
            'totalConsumables': 0
        }
    }
]);
```
</details>

4. Write a command that inserts a new report in the collection. The report must contain at least 3 features, 2 team members, and 1 consumable. (1.5)
<details>
  <summary>Solution 4</summary>
  
```javascript
db.reports.insertOne({
  // See (1)
});
```
</details>


## 2021 01 15 (5 points)
Suppose you want to record in a document-based storage solution a list of scientific articles. Each article is described by a title, a list of authors with respective affiliation and email, the number of pages, an abstract and the actual content. Content includes paragraphs, in turn containing text, table and images. Paragraphs can also recursively contain subparagraphs, with the same structure. An article includes also references to other articles (bibliography). As an example:
```json
{
  _id: doc1,
  Title: "X",
  Authors: [
  	{name="A", affiliation="Polimi"}, 
  	{name="B", affiliation="KTH"},
  …],
  Pages:45,
  Abstract: "…",
  Content: [
  	{section: "S1", title: "T1", text: "…"},
  	{section: "S2", title: "T2", text: "…", imgs: […] },
  …],
  Bibliography: [{paper: doc2}, {paper: doc3}, …]
}
```
Write the following queries:
1.	Find the documents written by at least one author from “PoliMi” that contains at least 20 pages and includes a section titled “Big Data” at any of the 3 top-most section levels
<details>
  <summary>Solution 1</summary>
  
```javascript
db.articles.find({
	"Authors": { $elemMatch: {affiliation: "PoliMi"} },
	"Pages": { $gte: 20 },
	$or: [
		{"Content": { $elemMatch: {title: "Big Data"} }},
		{"Content.subparagraphs": { $elemMatch: {title: "Big Data"} }},
		{"Content.subparagraphs.subparagraphs": { $elemMatch: {title: "Big Data"} }},
	]
})
```
</details>

2.	Find the documents that include a reference to another article written by at least one author from “UniMi”
<details>
  <summary>Solution 2</summary>
  
```javascript
db.articles.aggregate([
    $lookup: {
        from: "articles",
        localField: "Bibliography.paper",
        foreignField: "_id",
        as: "bib"
    },
    $match: {
        "bib.Authors": {$elemMatch: {affiliation: "UniMi"}}
    },
    $project: {
        bib: 0
    }
])
```
</details>