//	Joe Merten - Homework assignment - People Pt.2 (MongoDB Queries)

In people collection
=======================
 1 - Add a person to the collection. You pick the data, but they should have an empty array for children.
 db.people.insertOne(
	{  first_name: 'Tim',
	  last_name: 'Adams',
	  email: 'whome@nowhere.cn',
	  gender: 'Male',
	  age: 22,
	  state: 'Minnesota',
	  children: []
	}
 )
 //Confirm:
 db.people.find({email: 'whome@nowhere.cn'})

 2 - Add another person. They should have at least two children.
 db.people.insertOne(
	{  first_name: 'Mary',
	  last_name: 'Jones',
	  email: 'mjones@nowhere.com',
	  gender: 'female',
	  age: 30,
	  state: 'Minnesota',
	  children: [
		{
		  name: 'Thing 2',
		  age: 1
		},
		{
		  name: 'Thing 1',
		  age: 3
		}
	]
	}
 )
 //Confirm:
 db.people.find({email: 'mjones@nowhere.com'})

 3 - Update one person named Clarence. He moved from North Dakota to South Dakota.
 db.people.updateOne(
	{first_name: 'Clarence'},
	{
		$set: {state: 'South Dakota'}
	}
 )
 //Confirm:
 db.people.find({first_name: 'Clarence'})


 4 - Update Rebecca Hayes. Remove her email address.
 db.people.updateOne(
 	{$and: [
		{first_name: 'Rebecca'},
		{last_name: 'Hayes'}
	] },
	{
		$unset: {email: ''}
	}
 )
 //Confirm:
 db.people.find(
	{$and: [
		{first_name: 'Rebecca'},
		{last_name: 'Hayes'}
	] }
)


 5 - Update everyone from Missouri. They all had a birthday today, so add one to their age. (expect 4 matches)
db.people.updateMany(
	{state: 'Missouri'},
	{ $inc: { age: 1 } }
)
 //Confirm: 47, 60, 51, 29 before....
 db.people.find(
	{state: 'Missouri'},
	{first_name: 1, last_name: 1, age: 1}
)
// After 48, 61, 52, 30

 6 - Jerry Baker has updated information. Replace with a new document:
{ first_name: "Jerry", last_name: "Baker-Mendez", email: "jerry@classic.ly", gender:"Male", age: 28, state: "Vermont", "children": [{name: "Alan", age: 18}, {name: "Jenny", age: 3}] }
//	pre update:
 db.people.find(
	{$and: [
		{first_name: 'Jerry'},
		{last_name: 'Baker'}
	] }
)
db.people.replaceOne(
	{$and: [
		{first_name: 'Jerry'},
		{last_name: 'Baker'}
	] },
	{ first_name: "Jerry", last_name: "Baker-Mendez", email: "jerry@classic.ly", gender:"Male", age: 28, state: "Vermont", "children": [{name: "Alan", age: 18}, {name: "Jenny", age: 3}] }
)
//	post update check 1 = equals zero documents
 db.people.find(
	{$and: [
		{first_name: 'Jerry'},
		{last_name: 'Baker'}
	] }
).count()
//	post update check 2 = equals one document
 db.people.find(
	{$and: [
		{first_name: 'Jerry'},
		{last_name: 'Baker-Mendez'}
	] }
).count()

 7 - Delete Wanda Bowman.
//	pre update:
 db.people.find(
	{$and: [
		{first_name: 'Wanda'},
		{last_name: 'Bowman'}
	] }
)

db.people.remove(
	{$and: [
		{first_name: 'Wanda'},
		{last_name: 'Bowman'}
	] }
)

//	post update:  Yup, she's gone ;-)
 db.people.find(
	{$and: [
		{first_name: 'Wanda'},
		{last_name: 'Bowman'}
	] }
)

 8 - Delete everyone who does not have an email address specified. (expect 36 matches - maybe more depending what you added above)
