# postgrae-asignment

step 1 ==> install viertualenv ==> pip install virtualenv

step 2 ==> using virtualenv ==> virtualenv venv

step 3 ==> Activate virtualenv ==> source venv/Scripts/activate 

step - 4 ==> Install all dependencies ==> pip install -r requirements.txt

All these steps are optional if you want to run locally then the steps are mandatory

After this to runt he server ==> python manage.py runserver ==> it will start the server locally on 8000 port bydefault

deploymentlink ==> https://postgrae-asignment.vercel.app/

Apis ==>

create Booking api endpoint ==> https://postgrae-asignment.vercel.app/booking_retreat/bookings/

input data ==> {
    "user_id" : 2,
    "user_name" : "arin",
    "user_email" : "arindam@gmail.com",
    "user_phone" : "0303k303k3",
    "retreat_id" : 3,
    "retreat_title" : "testing",
    "retreat_location" : "durgapur",
    "retreat_price" : "0404",
    "retreat_duration" : 4,
    "payment_details" : "940403",
    "booking_date" : "2024/05/06"
}

fetch retreate endpoint ==> https://postgrae-asignment.vercel.app/booking_retreat/retreat/


create retreat api endpoint ==> https://postgrae-asignment.vercel.app/booking_retreat/retreat/

input data ==> [
  {
    "title": "Yoga for Stress Relief",
    "description": "A weekend retreat focused on yoga and meditation to relieve stress.",
    "date": 1692921600,
    "location": "Goa",
    "price": 200,
    "type": "Signature",
    "condition": "Stress Relief",
    "image": "https://cdn.midjourney.com/a287f9bc-d0fb-4e78-a0fa-e8136d3c408a/0_0.jpeg",
    "tag": [
      "relaxation",
      "meditation",
      "weekend"
    ],
    "duration": 3
  },
  {
    "title": "Flexibility Improvement Workshop",
    "description": "A 5-day workshop designed to improve flexibility through yoga.",
    "date": 1694304000,
    "location": "Rishikesh",
    "price": 500,
    "type": "Standalone",
    "condition": "Flexibility Improvement",
    "image": "https://cdn.midjourney.com/4eef5d57-1601-4b80-8e82-523003e9f95d/0_0.jpeg",
    "tag": [
      "flexibility",
      "yoga",
      "workshop"
    ],
    "duration": 5
  },
  {
    "title": "Weight Loss Retreat",
    "description": "A 7-day retreat focused on weight loss through yoga and diet.",
    "date": 1696118400,
    "location": "Kerala",
    "price": 700,
    "type": "Signature",
    "condition": "Weight Loss",
    "image": "https://cdn.midjourney.com/bc82ebc6-a3a4-4eda-be0b-bb3e65d4b8d3/0_1.jpeg",
    "tag": [
      "weight loss",
      "diet",
      "yoga"
    ],
    "duration": 7
  },
  {
    "title": "General Fitness Yoga Camp",
    "description": "A 3-day yoga camp to enhance overall fitness and well-being.",
    "date": 1694736000,
    "location": "Mumbai",
    "price": 300,
    "type": "Standalone",
    "condition": "General Fitness",
    "image": "https://cdn.midjourney.com/930ec767-aa6d-46e6-92a6-f019a9718304/0_3.jpeg",
    "tag": [
      "fitness",
      "yoga",
      "camp"
    ],
    "duration": 3
  },
  {
    "title": "Chronic Pain Management",
    "description": "A weekend retreat to manage chronic pain through specialized yoga techniques.",
    "date": 1700438400,
    "location": "Delhi",
    "price": 250,
    "type": "Signature",
    "condition": "Chronic Pain Management",
    "image": "https://cdn.midjourney.com/5b0cec06-2f37-4828-8602-316f6dbd0eb6/0_0.jpeg",
    "tag": [
      "pain management",
      "yoga",
      "weekend"
    ],
    "duration": 2
  },
  {
    "title": "Mental Wellness Retreat",
    "description": "A 4-day retreat focused on mental wellness through yoga and meditation.",
    "date": 1701734400,
    "location": "Pune",
    "price": 400,
    "type": "Standalone",
    "condition": "Mental Wellness",
    "image": "https://cdn.midjourney.com/32923aeb-db8c-4c27-8e9d-fb82928b7fc1/0_2.jpeg",
    "tag": [
      "mental wellness",
      "meditation",
      "yoga"
    ],
    "duration": 4
  },
  {
    "title": "Pre/Post-Natal Yoga",
    "description": "A specialized yoga program for pre and post-natal women.",
    "date": 1693872000,
    "location": "Chennai",
    "price": 350,
    "type": "Standalone",
    "condition": "Pre/Post-Natal",
    "image": "https://cdn.midjourney.com/1bf1a655-289a-48e4-a156-0dde0cf1b7ce/0_1.jpeg",
    "tag": [
      "pre-natal",
      "post-natal",
      "yoga"
    ],
    "duration": 3
  },
  {
    "title": "Detox Retreat",
    "description": "A 5-day detox retreat to cleanse the body and mind.",
    "date": 1699574400,
    "location": "Hyderabad",
    "price": 550,
    "type": "Signature",
    "condition": "Detox",
    "image": "https://cdn.midjourney.com/873b60f7-f026-40f9-b2d7-184e981ee1f5/0_3.jpeg",
    "tag": [
      "detox",
      "cleanse",
      "yoga"
    ],
    "duration": 5
  },
  {
    "title": "Spiritual Growth Retreat",
    "description": "A 7-day retreat focusing on spiritual growth through yoga and meditation.",
    "date": 1702598400,
    "location": "Varanasi",
    "price": 800,
    "type": "Signature",
    "condition": "Spiritual Growth",
    "image": "https://cdn.midjourney.com/e0dba42d-84bc-45e6-acca-bbaf8f817371/0_1.jpeg",
    "tag": [
      "spiritual growth",
      "meditation",
      "yoga"
    ],
    "duration": 7
  },
  {
    "title": "General Fitness Yoga Camp",
    "description": "A 3-day yoga camp to enhance overall fitness and well-being.",
    "date": 1695168000,
    "location": "Kolkata",
    "price": 350,
    "type": "Standalone",
    "condition": "General Fitness",
    "image": "https://cdn.midjourney.com/5d5f32ef-c40a-4258-9856-85db2f4f943a/0_0.jpeg",
    "tag": [
      "fitness",
      "yoga",
      "camp"
    ],
    "duration": 3
  },
  {
    "title": "Yoga Event 11",
    "description": "A description for Yoga Event 11.",
    "date": 1723566880,
    "location": "Pune",
    "price": 704,
    "type": "Signature",
    "condition": "Chronic Pain Management",
    "image": "https://cdn.midjourney.com/ec4680e8-d074-4a69-a24b-3d3f3946907b/0_2.jpeg",
    "tag": [
      "yoga",
      "camp",
      "weekend"
    ],
    "duration": 10
  },
  {
    "title": "Yoga Event 12",
    "description": "A description for Yoga Event 12.",
    "date": 1725678184,
    "location": "Chennai",
    "price": 376,
    "type": "Signature",
    "condition": "Chronic Pain Management",
    "image": "https://cdn.midjourney.com/02d7f36d-ba93-4850-b555-3ede5a22eca8/0_0.jpeg",
    "tag": [
      "diet",
      "meditation",
      "pain management"
    ],
    "duration": 7
  },
  {
    "title": "Yoga Event 13",
    "description": "A description for Yoga Event 13.",
    "date": 1734745782,
    "location": "Delhi",
    "price": 737,
    "type": "Signature",
    "condition": "Detox",
    "image": "https://cdn.midjourney.com/6eb2d2b3-eb07-427a-89f1-b5ac2df1c8f1/0_2.jpeg",
    "tag": [
      "pain management",
      "meditation",
      "relaxation"
    ],
    "duration": 4
  },
  {
    "title": "Yoga Event 14",
    "description": "A description for Yoga Event 14.",
    "date": 1734056561,
    "location": "Chennai",
    "price": 107,
    "type": "Standalone",
    "condition": "Mental Wellness",
    "image": "https://cdn.midjourney.com/e6c8452a-af8e-4cd3-b15a-c3dcf2a696a5/0_3.jpeg",
    "tag": [
      "workshop",
      "weight loss",
      "meditation"
    ],
    "duration": 7
  },
  {
    "title": "Yoga Event 15",
    "description": "A description for Yoga Event 15.",
    "date": 1729939908,
    "location": "Rishikesh",
    "price": 882,
    "type": "Signature",
    "condition": "Detox",
    "image": "https://cdn.midjourney.com/30ee2214-0810-4e17-aa5e-0c2edc1b4354/0_0.jpeg",
    "tag": [
      "spiritual growth",
      "diet",
      "weekend"
    ],
    "duration": 10
  },
  {
    "title": "Yoga Event 16",
    "description": "A description for Yoga Event 16.",
    "date": 1725472451,
    "location": "Delhi",
    "price": 311,
    "type": "Signature",
    "condition": "Flexibility Improvement",
    "image": "https://cdn.midjourney.com/2f9daef3-406b-4266-835e-a07fb09b4820/0_0.jpeg",
    "tag": [
      "relaxation",
      "spiritual growth",
      "flexibility"
    ],
    "duration": 3
  },
  {
    "title": "Yoga Event 17",
    "description": "A description for Yoga Event 17.",
    "date": 1734972658,
    "location": "Goa",
    "price": 555,
    "type": "Standalone",
    "condition": "Mental Wellness",
    "image": "https://cdn.midjourney.com/2f72aafd-e2f2-4bec-8afc-80877aa4634f/0_0.jpeg",
    "tag": [
      "yoga",
      "camp",
      "weekend"
    ],
    "duration": 6
  },
  {
    "title": "Yoga Event 18",
    "description": "A description for Yoga Event 18.",
    "date": 1727628942,
    "location": "Goa",
    "price": 414,
    "type": "Standalone",
    "condition": "Stress Relief",
    "image": "https://cdn.midjourney.com/873b60f7-f026-40f9-b2d7-184e981ee1f5/0_3.jpeg",
    "tag": [
      "weight loss",
      "workshop",
      "pain management"
    ],
    "duration": 2
  },
  {
    "title": "Yoga Event 19",
    "description": "A description for Yoga Event 19.",
    "date": 1732255454,
    "location": "Rishikesh",
    "price": 219,
    "type": "Standalone",
    "condition": "Mental Wellness",
    "image": "https://cdn.midjourney.com/e0dba42d-84bc-45e6-acca-bbaf8f817371/0_1.jpeg",
    "tag": [
      "diet",
      "weekend",
      "flexibility"
    ],
    "duration": 7
  },
  {
    "title": "Yoga Event 20",
    "description": "A description for Yoga Event 20.",
    "date": 1725581902,
    "location": "Varanasi",
    "price": 142,
    "type": "Signature",
    "condition": "Stress Relief",
    "image": "https://cdn.midjourney.com/5d5f32ef-c40a-4258-9856-85db2f4f943a/0_0.jpeg",
    "tag": [
      "weight loss",
      "camp",
      "yoga"
    ],
    "duration": 2
  },
  {
    "title": "Prachi Yoga  Event in pune Organised by usman please visit here",
    "description": "when you will visit i'll tell the description.",
    "date": 1725581902,
    "location": "pune",
    "price": 101,
    "type": "Signature",
    "condition": "Stress Relief",
    "image": "https://images.pexels.com/photos/802417/pexels-photo-802417.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "tag": [
      "weight loss",
      "camp",
      "yoga"
    ],
    "duration": 3
  },
  {
    "title": "Prashant Yoga  Event in Agra Organised by vishal please visit here",
    "description": "Organized by Vishal, this event invites you to experience the profound benefits of yoga in the beautiful city of Agra. Join us for a rejuvenating session that aims to harmonize mind, body, and spirit.",
    "date": 1723581502,
    "location": "Agra",
    "price": 101,
    "type": "Signature",
    "condition": "Stress Relief",
    "image": "https://images.pexels.com/photos/4078093/pexels-photo-4078093.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "tag": [
      "weight loss",
      "camp",
      "meditation"
    ],
    "duration": 5
  }
]
