# pyhack19
Pygmalion 2019
## Inspiration
Nearly a thousand children died of heatstroke in the cars. This year alone, 44 of them died because busy parents forgot about them. The trend is likely to continue given the earth's hotter climate. 

As a dad of a beautiful daughter myself, I don't want this to happen. 

Thus, I assembled a team of production engineers, home makers, and reliability specialists to build an IoT device/system that will alert parents before the tragedy happens.

## What it does
Our system learns to recognize the face of your child and alert the parent when they left their child in their car. 

The system (SKID) consists of: i) a camera facing passenger seats and ii) an onboard computer (a raspberry pi and/or a Macbook). The system starts when the car is stopped. The camera continuously analyze the face of the child. At the same time, the onboard computer continuously ping the parent's phone (via Bluetooth/Wifi). 

When the parent's phone is out of reach for the onboard computer and the child's face is still visible, an alert will be sent to the parent's phone. 

A child is saved.

## How I built it
We use following technologies:
- a Logitech webcam to capture jpg images (1 frame per second).
- a raspberry pi and a Macbook for receiving images from the camera.
- a Python face recognition API based on OpenCV/PIL to annotate the children face.
- a shared Dropbox folder to store the image containing the annotated face of the child
- a Slack webhook API for sending notification

## Challenges I ran into
- the face recognition API requires some special compilation configuration on Macbook
- the face recognition API requires some training of the child's image, for the purpose of a demo, we use a small training data set
- the Slack webhook does not allow image upload, so we included a link to the image
- setting up the camera on raspberry pi was a bit painful. We had a raspbrerry pi camera that did not work, so we had to pivot to webcam.

## Accomplishments that I'm proud of
- our system works in near real-time 
- conceptually the systems components are simple and thus more reliable

Our system will save lives of many children.

## What I learned
- python face recognition api
- python http requests manipulation
- raspberry pi hardware issues. 

## What's next for carhack

We hope that large car manufacturers such as Ford, Tesla, or Toyota will adopt this idea on their commercial products.