//	pre update #1 - This only count 1 document:
 db.people.find(
		{ "email" : { "$exists" : false } }
).count()
//	pre update #2 - This also only count 1 document:
 db.people.find(
		{ "email" : { "$exists" : null } }
).count()
//	pre update #3 - There are 203 documents...
db.people.find().count()
//	First delete...  deletedCount: 1
db.people.deleteMany(
		{ "email" : { "$exists" : false } }
)
//	Appaarrently that was the same document, there are no documents that match
//  { "email" : { "$exists" : null } }
//  202 documents left.
db.people.find(
		{ "email" : { "$exists" : null } }
).count()




In submissions collection
=============================
 9 - Add several documents to a new submissions collection. Do it all in one command. (Remember, MongoDB will create the collection for you. Just start adding documents.)
     a - title: "The River Bend", upvotes: 10, downvotes: 2, artist: <ID of Anna Howard>
     b - title: "Nine Lives", upvotes: 7, downvotes: 0, artist: <ID of Scott Henderson>
     c - title: "Star Bright", upvotes: 19, downvotes: 3, artist: <ID of Andrea Burke>
     d - title: "Why Like This?", upvotes: 1, downvotes: 5, artist: <ID of Steven Marshall>
     e - title: "Non Sequitur", upvotes: 11, downvotes: 1, artist: <ID of Gerald Bailey>
 db.people.find(
	{$and: [
		{first_name: 'Anna'},
		{last_name: 'Howard'}
	] }
)
//  https://www.mongodb.com/community/forums/t/insert-values-from-one-collection-to-fields-in-another-collection/156403
//  https://groups.google.com/g/mongodb-user/c/X9UltGPVpnw/m/z9LVo7s8CQAJ?pli=1

db.submissions.insertMany( [
	{ title: "The River Bend", upvotes: 10, downvotes: 2, artist:  ObjectId("6449cfdfd35f4bff0d3c4efb") },
	{ title: "Nine Lives", upvotes: 7, downvotes: 0, artist: ObjectId("6449cfdfd35f4bff0d3c4f29") },
	{ title: "Star Bright", upvotes: 19, downvotes: 3, artist: ObjectId("6449cfdfd35f4bff0d3c4fac") },
	{ title: "Why Like This?", upvotes: 1, downvotes: 5, artist: ObjectId("6449cfdfd35f4bff0d3c4f32") },
	{ title: "Non Sequitur", upvotes: 11, downvotes: 1, artist: ObjectId("6449cfdfd35f4bff0d3c4ef9") }
] )

10 - Add 2 upvotes for "The River Bend".
//	 pre-update = 10 upvotes...
db.submissions.find(
	{ title: "The River Bend"}
)
//	Do the update...
db.submissions.updateOne(
   { title: "The River Bend" },
   { $inc: { upvotes: +2 } }
)
//	 pre-update = 12 upvotes...
db.submissions.find(
	{ title: "The River Bend"}
)



11 - Add a field round2 = true to all submissions with at least 10 upvotes. (expect 3 matches)
//	 pre-update = found three...
db.submissions.find(
	{ upvotes: { $gt: 10 } }
)
//	Do the update...
//	 matchedCount: 3,
//	 modifiedCount: 3,
db.submissions.updateMany(
   { upvotes: { $gt: 10 } },
   { $push: { round2: true } }
)
//	Post update...  This worked, but appears to have added it as an array/list
db.submissions.find(
	{ upvotes: { $gt: 10 } }
)


Extended Challenges:
=====================
12 - Update Helen Clark. She had a baby! Add a child, name: Melanie, age: 0.


13 - Joan Bishop has a child named Catherine. She just had a birthday and prefers to go by "Cat". In one query update the child's name to "Cat" and increment her age by one.


14 - List all submissions that have more downvotes than upvotes.


mongodb+srv://kc8son:xafl8iLm6IGXVMBZ@cluster0.utmyy3i.mongodb.net/test